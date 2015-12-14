import unittest

from main_menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu("New Game,Load Game,Exit")

    def test_list_menu(self):
        self.assertEqual(self.menu.list_menu(), "1 New Game\n2 Load Game\n3 Exit\n")

unittest.main()
