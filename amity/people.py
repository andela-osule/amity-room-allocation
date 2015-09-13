class Person(object):
    """This represents a person.
    "   Must be instantiated with full name.
    """
    name = ''

    def __init__(self, name):
        Person.name = name

    def make_person(self, role):
        self.__class__ = Role.title[role]
        self.name = Person.name
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
    pass


class Role:
    """This manages titles that person can take on
    """
    title = {'fellow': Fellow, 'staff': Staff, 'manager': Manager}
