
import math
try:
    m = int(input("Введите стартовое количество организмов: "))
    p = int(input("Введите среднесуточное увеличение в процентах: "))
    n = int(input("Введите количество дней для размножения: "))
except ValueError:
    print("Ошибка! Введено некорректное значение!")
else:
    for i in range(1, n+1):
        m = m * (1 + p/100)
        print(f"Популяция в {i} день равна {math.floor(m)}")
