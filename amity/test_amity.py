from building import Amity, Office, Room, LivingSpace
import unittest


class AmityTestCase(unittest.TestCase):

    def test_can_create_office_or_living_space(self):
        r = Room('Anvil', 'office')
        self.assertIsInstance(r, Office)
        l = Room('Ruby', 'living space')
        self.assertIsInstance(l, LivingSpace)


if __name__ == '__main__':
    unittest.main()
