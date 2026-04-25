import math

def is_valid_password(user_password):
    def is_prime(user_num):
        if user_num < 2:
            return False
        for i in range(2, int(math.sqrt(user_num)) + 1):
            if user_num % i == 0:
                return False
        return True

    parts_password = user_password.split(':')
    if len(parts_password) != 3:
        return False

    a, b, c = parts_password
    if not a.isdigit() or not b.isdigit() or not c.isdigit():
        return False

    if a != a[::-1]:
        return False

    if not is_prime(int(b)):
        return False

    if int(c) % 2 != 0:
        return False

    return True

user_password = input('Введите ваш пароль: ')
print(f'Подходит ли ваш пароль: {is_valid_password(user_password)}')
