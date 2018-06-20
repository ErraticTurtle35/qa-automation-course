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

    [print(s) for s in Int2Lcd(width=9, height=1).convert2(0)]
    [print(s) for s in Int2Lcd(width=8, height=1).convert2(1)]
    [print(s) for s in Int2Lcd(width=7, height=1).convert2(2)]
    [print(s) for s in Int2Lcd(width=6, height=1).convert2(3)]
    [print(s) for s in Int2Lcd(width=5, height=1).convert2(4)]
    [print(s) for s in Int2Lcd(width=4, height=1).convert2(5)]
    [print(s) for s in Int2Lcd(width=3, height=1).convert2(6)]
    [print(s) for s in Int2Lcd(width=2, height=1).convert2(7)]
    [print(s) for s in Int2Lcd(width=1, height=1).convert2(8)]
    [print(s) for s in Int2Lcd(width=11, height=1).convert2(9)]