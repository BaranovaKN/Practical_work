
print("Кодовый замок")
CORRECT_PIN_CODE = 4590

while True:
    try:
        user_pin_code = int(input("Введите ваш пин-код: "))
    except ValueError:
        print("Ошибка! Введены некорректные данные!")
    else:
        if user_pin_code == CORRECT_PIN_CODE:
            print("Доступ разрешен")
            break
        print("Ошибка. Попробуйте еще раз")