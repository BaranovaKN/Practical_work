numbers = [10, 20, 30, 40, 50]

while True:
    try:
        user_num = int(input('Введите целое число: '))
    except ValueError:
        print('Ошибка! Введено некорректное число!')
    else:
        break

for i in range(len(numbers)):
    if numbers[i] == user_num:
        print('Ваше число есть в списке!')
        break
    if i == len(numbers) - 1:
        print('Нет такого числа')