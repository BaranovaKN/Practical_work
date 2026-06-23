user_num = int(input('Введите ваше число: '))
count_3 = 0
count_last_num = 0
count_even_num = 0
sum_num_more_5 = 0
multiply_more_7 = 1
count_0_and_5 = 0

last_num = current_num = user_num % 10
remainder_num = user_num // 10

while remainder_num > 0:
    if current_num == 3:
        count_3 += 1

    if current_num == last_num:
        count_last_num += 1

    if current_num % 2 == 0 and current_num != 0:
        count_even_num += 1

    if current_num > 5:
        sum_num_more_5 += current_num

    if current_num > 7:
        multiply_more_7 *= current_num

    if current_num == 0 or current_num == 5:
        count_0_and_5 += 1

    current_num = remainder_num % 10
    remainder_num = remainder_num // 10

print(f'В Вашем числе:\nКоличество 3: {count_3}\nПоследнее число встречается: {count_last_num} раз\n'
      f'Количество четных чисел: {count_even_num}\nСумма чисел больше 5: {sum_num_more_5}\n'
      f'Произведение чисел больше 7: {multiply_more_7}\nКоличество 5 и 0: {count_0_and_5}')