numbers = {
    0: [" _ ", "| |", "|_|"],
    1: [" ", " |", " |"],
    2: [" _", " _|", "|_"],
    3: [" _", " _|", " _|"],
    4: ["   ", "|_|", "  |"],
    5: [" _", "|_ ", " _|"],
    6: [" _", "|_", "|_|"],
    7: [" _ ", "  |", "  |"],
    8: [" _ ", "|_|", "|_|"],
    9: [" _ ", "|_|", "  |"]
}


class Int2Lcd:
    def convert(self, number):
        return numbers[number]
