
print("Строго возрастающая последовательность")

user_nums = [None, None, None]
user_num1 = None
user_num2 = None
user_num3 = None
i = 1
while True:
    try:
        user_num = int(input(f"Введите {i} число: "))
    except ValueError:
        print("Ошибка! Введены некорректные данные!")
    else:
        if user_num1 == None:
            user_num1 = user_num
            i += 1
            continue
        elif user_num2 == None and user_num > user_num1:
            user_num2 = user_num
            i += 1
            continue
        elif user_num3 == None and user_num2 != None and user_num > user_num2:
            user_num3 = user_num
            print("Последовательнсоть принята")
            break
        print(f"Ошибка! {i} число больше или равно {i-1}")
print(f"Ваша возрастающая последовательность {user_num1}, {user_num2}, {user_num3}")
