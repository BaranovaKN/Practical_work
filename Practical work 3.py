
# Задание 1

print("Task 1")

a = 42
b = 3.14159
c = "Hello, Python!"
d = True
e = [1, 2, 3]
f = (4, 5, 6)
g = {"name": "Alice", "age": 30}
h = {7, 8, 9}
i = None

print(f"""a это {type(a)} \nb это {type(b)} \nc это {type(c)} \nd это {type(d)} \n"""
      f"""e это {type(e)} \nf это {type(f)} \ng это {type(g)} \nh это {type(h)} \ni это {type(i)}""")


# Задание 2

# список
my_list = [1, 2, 3]
print(my_list)

my_list[1] = 100
print(my_list)

#кортеж
my_tuple = (1, 2, 3)
print(my_tuple)

try:
    my_tuple[1]=100
except TypeError:
    print("Ошибка! Нельзя изменять значения кортежа")

#строка
my_string = "cat"
print(my_string)

try:
    my_string[0]='b'
except TypeError:
    print("Ошибка! Нельзя изменять символ строки!")

#Задание 3

# try:
#     num1 = input("Введите первое число: ")
#     num1 = int(num1)
#     num2 = int(input("Введите второе число: "))
#     print(num1 + num2)
# except ValueError:
#     print("Ошибка! Введено некорректное значение!")

#Задание 5

shopping_list = ["apple", "milk", "eggs", "tomato"]
shopping_list.append("milk")
print("Длинна списка равна: ",len(shopping_list))

unique_items = set(shopping_list)
print(unique_items)

#Задание 6

# 1. Сбор данных от пользователя
name = input("Ваше имя: ")
age = int(input())
subject_str = input("введите ваши любимые предметы через запятую")

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
print(f"Имя")