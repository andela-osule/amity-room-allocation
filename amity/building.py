import tools


class Room(object):
    """Factory for creating rooms.
       Instantiate with <name> and <room type>
    """
    def __init__(self, name, room_type):
        self.__class__ = Amity.room_types.get(room_type)
        self.__init__(name)

    def set_name(self, name):
        self.name = name

    def get_capacity(self):
        return self.get_capacity()


class Office(Room):
    """This represents an office.
       This class should never be instantiated directly.
       Always use Room factory.
    """
    capacity = 6

    def __init__(self, name):
        self.set_name(name)

    def __repr__(self):
        return "Office: {0}".format(self.name)


class LivingSpace(Room):
    """This represents a living space.
       This class should never be instantiated directly.
       Always use Room factory.
    """
    capacity = 4

    def __init__(self, name):
        self.set_name(name)

    def __repr__(self):
        return "Living Space: {0}".format(self.name)


class Amity:
    """This represents the company building.
       Rooms can be added to company building.
    """
    people_collection = []
    room_collection = []
    room_types = {'office': Office,
                  'living space': LivingSpace}
    room_count = 0

    @staticmethod
    def add_room(room):
        """Add room object to the building.
        """
        if tools.get_parent(room) is Room:
            Amity.room_collection.append(room)
        Amity.update_room_count()

    @staticmethod
    def add_rooms(*rooms):
        """ Add multiple room objects to the building.
        """
        room_list = tools.flatten(rooms)
        for room in room_list:
            Amity.add_room(room)

    @staticmethod
    def update_room_count():
        Amity.room_count = len(Amity.room_collection)

    @staticmethod
    def remove_room(room_name):
        """Removes a room by name from the building.
        """
        room_index = Amity.find_room(room_name)
        try:
            del Amity.room_collection[room_index]
        except IndexError:
            print "Room {0} does not exist".format(room_name)
        Amity.update_room_count()

    @staticmethod
    def remove_rooms(*room_names):
        """Removes multiple rooms from the buiding.
           Arguments can be a list of rooms or comma-separated values
        """
        room_name_list = tools.flatten(list(room_names))
        for room_name in room_name_list:
            Amity.remove_room(room_name)

    @staticmethod
    def find_room(room_name):
        for index, room in enumerate(Amity.room_collection):
            if room.name in room_name:
                return index

    @staticmethod
    def add_person(person):
        """Adds a person to the people collection
        """
        Amity.people_collection.append(person)

    @staticmethod
    def add_persons(*persons):
        """Add persons to the people collection
        """
        persons_list = tools.flatten(list(persons))
        for person in persons_list:
            Amity.add_person(person)
