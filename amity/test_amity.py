from building import Amity, Office, Room, LivingSpace
from people import Person, Fellow, Staff, Manager
from random import randint
from tools import PeopleFileParser, AllocationWriter

import alloc
import unittest
import sys
import os.path

file_path = 'amity/data_samples/people.txt'


class aAmityTestCase(unittest.TestCase):

    def setUp(self):
        self.r = Room('Anvil', 'office')
        self.l = Room('Ruby', 'living space')
        self.f = Person('Jack').make_person('fellow')
        self.s = Person('Mark').make_person('staff')

    def test_can_create_office_or_living_space(self):
        self.assertIsInstance(self.r, Office)
        self.assertIsInstance(self.l, LivingSpace)

    def test_can_add_room_to_amity(self):
        Amity.reset_room_count()
        Amity.add_room(self.r)
        Amity.add_room(self.l)
        self.assertEquals(Amity.room_count, 2)

    def test_can_remove_room(self):
        Amity.room_collection
        Amity.remove_room(self.r.name)
        self.assertEquals(Amity.room_count, 1)

    def test_can_create_fellow_or_staff(self):
        self.assertIsInstance(self.f, Fellow)
        self.assertIsInstance(self.s, Staff)


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

        PeopleFileParser.line_to_person(file_path)
        print Amity.room_count
        person_name = 'ANDREW PHILLIPS'
        Manager.assign_to_room('Room 1', person_name)
        Manager.assign_to_room('Room 10', person_name)
        person = Amity.find_person(person_name)
        self.assertEquals(person.office.name, 'Room 1')
        self.assertIn(person, Amity.find_room('Room 1').occupants)

    def test_can_make_allocations(self):
        Manager.allocate()
        self.assertIsNone(Manager.get_list_of_unallocated())


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
        self.assertTrue(os.path.isfile('amity/output/allocation_table.txt'))


if __name__ == '__main__':
    unittest.main(buffer=True)
