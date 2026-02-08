print("Программа для расчета очереди")

print("Пожалуйста введите имена участников ")
NAME_START = "Александра"
NAME_FINISH = "Левон"
alexandra_found = False
levon_found = False
count = 0

while not levon_found:
    user_name = input("Введите имя: ")

    if alexandra_found and user_name == NAME_START:
        print("Ошибка! Александра уже стоит в очереди")
        continue
    elif user_name == NAME_START:
        alexandra_found = True
        continue
    elif user_name == NAME_FINISH:
        levon_found = True
    elif alexandra_found and not levon_found:
        count += 1

if alexandra_found and levon_found:
    print(f"Между Левоном и Александрой {count} человек")
else:
    print("Ошибка! Александры нет в очереди!")