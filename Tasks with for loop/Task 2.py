
import math

print("Вычисление факториала")
try:
    n = int(input("Введите число для вычисления факториала: "))
except ValueError:
    print("Ошибка! Введено некорректное значение!")
else:
    print(f"Факториал введенного числа:{math.factorial(n)}")