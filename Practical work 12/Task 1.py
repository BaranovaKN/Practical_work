while True:
    try:
        n = int(input('Введите целое число, которое больше 1, для составления последовательности: '))
    except ValueError:
        print('Ошибка! Введено некорректное число!')
    else:
        if n > 1:
            break
        else:
            print('Ошибка! Число должно быть больше 1')

list_odd_num = list(range(1, n+1, 2))
print(f'Последовательность нечетных чисел от 1 до {n}:\n')
print(*list_odd_num, sep=', ')
