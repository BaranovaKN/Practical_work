def is_password_good(password):
    if len(password) > 8 and not password.islower() and not password.isupper() and password.isalnum():
        return True
    else:
        return False

user_password = input('Введите пароль для проверки: ')
print(f'Надежен ли ваш пароль?: {is_password_good(user_password)}')
