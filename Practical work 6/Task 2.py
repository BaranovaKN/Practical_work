
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
        print("\nОшибка! Вы ввели число вне диапазона!")
