
n = int(input("Введите натуральное число, которое больше или равно 2: "))
max1 = 0
max2 = 0

for i in range(n):
    num =  int(input("Введите натуральное число: "))
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
print(f"Максимальное число {max1} и следующее число после него {max2}")