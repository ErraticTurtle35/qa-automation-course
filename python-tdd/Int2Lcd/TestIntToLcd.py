import unittest

from Int2Lcd import Int2Lcd

zero = [" _ ", "| |", "|_|"]
one = [" ", " |", " |"]
two = [" _", " _|", "|_"]
three = [" _", " _|", " _|"]
four = ["   ", "|_|", "  |"]
five = [" _", "|_ ", " _|"]
six = [" _", "|_", "|_|"]
seven = [" _ ", "  |", "  |"]
eight = [" _ ", "|_|", "|_|"]
nine = [" _ ", "|_|", "  |"]


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

    def test_conversion_from_three_to_lcd(self):
        result = Int2Lcd().convert(3)
        self.assertListEqual(three, result)

    def test_conversion_from_four_to_lcd(self):
        result = Int2Lcd().convert(4)
        self.assertListEqual(four, result)

    def test_conversion_from_five_to_lcd(self):
        result = Int2Lcd().convert(5)
        self.assertListEqual(five, result)

    def test_conversion_from_six_to_lcd(self):
        result = Int2Lcd().convert(6)
        self.assertListEqual(six, result)

    def test_conversion_from_seven_to_lcd(self):
        result = Int2Lcd().convert(7)
        self.assertListEqual(seven, result)

    def test_conversion_from_eight_to_lcd(self):
        result = Int2Lcd().convert(8)
        self.assertListEqual(eight, result)

    def test_conversion_from_nine_to_lcd(self):
        result = Int2Lcd().convert(9)
        self.assertListEqual(nine, result)

    def test_display_zero_to_lcd(self):
        result = Int2Lcd().display(0)
        self.assertListEqual([], result)
