
try:
    m = int(input("Введите начало диапазона: "))
    n = int(input("Введите конец диапазона: "))
except ValueError:
    print("Ошибка! Введено некорректное значение!")
else:
    if n > m:
        for i in range(m, n + 1):
            print(i)
    else:
        for i in range(m, n - 1, -1):
            print(i)
