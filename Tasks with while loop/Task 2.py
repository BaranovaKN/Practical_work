
print("Последовательность чисел")

number = 7
Total_Number = ""

while number % 7 == 0:
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Ошибка ввода")
    else:
        if number % 7 == 0:
            Total_Number += f"{number} "
else:
    print(f"Числовой ряд: {Total_Number}")