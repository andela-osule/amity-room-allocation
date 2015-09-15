from re import search
from people import Person, Manager

import os


def flatten(args):
    """This function flattens a nested list.
    """
    if isinstance(args, (list, tuple)):
        return [item for arg in args for item in flatten(arg)]
    else:
        return [args]


def get_parent(arg):
    """Return parent class of the arg
    """
    return arg.__class__.__base__


class PeopleFileParser:
    """This represents a class of methods for parsing text.
    """

    @staticmethod
    def parse_persons(datafile='amity/data_samples/people.txt',
                      add=True,
                      output=None):
        """Parses person from a file.

           Call with datafile path.

           Optional arguments are <add> and <output>
        """
        persons = []
        with open(datafile, 'r') as people_file:
            for line in people_file:
                s = search('^(\w+\s[^\s]+)[\s]{1,}(\w+)[\s]{0,}(\w)?', line)
                g = s.groups()
                name, role, interest = g
                p = Person(name).make_person(role, interest)
                persons.append(p)
        if add:
            from building import Amity
            Amity.add_persons(persons)
        if output is 'print':
            print persons
        return persons

    @staticmethod
    def line_to_person(datafile):
        return PeopleFileParser.parse_persons(datafile)


class AllocationWriter:
    @staticmethod
    def write_allocation(print_stdio=False, print_file=False):
        allocations = Manager.get_list_of_allocations()
        if print_file is True:
            with open(os.getcwd()+'/amity/output/allocation.txt', 'w+') as f:
                for room, occupants in allocations:
                    f.write(str(room)+'\n')
                    f.write(Manager.get_members_in_room(room.name)+'\n'*2)
        if print_stdio is True:
            Manager.print_list_of_allocations()
