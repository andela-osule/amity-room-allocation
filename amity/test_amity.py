from building import Amity, Office, Room, LivingSpace
from people import Person, Fellow, Staff
from alloc import generate_rooms
from random import randint
from tools import PeopleFileParser

import unittest


class AmityTestCase(unittest.TestCase):

    def setUp(self):
        self.r = Room('Anvil', 'office')
        self.l = Room('Ruby', 'living space')
        self.f = Person('Jack').make_person('fellow')
        self.s = Person('Mark').make_person('staff')
        self.amity = Amity

    def test_can_create_office_or_living_space(self):
        self.assertIsInstance(self.r, Office)
        self.assertIsInstance(self.l, LivingSpace)

    def test_can_add_room_to_amity(self):
        self.amity.add_room(self.r)
        self.amity.add_room(self.l)
        self.assertEquals(self.amity.room_count, 2)

    def test_can_remove_room(self):
        self.amity.remove_room(self.r.name)
        self.assertEquals(self.amity.room_count, 1)

    def test_can_create_fellow_or_staff(self):
        self.assertIsInstance(self.f, Fellow)
        self.assertIsInstance(self.s, Staff)


class AllocTestCase(unittest.TestCase):

    def test_can_generate_offices(self):
        rooms = generate_rooms('office')
        self.assertEquals(10, len(rooms))
        self.assertIsInstance(rooms[randint(0, 9)], Office)

    def test_can_generate_living_spaces(self):
        rooms = generate_rooms('living space')
        self.assertEquals(10, len(rooms))
        self.assertIsInstance(rooms[randint(0, 9)], LivingSpace)


class PeopleFileParserTestCase(unittest.TestCase):

    def test_can_parse_people_from_file(self):
        file_path = 'amity/data_samples/people.txt'
        persons = PeopleFileParser.line_to_person(file_path)
        self.assertEquals(len(persons), 5)
        self.assertIsInstance(persons[randint(0, 4)], Person)


if __name__ == '__main__':
    unittest.main()
