#!/usr/bin/python
# title          :amity/people.py
# description    :This package allocates people to rooms in a building.
# author         :Oluwafemi Sule
# email          :oluwafemi.sule@andela.com
# date           :20150915
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================

import abc


class Person(object):
    """This represents a person.
       It must be instantiated with <full name> and <sex>
       Example: p = Person('Jack Frost', 'M')
    """

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    @staticmethod
    def make_person(name, role, sex='M', has_expr_interest=False):
        """This creates an instance of either Fellow or Staff object.
           The <role> argument must be passed in.
        """
        special_person = Role.title[role.lower()]
        person = special_person(name, sex)
        person.office = None
        if isinstance(person, Fellow):
            if has_expr_interest == 'Y'\
               or has_expr_interest is True:
                person.has_expressed_interest = True
            else:
                person.has_expressed_interest = False

            person.living_space = None
        return person

    def has_office(self):
        """This checks if a person has been assigned an office
        """
        return True if self.office is not None else False

    def assign_office(self, office):
        """This assigns a person to an office
            Second argument is an office object
        """
        self.office = office

    def is_female(self):
        """This checks if a person is female.
        """
        return True if self.sex is 'F' else False


class Fellow(Person):
    """This represents a person who is a fellow.
    """
    def can_have_living_space(self):
        return True if self.has_expressed_interest else False

    def has_living_space(self):
        """This checks if a fellow has living space
        """
        return True if self.living_space is not None else False

    def assign_living_space(self, room):
        """This assign a fellow a living space.
            Second argument is a room object.
        """
        self.living_space = room

    def __repr__(self):
        return "Fellow: {0}".format(self.name)


class Staff(Person):
    """This represents a person who is a staff.
    """

    def can_have_living_space(self):
        """Check if a staff can have living space.
           This returns always return False.
        """
        return False

    def __repr__(self):
        return "Staff: {0}".format(self.name)


class Manager(Staff):
    """This represents a Manager
    """
    __metaclass__ = abc.ABCMeta


class Role:
    """This manages the title that a person can take on
    """
    title = {'fellow': Fellow, 'staff': Staff, 'manager': Manager}
