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
        if type(room) is not list:
            Amity.rooms.append(room)
        else:
            for room_object in room:
                Amity.rooms.append(room_object)
        Amity.update_room_count()

    @staticmethod
    def update_room_count():
        Amity.room_count = len(Amity.rooms)
