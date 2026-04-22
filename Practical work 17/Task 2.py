import math

def is_prime(user_num):
    if user_num < 2:
        return False
    for i in range(2, int(math.sqrt(user_num)) + 1):
        if user_num % i == 0:
            return False
    return True

while True:
    try:
        user_num = int(input('Введите число для проверки: '))
    except ValueError:
        print('ОШИБКА! ВВЕДЕНО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
    else:
        if user_num > 0:
            break
        print('Число должно быть положительным!')

print(f'Ваше число простое?: {is_prime(user_num)}')
