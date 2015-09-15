import abc


class Person(object):
    """This represents a person.
       It must be instantiated with <full name> and <sex>
       Example: p = Person('Jack Frost', 'M')
    """
    name = ''
    sex = ''

    def __init__(self, name, sex='M'):
        Person.name = name
        Person.sex = sex

    def make_person(self, role, has_expr_interest=False):
        """This creates an instance of either Fellow or Staff object.
           The <role> argument must be passed in.
        """
        self.__class__ = Role.title[role.lower()]
        self.name = Person.name
        self.sex = Person.sex
        self.office = None
        if self.__class__ is Fellow:
            if has_expr_interest == 'Y'\
               or has_expr_interest is True:
                self.has_expressed_interest = True
            else:
                self.has_expressed_interest = False

            self.living_space = None
        return self

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
