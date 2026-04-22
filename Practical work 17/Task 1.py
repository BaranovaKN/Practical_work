def get_days(user_month):
    match user_month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28

while True:
    try:
        user_month = int(input('Введите ваш месяц: '))
    except ValueError:
        print('ОШИБКА! ВВЕДЕНО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
    else:
        if 13 > user_month > 0:
            break
        else:
            print('Месяцев всего 12!')

print(f'В {user_month} месяце: {get_days(user_month)} дней')

def get_days(user_month):
    match user_month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28

while True:
    try:
        user_month = int(input('Введите ваш месяц: '))
    except ValueError:
        print('ОШИБКА! ВВЕДЕНО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
    else:
        if 13 > user_month > 0:
            break
        else:
            print('Месяцев всего 12!')

print(f'В {user_month} месяце: {get_days(user_month)} дней')
