import unittest

from Int2Lcd import Int2Lcd

zero = [" _ ", "| |", "|_|"]


class TestInt2Lcd(unittest.TestCase):
    def test_conversion_from_zero_to_lcd(self):
        result = Int2Lcd().convert(0)
        self.assertListEqual(zero, result)