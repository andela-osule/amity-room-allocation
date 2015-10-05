#!/usr/bin/python
# title          :amity/tools.py
# description    :This package allocates people to rooms in a building.
# author         :Oluwafemi Sule
# email          :oluwafemi.sule@andela.com
# date           :20150915
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================

from re import search
from people import Person, Manager
from datetime import datetime

import os


def flatten(args):
    """This function flattens a nested list.
    """
    if isinstance(args, (list, tuple)):
        return [item for arg in args for item in flatten(arg)]
    else:
        return [args]


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
                match = search('^(\w+\s[^\s]+)[\s]{1,}(\w+)[\s]{0,}(\w)?', line)
                group = match.groups()
                name, role, interest = group
                p = Person.make_person(name, role, interest)
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
            file_path = os.getcwd() + '/amity/output/allocation_'\
            + datetime.now().strftime('%d_%m_%Y_%H_%I_%S') + '.txt'
            with open(file_path, 'w+') as f:
                for room, occupants in allocations:
                    f.write(str(room)+'\n')
                    f.write(Manager.get_members_in_room(room.name)+'\n'*2)
            return file_path
        if print_stdio is True:
            Manager.print_list_of_allocations()
