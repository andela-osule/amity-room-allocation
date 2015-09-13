from re import search
from people import Person


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
                p = Person(g[0]).make_person(g[1], g[2])
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
    pass
