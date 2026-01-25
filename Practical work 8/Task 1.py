
try:
    n = int(input("Введите число для составления таблицы умножения: "))
except ValueError:
    print("Ошибка! Введено некорректное значение!")
else:
    print(f"Таблица умножения на {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")