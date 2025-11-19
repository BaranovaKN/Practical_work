
import math

# Задание 1

x = float(input("Введите число x: ")) #берем пременную float так как нужны действительнные числа
print("сумма из числа x округленного в болььшую и меньшую сторону равняется: ", math.ceil(x)+math.floor(x))

# Задание 2
def calculate_distance(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
x_1, y_1 = map(float, input("Введите кординаты для первой точки через пробел: ").split())
x_2, y_2 = map(float, input("Введите кординаты для второй точки через пробел: ").split())

distance = calculate_distance(x_1, y_1, x_2, y_2)

print(f"длинна отрезка с начальной точкой ({x_1};{y_1}) и конечной точкой ({x_2};{y_2}) равна {distance:.2f}")

# Задание 3

num = int(input("Введите четырехзначное число: "))

num_thousand = num//1000
num_hundred = (num-num_thousand*1000)//100
num_tens = (num-num_thousand*1000-num_hundred*100)//10
num_units = num-num_thousand*1000-num_hundred*100-num_tens*10

print(f"Цифра в позиции тысяч равна {num_thousand} "
      f"\nЦифра в позиции сотен равна {num_hundred} "
      f"\nЦифра в позиции десятков равна {num_tens} "
      f"\nЦифра в позиции единиц равна {num_units} ")

# Задание 4

students = int(input("введите количество студентов: "))
mandarin = int(input("введите количество мандаринов: "))

mandarin_for_student = mandarin//students
mandarin_rest = mandarin%students

print(f"студенты получили по {mandarin_for_student} мандаринов в руки, а в корзине осталось {mandarin_rest}")

# Задание 5

time = int(input("введите количество минут: "))
print(f"{time} мин - это {time//60} час {time%60} минут")

# Задание 6

x = int(input("Введите x: "))
x = math.radians(x)
result = math.sin(x)+math.cos(x)+math.tan(x)**2

print("результат вычиления функции: ", result)

# Задание 7

num_seat = int(input("введите номер места: "))
place_in_coupe = 4

num_coupe = math.ceil(num_seat/place_in_coupe)

print(f"при номере места {num_seat} пассажир будет в {num_coupe} купе")