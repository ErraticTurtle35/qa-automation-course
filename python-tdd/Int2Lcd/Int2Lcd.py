numbers = {
    0: [" _ ", "| |", "|_|"],
    1: [" ", " |", " |"]
}


class Int2Lcd:
    def convert(self, number):
        return numbers[number]
