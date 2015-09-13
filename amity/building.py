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
    room = []
    room_types = {'office': Office,
                  'living space': LivingSpace}

    def add_room(self, room):
        room.append(room)
