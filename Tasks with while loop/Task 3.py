
print("Количество отличных оценок ученика")

count_max_user_mark = 0
while(True):

    try:
        user_mark = int(input("Пожалуйста введите оценку от 1 до 5: "))
    except ValueError:
        print("Ошибка! Введено некорректное значение!")
    else:
        MIN_MARK = 1
        MAX_MARK = 5

        if not MIN_MARK <= user_mark <= MAX_MARK:
            print("Ошибка! Введено некорректное значение!")
            break
        elif user_mark == MAX_MARK:
            count_max_user_mark += 1

print(f"У ученика есть {count_max_user_mark} пятерок")

