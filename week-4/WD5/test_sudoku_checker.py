import sudoku_checker
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_complete_too_long(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too long.")

    def test_is_complete_basic_order(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = True
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The basic order of 1-9 is correct.")

unittest.main()
