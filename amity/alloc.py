from people import Manager, Staff
from building import Room, Amity, LivingSpace, Office
from random import randint


def generate_rooms(room_type, n=10):
    """This function can be used to generate rooms.
       It should be called with <room_type> and <n:number_of_rooms>
       It returns list of room objects.
    """
    start = Amity.room_count or Amity.room_count + 1
    rooms = [Room("Room {0}".format(i),
             room_type) for i in xrange(start, start+n)]
    return rooms


@staticmethod
def assign_to_office(office, person):
    """Assign person to an office.
    """
    if not office.filled():
        office.add_occupant(person)


@staticmethod
def get_list_of_allocations():
    """This gets the list of allocations
    """
    pass


@staticmethod
def print_list_of_allocations():
    """This prints the list of allocations
    """
    pass


@staticmethod
def get_list_of_unallocated():
    """This gets the list of unallocated people
    """
    pass


@staticmethod
def print_members_in_room(room_name):
    """Given a room, this prints all members in it.
    """
    pass


@staticmethod
def assign_to_room(room_name, person_name):
    """Assign a person to a room.
    """
    person = Amity.find_person(person_name)
    room = Amity.find_room(room_name)
    if isinstance(room, Office) and not person.has_office():
        Manager.assign_to_office(room, person)
    elif isinstance(room, LivingSpace) and not isinstance(person, Staff):
        Manager.assign_to_living_space(room, person)


@staticmethod
def assign_to_living_space(living_space, person):
    """Assign a person to a living space.
    """
    if person.has_expressed_interest():
        if person.is_female():
            if living_space.has_no_occupant()\
               or (living_space.has_female_occupant()
               and not living_space.filled()):
                living_space.add_occupant(person)
        else:
            if living_space.has_no_occupant() or not living_space.filled():
                living_space.add_occupant(person)


@staticmethod
def allocate():
    while not (Amity.all_rooms_filled() or Amity.all_persons_assigned()):
        Manager.assign_to_living_space(
                                    Amity.room_collection[randint(0, 20)],
                                    Amity.people_collection[randint(0, 20)]
                                    )


Manager.assign_to_room = assign_to_room
Manager.assign_to_office = assign_to_office
Manager.assign_to_living_space = assign_to_living_space
Manager.allocate = allocate
Manager.get_list_of_unallocated = get_list_of_unallocated
Manager.print_list_of_allocations = print_list_of_allocations
Manager.print_members_in_room = print_members_in_room

if __name__ == '__main__':
    offices = generate_rooms('office')
    Amity.add_rooms(offices)

    living_spaces = generate_rooms('living space')
    Amity.add_rooms(living_spaces)
    print "You have {0} rooms now in Amity".format(Amity.room_count)
