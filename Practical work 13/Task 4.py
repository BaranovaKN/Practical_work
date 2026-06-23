user_ip = input("Введите ваш IP: ").split('.')
if len(user_ip) != 4:
    print("Нет")
else:
    valid = True
    for i in user_ip:
        if not i.isdigit():
            valid = False
            break
        elif int(i) < 0 or int(i) > 255:
            valid = False
            break
    if valid:
        print("Да")
    else:
        print("Нет")