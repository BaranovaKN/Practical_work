
try:
    num1 = input("Введите первое число: ")
    num1 = int(num1)
    num2 = int(input("Введите второе число: "))
    print(num1 + num2)
except ValueError:
    print("Ошибка! Введено некорректное значение!")

