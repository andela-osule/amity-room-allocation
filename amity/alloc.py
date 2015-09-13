from people import Manager, Person
from building import Room, Amity


def generate_rooms(room_type, n=10):
    """Generate rooms.
    "  To be called with <room_type> and <n:number_of_rooms>
    "  Returns list of room objects
    """
    start = Amity.room_count + 1
    rooms = [Room("Room {0}".format(i), room_type) for i in xrange(start, n+1)]
    return rooms


def assign_to_office(self):
    print self.name


def assign_to_room(self):
    pass

Manager.assign_to_office = assign_to_office

if __name__ == '__main__':
    offices = generate_rooms('office')
    Amity.add_rooms(offices)

    living_spaces = generate_rooms('living space')
    Amity.add_rooms(living_spaces)
    print "You have {0} rooms now in Amity".format(Amity.room_count)
