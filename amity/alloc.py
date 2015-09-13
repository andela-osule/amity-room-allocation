from people import Manager, Person
from building import Room, Amity


def generate_rooms(room_type, n=10):
    """This function can be used to generate rooms.
       It should be called with <room_type> and <n:number_of_rooms>
       It returns list of room objects.
    """
    start = Amity.room_count + 1
    rooms = [Room("Room {0}".format(i), room_type) for i in xrange(start, n+1)]
    return rooms


def assign_to_office(self):
    print self.name


def get_list_of_allocations():
    """This gets the list of allocations
    """
    pass


def print_list_of_allocations():
    """This prints the list of allocations
    """
    pass


def get_list_of_unallocated():
    """This gets the list of unallocated people
    """
    pass


def print_members_in_room(room_name):
    """Given a room, this prints all members in it.
    """
    pass


def assign_to_room(self):
    pass

Manager.assign_to_office = assign_to_office

if __name__ == '__main__':
    offices = generate_rooms('office')
    Amity.add_rooms(offices)

    living_spaces = generate_rooms('living space')
    Amity.add_rooms(living_spaces)
    print "You have {0} rooms now in Amity".format(Amity.room_count)
