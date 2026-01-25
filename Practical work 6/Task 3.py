
print("Пожалуйста вводите положение одной клетки(2 числа) через пробел за раз."
      "\n числа должны находится в пределах шахматной доски 8х8"
      "\n первое число - номер слобца\n второе - номер строки\n")
try:
    square_1 = tuple(map(int, input("Введите положение первой клеки: ").split()))
    square_2 = tuple(map(int, input("Введите положение второй клеки: ").split()))

except ValueError:
    print("\nВведены некорректные значения!")

else:
    CHESSBOARD_SIZE = 8
    FIRST_NUM_CHESSBOARD = 1

    if (FIRST_NUM_CHESSBOARD <= square_1[0] <= CHESSBOARD_SIZE
            and FIRST_NUM_CHESSBOARD <= square_1[1] <= CHESSBOARD_SIZE
            and FIRST_NUM_CHESSBOARD <= square_2[0] <= CHESSBOARD_SIZE
            and FIRST_NUM_CHESSBOARD <= square_2[1] <= CHESSBOARD_SIZE
            and len(square_1) == 2 and len(square_2) == 2):
        print("\nСовпадает ли цвет ваших клеток?")

        if (square_1[0] + square_1[1]) % 2 == (square_2[0] + square_2[1]) % 2:
            print("YES")

        else:
            print("NO")

    else:
        print("Ошибка ввода!")
