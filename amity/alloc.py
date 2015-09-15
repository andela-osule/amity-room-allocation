from people import Manager, Fellow
from building import Room, Amity, LivingSpace, Office


def generate_rooms(room_type, n=10):
    """This function can be used to generate rooms.
       It should be called with <room_type> and <n:number_of_rooms>
       It returns list of room objects.
    """
    start = (Amity.room_count or Amity.room_count) + 1
    rooms = [Room("Room {0}".format(i),
             room_type) for i in xrange(start, start+n)]
    return rooms


@staticmethod
def assign_to_office(person, room=None):
    """Assign person to an office.
    """
    if room is None:
        room = Amity.get_random_office()
    if not room.filled():
        room.add_occupant(person)


@staticmethod
def get_list_of_allocations():
    """This gets the list of allocations
    """
    return [(room.name, room.occupants) for room in Amity.room_collection]


@staticmethod
def print_list_of_allocations():
    """This prints the list of allocations
    """
    for room_name, occupants in Manager.get_list_of_allocations():
        print room_name
        Amity.print_members_in_room(room_name)


@staticmethod
def print_members_in_room(room_name):
    """Given a room, this prints all members in it.
    """
    room = Amity.find_room(room_name)
    print ', '.join(occupant.name for occupant in room.occupants)


@staticmethod
def get_list_of_unallocated_people():
    """This gets the list of unallocated people
    """
    return [person.name
            for person in Amity.people_collection
            if not person.has_office()
            or (isinstance(person, Fellow)
                and not person.has_living_space())]


@staticmethod
def assign_to_room(person, room_name=None):
    """Assign a person to a room.
        <room_name> is optional.
    """
    # find a person by name
    if type(person) is str:
        person = Amity.find_person(person)
    # find a room by name if specified
    if type(room_name) is str:
        room = Amity.find_room(room_name)
        # is the room an office?
        if isinstance(room, Office):
            if not person.has_office():
                Manager.assign_to_office(person, room)
        # is the room a living space?
        elif isinstance(room, LivingSpace):
            if person.can_have_living_space() and \
             not person.has_living_space():
                Manager.assign_to_living_space(person, room)
    else:
        if not person.has_office():
            Manager.assign_to_office(person)
        if isinstance(person, Fellow) and person.can_have_living_space():
            if not person.has_living_space():
                Manager.assign_to_living_space(person)


@staticmethod
def assign_to_living_space(person, room=None):
    """Assign a person to a living space.
    """
    if room is None:
        room = Amity.get_random_living_space()
    if person.is_female():
        room = Amity.find_living_space_with_female_occupant()\
              or Amity.get_random_living_space()
        if room.has_no_occupant()\
           or room.has_female_occupant():
            room.add_occupant(person)
    else:
        if not room.has_female_occupant() \
         and not person.has_living_space():
            room.add_occupant(person)


@staticmethod
def allocate():
    for person in Amity.people_collection:
        Manager.assign_to_room(person)


Manager.assign_to_room = assign_to_room
Manager.assign_to_office = assign_to_office
Manager.assign_to_living_space = assign_to_living_space
Manager.allocate = allocate
Manager.get_list_of_unallocated_people = get_list_of_unallocated_people
Manager.print_list_of_allocations = print_list_of_allocations
Manager.print_members_in_room = print_members_in_room

if __name__ == '__main__':
    offices = generate_rooms('office')
    Amity.add_rooms(offices)

    living_spaces = generate_rooms('living space')
    Amity.add_rooms(living_spaces)
    print "You have {0} rooms now in Amity".format(Amity.room_count)
