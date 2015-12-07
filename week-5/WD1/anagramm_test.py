import unittest
from anagramm import is_anagramm

class Test_is_anagramma(unittest.TestCase):
    def test_anagramma(self):
        self.assertEqual(is_anagramm("", ""), True)
        self.assertEqual(is_anagramm("a", ""), False)
        self.assertEqual(is_anagramm("ab", "ba"), True)
        self.assertEqual(is_anagramm("ab", "ba"), True)
        self.assertEqual(is_anagramm("abc", "bac"), True)
        self.assertEqual(is_anagramm("abcdefghij", "cdefghaijb"), True)

unittest.main()
