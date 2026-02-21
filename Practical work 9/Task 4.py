print("Все вместе")

try:
    num = int(input("Введите натуральное число: "))
except ValueError:
    print("Ошибка! Введено некорректное значение")
else:
    if num > 0:
        count_3= 0
        count_last_num = 0
        count_even_num = 0
        sum_num_more_than_5 = 0
        multiply_num_more_than_7 = 1
        count_0_and_5 = 0
        last_num = num%10
        while num > 0:
            digit = num % 10
            if digit == 3:
                count_3 +=1
            if digit == last_num:
                count_last_num += 1
            if digit % 2 == 0:
                count_even_num += 1
            if digit > 5:
                sum_num_more_than_5 += digit
            if digit > 7:
                multiply_num_more_than_7 *= digit
            if digit == 0 or digit == 5:
                count_0_and_5 += 1
            num //= 10
        print(f"В вашем числе:\nЧисло 3 встречается {count_3} раз\nПоследнее число {last_num} встречается {count_last_num} раз\n"
              f"Честные числа встречаются {count_even_num} раз\nСумма чисел больше 5 равна {sum_num_more_than_5}\n"
              f"Произведение чисел больше 7 равно {multiply_num_more_than_7}\nЧисла 0 и 5 встречаются {count_0_and_5} раз")
    else:
        print("Ошибка! Введено не натуральное число")