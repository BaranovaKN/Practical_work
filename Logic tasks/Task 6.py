
try:
    n = int(input("Введите любое положительное число: "))
except ValueError:
    print("\nОшибка! Введено некорректное значение!")
else:
    if n > 0:

        # Мы можем представить n как количество чисел
        # Для решения мы должны убрать ту часть, что делятся 2, 3, 5
        # При этом некоторые числа будут убраны дважды это те что делятся на 6, 10, 15 и их необходимо вернуть
        # Это числа что делятся на два из трех чисел диапазона
        # При этом необходимо убрать снова те числа что были добавлены несколько раз, это те числа что делятся на 30
        # Это числа что делятся одновременно на все заданные делители одновременно

        EXCLUDED_DIVISOR_1 = 2
        EXCLUDED_DIVISOR_2 = 3
        EXCLUDED_DIVISOR_3 = 5

        result = (n - n // EXCLUDED_DIVISOR_1 - n // EXCLUDED_DIVISOR_2 - n // EXCLUDED_DIVISOR_3
                  + n // (EXCLUDED_DIVISOR_1 * EXCLUDED_DIVISOR_2) + n // (EXCLUDED_DIVISOR_1 * EXCLUDED_DIVISOR_3)
                  + n // (EXCLUDED_DIVISOR_2 * EXCLUDED_DIVISOR_3)
                  - n // (EXCLUDED_DIVISOR_1 * EXCLUDED_DIVISOR_2 * EXCLUDED_DIVISOR_3))
        print("\nКоличество целых положительных чисел не превышающих n, которые не делятся "
              f"на {EXCLUDED_DIVISOR_1}, {EXCLUDED_DIVISOR_2} и {EXCLUDED_DIVISOR_3} - это {result} числа")
    else:
        print("\nОшибка! Введено число меньшее или равное нулю")
