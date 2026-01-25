
import math

def calculate_rectangle_area(width, height):
    """

    Вычисляет площадь прямоугольника.

    Args:
        width (int): Ширина прямоугольника.
        height (int): Высота прямоугольника.

    Returns:
        int: Площадь прямоугольника.
    """
    return width* height

def calculate_circle_area(radius):
    """
    Args:
        radius (int): радиус круга

    Returns:
        float: площадь круга
    """
    return math.pi * radius**2

width, height = map(int, input("Введите ширину и высоту прямоугольника через пробел: ").split())
rectangle_area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника - {rectangle_area}")

radius = int(input("Введите радиус круга: "))
circle_area = calculate_circle_area(radius)
print(f"Площадь круга - {circle_area}")