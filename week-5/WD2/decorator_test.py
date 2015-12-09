import unittest
from decorator import Rusty

class RustyTest(unittest.TestCase):
    def test_rusty_effect(self):
        weapon = Rusty(TestWeapon())
        self.assertEqual(weapon.damage(), 5)
        self.assertEqual(Rusty(TestMace()).damage(), 15)

class TestWeapon:
    def damage(self):
        return 10

class TestMace:
    def damage(self):
        return 30

if __name__ == "__main__":
    unittest.main()
