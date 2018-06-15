from Int2Lcd import Int2Lcd

if __name__ == "__main__":
    lcd__display = Int2Lcd().display(1234567890)
    [print(column) for column in lcd__display]
    [print(s) for s in Int2Lcd().convert(0)]
    [print(s) for s in Int2Lcd().convert(1)]
    [print(s) for s in Int2Lcd().convert(2)]
    [print(s) for s in Int2Lcd().convert(3)]
    [print(s) for s in Int2Lcd().convert(4)]
    [print(s) for s in Int2Lcd().convert(5)]
    [print(s) for s in Int2Lcd().convert(6)]
    [print(s) for s in Int2Lcd().convert(7)]
    [print(s) for s in Int2Lcd().convert(8)]
    [print(s) for s in Int2Lcd().convert(9)]
