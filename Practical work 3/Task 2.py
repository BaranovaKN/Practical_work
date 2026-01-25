
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
