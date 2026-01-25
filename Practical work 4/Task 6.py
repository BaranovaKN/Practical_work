
import math

x = int(input("Введите x: "))
x = math.radians(x)
result = math.sin(x)+math.cos(x)+math.tan(x)**2

print("результат вычиления функции: ", result)