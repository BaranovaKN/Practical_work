import math

def is_prime(user_num):
    if user_num < 2:
        return False
    for i in range(2, int(math.sqrt(user_num)) + 1):
        if user_num % i == 0:
            return False
    return True

def is_valid_password(user_password):
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

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
