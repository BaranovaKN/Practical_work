
# 1. Сбор данных от пользователя
name = input("Ваше имя: ")
age = int(input("Ввш возрвст: "))
subject_str = input("введите ваши любимые предметы через запятую: ")

# 2. Преобразование subject_str в subject_list
subject_list = [subject_str.strip() for subject_str in subject_str.split(",")]

# 3. Создание словаря
student = {
    "Имя":name,
    "Возраст":age,
    "Список любимых предметов":subject_list
}

# 4. Красивый вывод анкеты
print("="*40)
print("АНКЕТА СТУДЕНТА")
print("="*40)
print(f"Имя: {student["Имя"]} \nВозраст: {student["Возраст"]}"
      f"\nЛюбимые предметы: {student["Список любимых предметов"]}")
print("="*40)