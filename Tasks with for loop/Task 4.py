
try:
    m, n = map(int, input("Введите два числа начало и конец диапазона: ").split())
except ValueError:
    print("Ошибка! Введено некорректное значение!")
else:
    if n < m:
        print("Первое число должно быть больше или равно второму")
    else:
        for i in range(m, n + 1):
            if i % 17 == 0 or i % 15 == 0 or i % 10 == 9:
                print(i)
