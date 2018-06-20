from itertools import zip_longest

numbers = {
    0: [" _ ", "| |", "|_|"],
    1: ["   ", "  |", "  |"],
    2: [" _ ", " _|", "|_ "],
    3: [" _ ", " _|", " _|"],
    4: ["   ", "|_|", "  |"],
    5: [" _ ", "|_ ", " _|"],
    6: [" _ ", "|_ ", "|_|"],
    7: [" _ ", "  |", "  |"],
    8: [" _ ", "|_|", "|_|"],
    9: [" _ ", "|_|", "  |"]
}

patterns = {
    0: [" _ ", "| |", "|_|"],
    1: ["   ", "  |", "  |"]
}


class Int2Lcd:
    def display(self, natural_number):
        lcd_numbers = [self.convert(int(number)) for number in str(natural_number)]
        return [" ".join(column) for column in zip_longest(*lcd_numbers)]

    def convert(self, number):
        return numbers[number]

    def convert2(self, number):
        number_pattern = patterns[number]
        if number_pattern[0][0].isspace() and number_pattern[0][1] == "_" and number_pattern[0][2].isspace():
            number_pattern[0] = " " + "".join(["_" for i in range(self.width)]) + " "
        elif number_pattern[0][0].isspace() and number_pattern[0][1].isspace() and number_pattern[0][2].isspace():
            number_pattern[0] = " " + "".join([" " for i in range(self.width)]) + " "

        if number_pattern[1][0] == "|" and number_pattern[1][1].isspace() and number_pattern[1][2] == "|":
            number_pattern[1] = "|" + "".join([" " for i in range(self.width)]) + "|"
        elif number_pattern[1][0].isspace() and number_pattern[1][1].isspace() and number_pattern[1][2] == "|":
            number_pattern[1] = " " + "".join([" " for i in range(self.width)]) + "|"

        if number_pattern[2][0] == "|" and number_pattern[2][1] == "_" and number_pattern[2][2] == "|":
            number_pattern[2] = "|" + "".join(["_" for i in range(self.width)]) + "|"
        elif number_pattern[2][0].isspace() and number_pattern[2][1].isspace() and number_pattern[2][2] == "|":
            number_pattern[2] = " " + "".join([" " for i in range(self.width)]) + "|"
        return number_pattern

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    def __init__(self, width=None, height=None):
        self._width = width
        self._height = height
