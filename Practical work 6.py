
# Задание 1

try:
    temperature = float(input("Пожалуйста введите вашу температуру: "))
    pressure = int(input("Пожалуйста введите ваше давление: "))
    pulse = int(input("Пожалуйста введите ваш пульс: "))

except ValueError:
    print("\nВведены некорректные значения!")

else:
    NORMAL_TEMPERATURE_MIN = 36
    NORMAL_TEMPERATURE_MAX = 37
    MIDDLE_DEVIATION_TEMPERATURE_MIN = 35
    MIDDLE_DEVIATION_TEMPERATURE_MAX = 38
    NORMAL_PRESSURE_MIN = 110
    NORMAL_PRESSURE_MAX = 130
    MIDDLE_DEVIATION_PRESSURE_MIN = 105
    MIDDLE_DEVIATION_PRESSURE_MAX = 140
    NORMAL_PULSE_MIN = 60
    NORMAL_PULSE_MAX = 100
    MIDDLE_DEVIATION_PULSE_MIN = 55
    MIDDLE_DEVIATION_PULSE_MAX = 110

    print("\nВаше состояние здоровья на основе данных ответов: ")

    if (NORMAL_TEMPERATURE_MIN <= temperature <= NORMAL_TEMPERATURE_MAX
            and NORMAL_PRESSURE_MIN <= pressure <= NORMAL_PRESSURE_MAX
            and NORMAL_PULSE_MIN <= pulse <= NORMAL_PULSE_MAX):

        # условие if можно перенести на следущую строку если оно в скобках это позволяет:
        # 1. укоротить код
        # 2. сделать его визуально понятнее
        # благодаря этому в моей работе можно рассмотреть с удобством в каком диапозоне переменные

        print("Вы находитесь в нормальном состоянии")

    elif (temperature < MIDDLE_DEVIATION_TEMPERATURE_MIN or temperature > MIDDLE_DEVIATION_TEMPERATURE_MAX
          or pressure <  MIDDLE_DEVIATION_PRESSURE_MIN or pressure >  MIDDLE_DEVIATION_PRESSURE_MAX
          or pulse < MIDDLE_DEVIATION_PULSE_MIN or pulse > MIDDLE_DEVIATION_PULSE_MAX):
        print("Ваше состояние плохое. Необходим вызов врача!")

    else:
        print("У вас легкое недомогание")

# Задание 2
try:
    num = int(input("Введите пожалуйста число от 1 до 36: "))

except ValueError:
    print("\nВведены некорректные значения!")

else:
    POCKET_ZERO = 0
    LAST_NUMBER_POCKET_RANGE_1 = 10
    LAST_NUMBER_POCKET_RANGE_2 = 18
    LAST_NUMBER_POCKET_RANGE_3 = 28
    LAST_NUMBER_POCKET_RANGE_4 = 36

    if 0 <= num <=36:
        print("\nВам Выпал:")

        if num == POCKET_ZERO:
            print("Выпал зеленый карман")

        elif ((POCKET_ZERO <= num <= LAST_NUMBER_POCKET_RANGE_1
               or LAST_NUMBER_POCKET_RANGE_2  < num <= LAST_NUMBER_POCKET_RANGE_3 and num % 2 == 0)
               or (LAST_NUMBER_POCKET_RANGE_1 < num < LAST_NUMBER_POCKET_RANGE_3
               or LAST_NUMBER_POCKET_RANGE_3 < num <= LAST_NUMBER_POCKET_RANGE_4 and num % 2 == 1)):
            print("Выпал черный карман")

        else:
            print("Выпал красный карман")

    else:
        print("\nОшибка! Вы ввели число вне диапозона!")

# Задание 3

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

# Задание 4

print("Пожалуйста вводите положение одной клетки(2 числа) через пробел за раз."
      "\n числа должны находится в пределах шахматной доски 8х8"
      "\n первое число - номер слобца\n второе - номер строки\n")
try:
    square_start = tuple(map(int, input("Введите начальное положениие слона: ").split()))
    square_finish = tuple(map(int, input("Введите конечное положение слона: ").split()))

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
        print("\nМожет ли слон сходить на заданную вами клетку за один ход? ")

        if abs(square_start[0] - square_finish[0]) == abs(square_start[1] - square_finish[1]):
            print("YES")

        else:
            print("NO")

    else:
        print("\nОшибка ввода!")

# Задание 5

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


