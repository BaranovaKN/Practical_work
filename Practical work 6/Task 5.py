
print("Пожалуйста вводите положение одной клетки(2 числа) через пробел за раз."
      "\n числа должны находится в пределах шахматной доски 8х8"
      "\n первое число - номер слобца\n второе - номер строки\n")
try:
    square_start = tuple(map(int, input("Введите начальное положениие ферзя: ").split()))
    square_finish = tuple(map(int, input("Введите конечное положение ферзя: ").split()))

except ValueError:
    print("Введены некорректные значения!")

else:
    CHESSBOARD_SIZE = 8
    FIRST_NUM_CHESSBOARD = 1

    if (FIRST_NUM_CHESSBOARD <= square_start[0] <= CHESSBOARD_SIZE
            and FIRST_NUM_CHESSBOARD <= square_start[1] <= CHESSBOARD_SIZE
            and FIRST_NUM_CHESSBOARD <= square_finish[0] <= CHESSBOARD_SIZE
            and FIRST_NUM_CHESSBOARD <= square_finish[1] <= CHESSBOARD_SIZE
            and len(square_start) == 2 and len(square_finish) == 2):
        print("\nМожет ли ферзь сходить на заданную вами клетку за один ход? ")

        if (abs(square_start[0] - square_finish[0]) == abs(square_start[1] - square_finish[1])
                or square_start[0] == square_finish[0] or square_start[1] == square_finish[1]):
            print("YES")

        else:
            print("NO")

    else:
        print("\nОшибка ввода!")


