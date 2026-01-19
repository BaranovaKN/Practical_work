
print("Пароль")

PASSWORD = "admin"
i = 1

while True:
    user_password = input("Введите пароль: ")
    if user_password == PASSWORD:
        print("Доступ разрешен!")
        break
    elif i > 2:
        print("Вход заблокирован")
        break
    i += 1

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