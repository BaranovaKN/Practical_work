import math

# Задание 1

#     annual_income = float(input("Введите свой годовой доход: "))
#     TAX_RATE = 0.13
#
#     if annual_income >= 0:
#         tax_amount = annual_income * TAX_RATE
#         income_after_tax = annual_income - tax_amount
#
#         print(f"\nВаша общая сумма дохода - {annual_income:,.2f} руб. \nСумма вашего налога - {tax_amount:,.2f} руб. "
#               f"\nВаш доход после уплаты налогов - {income_after_tax:,.2f} руб.")

#     else:
#         print("\nОшибка! Доход должен быть больше или равен 0")
# Задание 2
#
#     height, weight = map(float, input("Пожалуйста введите ваш рост(в метрах) "
#                                     "и вес (в кг) в одной строке через пробел: ").split())
#     bmi = weight / (height * height)
#     print(f"\nваш Индекс Массы Тела - {bmi:.1f}")

# Задание 3
#
# def convert_usd_to_rub(amount_usd):
#     """
#     Конвертирует сумму в долларах в рубли.
#
#     Args:
#          amount_usd (int): сумма в долларах.
#
#     Returns:
#         float: сумму в рублях.
#     """
#     USD_TO_RUB = 95.50
#     return USD_TO_RUB * amount_usd
#
# amount_usd = int(input("введите сумму в долларах: "))
# amount_rub = convert_usd_to_rub(amount_usd)
# print(f"Ваша сумма в долларах равна - {amount_rub} руб.")

# Задание 4

# def calculate_rectangle_area(width, height):
#     """
#
#     Вычисляет площадь прямоугольника.
#
#     Args:
#         width (int): Ширина прямоугольника.
#         height (int): Высота прямоугольника.
#
#     Returns:
#         int: Площадь прямоугольника.
#     """
#     return width* height
#
# def calculate_circle_area(radius):
#     """
#     Args:
#         radius (int): радиус круга
#
#     Returns:
#         float: площадь круга
#     """
#     return math.pi * radius**2
#
# width, height = map(int, input("Введите ширину и высоту прямоугольника через пробел: ").split())
# rectangle_area = calculate_rectangle_area(width, height)
# print(f"Площадь прямоугольника - {rectangle_area}")
#
# radius = int(input("Введите радиус круга: "))
# circle_area = calculate_circle_area(radius)
# print(f"Площадь круга - {circle_area}")

# Задание 5
#
# B5000 = 5000
# B2000 = 2000
# B1000 = 1000
# B500 = 500
# B200 = 200
# B100 = 100
#
# amount_money = int(input("Введите количество денег которое хотите снять(кратно 100): "))
#
# number_b5000 = amount_money//5000
# rest_money = amount_money%5000
# number_b2000 = rest_money//2000
# rest_money = rest_money%2000
# number_b1000 = rest_money//1000
# rest_money = rest_money%1000
# number_b500 = rest_money//500
# rest_money = rest_money%500
# number_b200 = rest_money//200
# rest_money = rest_money%200
# number_b100 = rest_money//100
#
# print(f"Если вы снимете - {amount_money} руб. вы получите купюр: "
#       f"\nкупюр по 5000 - {number_b5000}\nкупюр по 2000 - {number_b2000}\nкупюр по 1000 -{number_b1000}"
#       f"\nкупюр по 500 - {number_b500}\nкупюр по 200 - {number_b200}\nкупюр по 100 - {number_b100}")

# Задание 6

def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между двумя точками.

    Args:
        x1, y1 (float): Координаты первой точки.
        x2, y2 (float): Координаты второй точки.

    Returns:
        float: Расстояние между точками.
    """
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по формуле Герона.

    Args:
        a (float): расстояние между A и B.
        b (float): расстояние между B и C.
        b (float): расстояние между A и C.

    Returns:
        float: Расстояние между точками.
    """
    semiperimeter = ( a + b + c) / 2
    triangle_area = math.sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))
    return triangle_area

A_x, A_y = map(float, input("Введите координаты точки А через пробел: ").split())
B_x, B_y = map(float, input("Введите координаты точки B через пробел: ").split())
C_x, C_y = map(float, input("Введите координаты точки C через пробел: ").split())

a = calculate_distance(A_x, A_y, B_x, B_y)
b = calculate_distance(C_x, C_y, B_x, B_y)
c = calculate_distance(A_x, A_y, C_x, C_y)

triangle_area = calculate_triangle_area(a, b, c)

print(f"Площадь треугольника - {triangle_area:.2f}, стороны треугольника - {a:.2f}; {b:.2f}; {c:.2f}")
# Задание 7


