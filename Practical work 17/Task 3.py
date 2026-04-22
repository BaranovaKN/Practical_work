import math

def is_prime(user_num):
    if user_num < 2:
        return False
    for i in range(2, int(math.sqrt(user_num)) + 1):
        if user_num % i == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))

def get_next_prime(user_num):
    if not is_prime(user_num):
        while not is_prime(user_num):
            user_num += 1
    return user_num

print(get_next_prime(1))
print(get_next_prime(10))
