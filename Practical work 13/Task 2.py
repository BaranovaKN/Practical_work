n = int(input("Введите количество строк: "))
user_list = []
for i in range(1,n+1):
    user_list.extend(input(f"Введите {i} вашу строку из {n}: "))
print('Все символы в вашем списке:\n',*user_list)
