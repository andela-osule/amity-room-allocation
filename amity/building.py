#!/usr/bin/python
# title          :amity/building.py
# description    :This package allocates people to rooms in a building.
# author         :Oluwafemi Sule
# email          :oluwafemi.sule@andela.com
# date           :20150915
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================

import tools
from random import randint
from exception import OutOfOfficeException, OutOfLivingSpaceException


class Room(object):
    """Factory for creating rooms.
       Instantiate with <name> and <room type>
    """
    def __init__(self, name, room_type):
        self.__class__ = Amity.room_types.get(room_type)
        self.occupants = []
        self.__init__(name)

    def set_name(self, name):
        """Assign name to a room.
        """
        self.name = name

    def get_capacity(self):
        """Get the capacity of a room.
        """
        return self.capacity

    def filled(self):
        """Check if a room is filled with people
        """
        return True if len(self.occupants) == self.capacity else False

    def has_no_occupant(self):
        """Check if a room has an occupant.
        """
        return True if len(self.occupants) == 0 else False


class Office(Room):
    """This represents an office.
       This class should never be instantiated directly.
       Always use Room factory.
    """
    capacity = 6

    def __init__(self, name):
        self.set_name(name)

    def add_occupant(self, person):
        """Add an occupant to a room.
        """
        self.occupants.append(person)
        person.assign_office(self)

    def __repr__(self):
        return "{0} (OFFICE)".format(self.name)


class LivingSpace(Room):
    """This represents a living space.
       This class should never be instantiated directly.
       Always use Room factory.
    """
    capacity = 4

    def __init__(self, name):
        self.set_name(name)

    def has_female_occupant(self):
        """Check if a female occupant is present in the room
        """
        for person in self.occupants:
            if person.is_female():
                return True
        return False

    def add_occupant(self, person):
        """Add an occupant to a room.
        """
        self.occupants.append(person)
        person.assign_living_space(self)

    def __repr__(self):
        return "{0} (LIVING)".format(self.name)


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
        """Update the room count as room collection changes.
        """
        Amity.room_count = len(Amity.room_collection)

    @staticmethod
    def remove_room(room_name):
        """Remove a room by name from the building.
        """
        room_space = Amity.find_room(room_name)
        try:
            Amity.room_collection.remove(room_space)
        except ValueError:
            print "Room {0} does not exist".format(room_name)
        Amity.update_room_count()

    @staticmethod
    def remove_rooms(*room_names):
        """Remove multiple rooms from the buiding.
           Arguments can be a list of rooms or comma-separated values
        """
        room_name_list = tools.flatten(list(room_names))
        for room_name in room_name_list:
            Amity.remove_room(room_name)

    @staticmethod
    def find_room(room_name):
        """Find a room by name
        """
        for room in Amity.room_collection:
            if room.name == room_name:
                return room
        return None

    @staticmethod
    def add_person(person):
        """Add a person to the people collection
        """
        Amity.people_collection.append(person)

    @staticmethod
    def add_persons(*persons):
        """Add persons to the people collection
        """
        persons_list = tools.flatten(list(persons))
        for person in persons_list:
            Amity.add_person(person)

    @staticmethod
    def reset_room_count():
        """Reset room count to zero
        """
        Amity.remove_rooms([room.name for room in Amity.room_collection])

    @staticmethod
    def find_person(person_name):
        """Find a person in the people_collection by <person_name>
           and returns a person object instance from the collection
        """
        for person in Amity.people_collection:
            if person.name == person_name:
                return person
        return None

    @staticmethod
    def all_rooms_filled():
        """Check if all rooms are filled
        """
        for room in Amity.room_collection:
            if not room.filled():
                return False
        return True

    @staticmethod
    def all_persons_assigned():
        """Check if every person has room
        """
        for person in Amity.people_collection:
            if not person.has_office():
                return False
        return True

    @staticmethod
    def find_living_space_with_female_occupant():
        """Find a living space with a female occupant
        """
        for room in Amity.room_collection:
            if isinstance(room, LivingSpace):
                if room.has_female_occupant() and not room.filled():
                    return room
            elif not isinstance(room, LivingSpace):
                if room.filled():
                    return room
        return None

    @staticmethod
    def get_random_office():
        """Get a random office
        """
        offices = [room for room in Amity.room_collection
                   if isinstance(room, Office) and not room.filled()]
        try:
            o = offices[randint(0, len(offices)-1)]
            return o
        except:
            raise OutOfOfficeException()

    @staticmethod
    def get_random_living_space():
        """Get a random living space
        """
        living_spaces = [room for room in Amity.room_collection
                         if isinstance(room, LivingSpace)
                         and not room.filled()]
        try:
            l = living_spaces[randint(0, len(living_spaces)-1)]
            return l
        except:
            raise OutOfLivingSpaceException()
