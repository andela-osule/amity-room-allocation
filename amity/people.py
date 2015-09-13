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

    def make_person(self, role, has_expr_interest=False):
        """Create an instance of either Fellow or Staff object.
        "  <role> argument must be passed in.
        """
        self.__class__ = Role.title[role.lower()]
        self.name = Person.name
        self.sex = Person.sex
        if self.__class__ is Fellow:
            self.has_expressed_interest = has_expr_interest
        return self


class Fellow(Person):
    """This represents a person who is a fellow.
    """
    def can_have_living_space(self):
        return True if self.has_expressed_interest else False

    def __repr__(self):
        return "Fellow: {0}".format(self.name)


class Staff(Person):
    """This represents a person who is a staff.
    """
    def __repr__(self):
        return "Staff: {0}".format(self.name)


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
