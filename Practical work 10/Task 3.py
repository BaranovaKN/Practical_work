
print("Рекордсмен")

MAX_NUM = None
FINAL_NUM = 0

while True:
    try:
        user_num = int(input("Введите ваше натуральное число: "))
    except ValueError:
        print("Ошибка! Введены некорректные данные!")
    else:
        if user_num == 0:
            print(f"Введенное вами максимальное число: {MAX_NUM}")
            break
        elif 0 > user_num:
            print("Ошибка! Число отрицательное!")
        elif MAX_NUM == None or user_num > MAX_NUM:
            MAX_NUM = user_num

