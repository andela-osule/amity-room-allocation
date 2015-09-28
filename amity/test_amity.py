#!/usr/bin/python
# title          :amity/test_amity.py
# description    :This package allocates people to rooms in a building.
# author         :Oluwafemi Sule
# email          :oluwafemi.sule@andela.com
# date           :20150915
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================

from building import Amity, Office, Room, LivingSpace
from people import Person, Fellow, Staff, Manager
from random import randint
from tools import PeopleFileParser, AllocationWriter
from exception import OutOfLivingSpaceException, OutOfOfficeException

import nose
import sys
import os
import alloc
import unittest
import os.path

sys.path.insert(0, '../')
os.environ['NOSE_WITH_COVERAGE'] = '1'
os.environ['NOSE_COVER_PACKAGE'] = 'amity'
file_path = 'amity/data_samples/people.txt'


class AmityTestCase(unittest.TestCase):

    def setUp(self):
        self.r = Room('Anvil', 'office')
        self.l = Room('Ruby', 'living space')
        self.f = Person('Jane', 'F').make_person('fellow',
                                                 has_expr_interest=True)
        self.s = Person('Mark').make_person('staff')

    def test_can_create_office_or_living_space(self):
        self.assertIsInstance(self.r, Office)
        self.assertIsInstance(self.l, LivingSpace)

    def test_can_add_room_to_amity(self):
        Amity.reset_room_count()
        Amity.add_room(self.r)
        Amity.add_room(self.l)
        self.assertEquals(Amity.room_count, 2)
        self.assertEquals(Amity.room_collection[1].get_capacity(), 4)
        self.assertEquals(Amity.room_collection[1].has_no_occupant(), True)

    def test_can_remove_room(self):
        Amity.room_collection
        Amity.remove_room(self.r.name)
        self.assertEquals(Amity.room_count, 1)

    def test_can_create_fellow_or_staff(self):
        self.assertIsInstance(self.f, Fellow)
        self.assertIsInstance(self.s, Staff)

    def test_can_assign_singly_to_room(self):
        self.assertEquals(Amity.room_collection[1].has_female_occupant(),
                          False)
        Manager.assign_to_room(self.f, self.l)
        self.assertEquals(Amity.room_collection[1].has_female_occupant(), True)


class AllocTestCase(unittest.TestCase):

    def test_can_generate_and_assign_to_rooms(self):
        rooms = alloc.generate_rooms('office')
        self.assertEquals(len(rooms), 10)
        Amity.add_rooms(rooms)
        self.assertIsInstance(rooms[randint(0, 9)], Office)
        rooms = alloc.generate_rooms('living space')
        self.assertEquals(len(rooms), 10)
        Amity.add_rooms(rooms)
        self.assertIsInstance(rooms[randint(0, 9)], LivingSpace)
        self.assertEqual(Amity.room_count, 20)

        # test that file can be parsed
        PeopleFileParser.line_to_person(file_path)
        person_name = 'ANDREW PHILLIPS'
        Manager.assign_to_room(person_name, 'Room 1')
        Manager.assign_to_room(person_name, 'Room 10')
        person = Amity.find_person(person_name)
        self.assertEquals(person.office.name, 'Room 1')
        self.assertIn(person, Amity.find_room('Room 1').occupants)

        # test that manager can make allocations
        Manager.allocate()
        self.assertEquals([], Manager.get_list_of_unallocated_people())

    def test_can_raise_exception(self):
        names = ['Damian', 'Rick', 'Charles',
                 'William', 'Brad', 'Wilson', 'Damian']

        persons = [Person(name).make_person('Fellow', True) for name in names]

        def assign_all(room_name):
            for person in persons:
                Manager.assign_to_room(person, room_name)

        #raise Exception(Amity.room_collection)
        self.assertRaises(OutOfOfficeException,
                          assign_all, 'Room 1')
        self.assertRaises(OutOfLivingSpaceException,
                          assign_all, 'Room 11')



class PeopleFileParserTestCase(unittest.TestCase):

    def test_can_parse_people_from_file(self):
        persons = PeopleFileParser.line_to_person(file_path)
        self.assertEquals(len(persons), 5)
        self.assertIsInstance(persons[randint(0, 4)], Person)


class AllocationWriterTestCase(unittest.TestCase):

    def test_can_write_allocation_to_stdio(self):
        AllocationWriter.write_allocation(print_stdio=True)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run test in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertIn('Room 1 (OFFICE)', output)

    def test_can_write_allocation_to_file(self):
        AllocationWriter.write_allocation(print_file=True)
        self.assertTrue(os.path.isfile(os.getcwd()
                        + '/amity/output/allocation.txt'))


if __name__ == '__main__':
    nose.run()
