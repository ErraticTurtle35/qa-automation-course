import unittest

from Int2Lcd import Int2Lcd

zero = [" _ ", "| |", "|_|"]
one = [" ", " |", " |"]
two = [" _", " _|", "|_"]


class TestInt2Lcd(unittest.TestCase):
    def test_conversion_from_zero_to_lcd(self):
        result = Int2Lcd().convert(0)
        self.assertListEqual(zero, result)

    def test_conversion_from_one_to_lcd(self):
        result = Int2Lcd().convert(1)
        self.assertListEqual(one, result)

    def test_conversion_from_two_to_lcd(self):
        result = Int2Lcd().convert(2)
        self.assertListEqual(two, result)
