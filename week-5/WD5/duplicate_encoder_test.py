import unittest

from duplicate_encoder import CodeWars

class TestIntro(unittest.TestCase):
    def setUp(self):
        self.word1 = CodeWars("din")
        self.word2 = CodeWars("recede")
        self.word3 = CodeWars("Succes")

    def test_without_repeat(self):
        self.assertEqual(self.word1.change_characters(), "(((")

unittest.main()
