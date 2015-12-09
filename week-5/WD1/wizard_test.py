import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard("Merlin", 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike_five_manna(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        opponent = Wizard("opi", 40, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 15)
        self.assertEqual(opponent.hp, 10)

    def test_strike_less_than_five_manna(self):
        wizard = Wizard("Merlin", 40, 9, 4)
        opponent = Wizard("opi", 40, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 4)
        self.assertEqual(opponent.hp, 37)

unittest.main()
