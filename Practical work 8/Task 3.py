
import math
try:
    n = int(input("Введите число: "))
except ValueError:
    print("Ошибка! Введено некорректное значение!")
else:
    res = 0

    for i in range(n+1):
        if i % 2 == 0:
            res -= i
        else:
            res += i

    res+=math.pow(-1, n+1)*n
    print(res)