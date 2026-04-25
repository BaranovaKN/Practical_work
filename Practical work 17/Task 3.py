import math

def is_prime(user_num):
    if user_num < 2:
        return False
    for i in range(2, int(math.sqrt(user_num)) + 1):
        if user_num % i == 0:
            return False
    return True

def get_next_prime(user_num):
    user_num +=1
    if not is_prime(user_num):
        while not is_prime(user_num):
            user_num += 1
    return user_num

while True:
    try:
        user_num = int(input('Введите число для нахождения следующего простого числа после вашего: '))
    except ValueError:
        print('ОШИБКА! ВВЕДЕНО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
    else:
        break

print(f'Следующее простое число после вашего: {get_next_prime(user_num)}')