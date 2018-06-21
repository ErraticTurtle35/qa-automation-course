import unittest

from Int2Lcd import Int2Lcd

zero = [" _ ", "| |", "|_|"]
one = ["   ", "  |", "  |"]
two = [" _ ", " _|", "|_ "]
three = [" _ ", " _|", " _|"]
four = ["   ", "|_|", "  |"]
five = [" _ ", "|_ ", " _|"]
six = [" _ ", "|_ ", "|_|"]
seven = [" _ ", "  |", "  |"]
eight = [" _ ", "|_|", "|_|"]
nine = [" _ ", "|_|", "  |"]
all_natural_number_in_lcd_format = ['     _   _       _   _   _   _   _   _ ',
                                    '  |  _|  _| |_| |_  |_    | |_| |_| | |',
                                    '  | |_   _|   |  _| |_|   | |_|   | |_|']

all_natural_number_in_lcd_number_list = [['   ', '  |', '  |'], [' _ ', ' _|', '|_ '], [' _ ', ' _|', ' _|'],
                                         ['   ', '|_|', '  |'], [' _ ', '|_ ', ' _|'], [' _ ', '|_ ', '|_|'],
                                         [' _ ', '  |', '  |'], [' _ ', '|_|', '|_|'], [' _ ', '|_|', '  |'],
                                         [' _ ', '| |', '|_|']]


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
        self.assertListEqual(zero, result)

    def test_conversion_from_1234567890_to_lcd_numbers_list(self):
        result = [Int2Lcd().convert(int(number)) for number in str(1234567890)]
        self.assertListEqual(all_natural_number_in_lcd_number_list, result)

    def test_display_1234567890_to_lcd(self):
        result = Int2Lcd().display(1234567890)
        self.assertListEqual(all_natural_number_in_lcd_format, result)

    def test_assignation_of_width_and_height(self):
        int2lcd = Int2Lcd(width=1, height=1)
        self.assertEqual(int2lcd.width, 1)
        self.assertEqual(int2lcd.height, 1)

    def test_conversion_from_zero_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(0)
        self.assertListEqual([" ___ ", "|   |", "|___|"], result)

    def test_conversion_from_one_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(1)
        self.assertListEqual(["     ", "    |", "    |"], result)

    def test_conversion_from_two_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(2)
        self.assertListEqual([" ___ ", " ___|", "|___ "], result)

    def test_conversion_from_three_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(3)
        self.assertListEqual([" ___ ", " ___|", " ___|"], result)

    def test_conversion_from_four_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(4)
        self.assertListEqual(["     ", "|___|", "    |"], result)

    def test_conversion_from_five_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(5)
        self.assertListEqual([" ___ ", "|___ ", " ___|"], result)

    def test_conversion_from_six_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(6)
        self.assertListEqual([" ___ ", "|___ ", "|___|"], result)

    def test_conversion_from_seven_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(7)
        self.assertListEqual([" ___ ", "    |", "    |"], result)

    def test_conversion_from_eight_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(8)
        self.assertListEqual([" ___ ", "|___|", "|___|"], result)

    def test_conversion_from_nine_to_lcd_with_width_3(self):
        int2lcd = Int2Lcd(width=3, height=1)
        result = int2lcd.convert2(9)
        self.assertListEqual([" ___ ", "|___|", "    |"], result)

    def test_conversion_from_zero_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(0)
        self.assertListEqual([' ___ ', '|   |', '|   |', '|   |', '|___|'], result)

    def test_conversion_from_one_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(1)
        self.assertListEqual(['     ', '    |', '    |', '    |', '    |'], result)

    def test_conversion_from_three_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(3)
        self.assertListEqual([" ___ ", "    |", " ___|", "    |", " ___|"], result)

    def test_conversion_from_four_to_lcd_with_height_3(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(4)
        self.assertListEqual(["     ", "|   |", "|___|", "    |", "    |"], result)

    def test_conversion_from_five_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(5)
        self.assertListEqual([" ___ ", "|    ", "|___ ", "    |", " ___|"], result)

    def test_conversion_from_six_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(6)
        self.assertListEqual([" ___ ", "|    ", "|___ ", "|   |", "|___|"], result)

    def test_conversion_from_seven_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(7)
        self.assertListEqual([" ___ ", "    |", "    |", "    |", "    |"], result)

    def test_conversion_from_eight_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(8)
        self.assertListEqual([" ___ ", "|   |", "|___|", "|   |", "|___|"], result)

    def test_conversion_from_nine_to_lcd_with_height_2(self):
        int2lcd = Int2Lcd(width=3, height=2)
        result = int2lcd.convert2(9)
        self.assertListEqual([" ___ ", "|   |", "|___|", "    |", "    |"], result)

    def test_conversion_from_one_to_lcd_with_height_3(self):
        int2lcd = Int2Lcd(width=3, height=3)
        result = int2lcd.convert2(2)
        self.assertListEqual(['     ', '    |', '    |', '    |', '    |'], result)
