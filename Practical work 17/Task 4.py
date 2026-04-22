def is_password_good(password):
    if len(password) > 8 and not password.islower() and not password.isupper() and password.isalnum():
        return True
    else:
        return False

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
