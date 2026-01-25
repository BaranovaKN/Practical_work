
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
