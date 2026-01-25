
import math

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
