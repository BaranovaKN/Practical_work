user_list = list(map(int, input('Введите ваши числа через пробел: ').split()))
count = 0
for i in range(len(user_list)):
    for j in range(i+1, len(user_list)):
        if i == j:
            continue
        if user_list[i] == user_list[j]:
            count += 1

print(f'Количество пар чисел в вашем списке: {count}')