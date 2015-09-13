import abc


class Person(object):
    """This represents a person.
    "   Must be instantiated with <full name> and <sex>
    "   Example: p = Person('Jack Frost', 'M')
    """
    name = ''
    sex = ''

    def __init__(self, name, sex='M'):
        Person.name = name
        Person.sex = sex

    def make_person(self, role):
        self.__class__ = Role.title[role.lower()]
        self.name = Person.name
        self.sex = Person.sex
        return self


class Fellow(Person):
    """This represents a person who is a fellow.
    """
    def can_have_living_space(self):
        return True


class Staff(Person):
    """This represents a person who is a staff.
    """
    pass


class Manager(Staff):
    """This represents a Manager
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def assign_to_office(self, person, office):
        """Assign a person to an office space
        """
        pass

    @abc.abstractmethod
    def assign_to_room(self, person, room):
        """Assign a person to an living space
        """
        pass


class Role:
    """This manages titles that person can take on
    """
    title = {'fellow': Fellow, 'staff': Staff, 'manager': Manager}
