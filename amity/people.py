class Fellow:
    def __init__(self, name):
        self.name = name


class Staff:
    def __init__(self, name):
        self.name = name


class Person(object):
    """This represents a person.
    "   Must be instantiated with full name of person and role.
    "   Role could be fellow or staff
    """
    __roles = {'fellow': Fellow, 'staff': Staff}

    def make_person(self, name, role):
        return Person.__roles[role](name)

    def __init__(self, name, role):
        self.__class__ = Person.get_role_class(role)
        self.__init__()
        self.name = name
