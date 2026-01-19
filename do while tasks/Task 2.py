
print("Произведение")

total_multiply = 1

while True:
    try:
        user_num = float(input("Введите число: "))
    except ValueError:
        print("ОШИБКА! ВВЕДЕНО НЕКОРРЕКТНОЕ ЗНАЧАНИЕ!")
    else:
        if user_num <= 0:
            break
        total_multiply *= user_num

print(f"Произведение всех введеных положительных чисел: {total_multiply:.2f}")
