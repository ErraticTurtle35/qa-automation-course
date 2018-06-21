from itertools import zip_longest

AVAILABLE_LCD_PATTERNS = {
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


class Int2Lcd:
    def display(self, natural_number):
        lcd_numbers = [self.convert(int(number)) for number in str(natural_number)]
        return [" ".join(column) for column in zip_longest(*lcd_numbers)]

    def convert(self, number):
        self.number_pattern = AVAILABLE_LCD_PATTERNS[number].copy()
        self._update_width()
        if self.height > 1:
            new_number_pattern = self._update_height_of_rows()
            return new_number_pattern
        return self.number_pattern

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

    @property
    def number_pattern(self):
        return self._number_pattern

    @number_pattern.setter
    def number_pattern(self, pattern):
        self._number_pattern = pattern

    def _update_width(self):
        self._update_width_of_the_first_row()
        self._update_width_of_the_middle_row()
        self._update_width_of_the_lower_row()

    def _update_width_of_the_lower_row(self):
        if self.number_pattern[2][0] == "|" and self.number_pattern[2][1] == "_" and self.number_pattern[2][2] == "|":
            self.number_pattern[2] = "|" + "".join(["_" for i in range(self.width)]) + "|"
        elif self.number_pattern[2][0].isspace() and self.number_pattern[2][1].isspace() and self.number_pattern[2][
            2] == "|":
            self.number_pattern[2] = " " + "".join([" " for i in range(self.width)]) + "|"
        elif self.number_pattern[2][0] == "|" and self.number_pattern[2][1] == "_" and self.number_pattern[2][
            2].isspace():
            self.number_pattern[2] = "|" + "".join(["_" for i in range(self.width)]) + " "
        elif self.number_pattern[2][0].isspace() and self.number_pattern[2][1] == "_" and self.number_pattern[2][
            2] == "|":
            self.number_pattern[2] = " " + "".join(["_" for i in range(self.width)]) + "|"

    def _update_width_of_the_middle_row(self):
        if self.number_pattern[1][0] == "|" and self.number_pattern[1][1].isspace() and self.number_pattern[1][
            2] == "|":
            self.number_pattern[1] = "|" + "".join([" " for i in range(self.width)]) + "|"
        elif self.number_pattern[1][0].isspace() and self.number_pattern[1][1].isspace() and self.number_pattern[1][
            2] == "|":
            self.number_pattern[1] = " " + "".join([" " for i in range(self.width)]) + "|"
        elif self.number_pattern[1][0].isspace() and self.number_pattern[1][1] == "_" and self.number_pattern[1][
            2] == "|":
            self.number_pattern[1] = " " + "".join(["_" for i in range(self.width)]) + "|"
        elif self.number_pattern[1][0] == "|" and self.number_pattern[1][1] == "_" and self.number_pattern[1][2] == "|":
            self.number_pattern[1] = "|" + "".join(["_" for i in range(self.width)]) + "|"
        elif self.number_pattern[1][0] == "|" and self.number_pattern[1][1] == "_" and self.number_pattern[1][
            2].isspace():
            self.number_pattern[1] = "|" + "".join(["_" for i in range(self.width)]) + " "

    def _update_width_of_the_first_row(self):
        if self.number_pattern[0][0].isspace() and self.number_pattern[0][1] == "_" and self.number_pattern[0][
            2].isspace():
            self.number_pattern[0] = " " + "".join(["_" for i in range(self.width)]) + " "
        elif self.number_pattern[0][0].isspace() and self.number_pattern[0][1].isspace() and self.number_pattern[0][
            2].isspace():
            self.number_pattern[0] = " " + "".join([" " for i in range(self.width)]) + " "

    def _update_height_of_rows(self):
        new_number_pattern = []
        for pattern in self.number_pattern:
            if "|" in pattern:
                for repetition in range(self.height):
                    if repetition != self.height - 1:
                        new_number_pattern.append(pattern.replace("_", " "))
                    else:
                        new_number_pattern.append(pattern)
            else:
                new_number_pattern.append(pattern)
        return new_number_pattern

    def __init__(self, width=None, height=None):
        self._width = width
        self._height = height
        self._number_pattern = None
