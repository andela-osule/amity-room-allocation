from building import Amity, Office, Room, LivingSpace
import unittest


class AmityTestCase(unittest.TestCase):

    def setUp(self):
        self.r = Room('Anvil', 'office')
        self.l = Room('Ruby', 'living space')
        self.amity = Amity

    def test_can_create_office_or_living_space(self):
        self.assertIsInstance(self.r, Office)
        self.assertIsInstance(self.l, LivingSpace)

    def test_can_add_room_to_amity(self):
        self.amity.add_room([self.r, self.l])
        self.assertEquals(self.amity.room_count, 2)

if __name__ == '__main__':
    unittest.main()
