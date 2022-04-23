def hello():
    print('-----------------')
    print('     Привет!     ')
    print('    Сыграем?     ')
    print(' Введи два числа ')
    print('x - номер строки ')
    print('y - номер столбца')
    print('-----------------')
hello()

field = [
   [' ', ' ', ' '],
   [' ', ' ', ' '],
   [' ', ' ', ' ']
]
field

def show():
    print(f'   0 1 2')
    print(f'0{field[0][0]} {field[0][1]} {field[0][2]}')
    print(f'1{field[1][0]} {field[1][1]} {field[1][2]}')
    print(f'2{field[2][0]} {field[2][1]} {field[2][2]}')
show()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        x, y = map(int, input().split())

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Выход за пределы")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y


ask()

def win_check():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


hello()
field = [
   [' ', ' ', ' '],
   [' ', ' ', ' '],
   [' ', ' ', ' ']
]
field
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_check():
        break

    if count == 9:
        print(" Ничья!")
        break