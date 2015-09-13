import tools


class Room(object):
    """Factory for creating rooms.
    "  Instantiate with <name> and <room type>
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
    "  Should not be instantiated directly.
    "  Use Room factory.
    """
    capacity = 6

    def __init__(self, name):
        self.set_name(name)


class LivingSpace(Room):
    """This represents a living space.
    "  Should not be instantiated directly.
    "  Use Room factory.
    """
    capacity = 4

    def __init__(self, name):
        self.set_name(name)


class Amity:
    """This represents the company building.
    "  Rooms can be added to company building.
    """

    rooms = []
    room_types = {'office': Office,
                  'living space': LivingSpace}

    @staticmethod
    def add_room(room):
        """Add room object to the building.
        """
        if tools.get_parent(room) is Room:
            Amity.rooms.append(room)
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
        Amity.room_count = len(Amity.rooms)

    @staticmethod
    def remove_room(room_name):
        """Removes a room by name from the building.
        """
        room_index = Amity.find_room(room_name)
        try:
            del Amity.rooms[room_index]
        except IndexError:
            print "Room {0} does not exist".format(room_name)
        Amity.update_room_count()

    @staticmethod
    def remove_rooms(*room_names):
        """Removes multiple rooms from the buiding.
        " Arguments can be a list of rooms or comma-separated
        """
        room_name_list = tools.flatten(list(room_names))
        for room_name in room_name_list:
            Amity.remove_room(room_name)

    @staticmethod
    def find_room(room_name):
        for index, room in enumerate(Amity.rooms):
            if room.name in room_name:
                return index
