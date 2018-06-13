numbers = {
    0: [" _ ", "| |", "|_|"],
    1: [" ", " |", " |"],
    2: [" _", " _|", "|_"]
}


class Int2Lcd:
    def convert(self, number):
        return numbers[number]
