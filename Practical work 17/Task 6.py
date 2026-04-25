import math

def solve(a, b, c):
    d = math.sqrt(math.pow(b,2) - 4*a*c)

    if (-b+d)/(2*a) > (-b-d)/(2*a):
        return (-b+d)/(2*a), (-b-d)/(2*a)
    else:
        return (-b-d)/(2*a), (-b+d)/(2*a)

while True:
    try:
        user_a, user_b, user_c = map(int, input('Введите ваши коэффициенты для квадратного '
                                                'уравнения через запятую по порядку: ').split(', '))
    except ValueError:
        print('Ошибка!Введены некорректные значения!')
    else:
        if (math.pow(user_b,2) - 4*user_a*user_c) < 0:
            print('Ошибка в вашем квадратном уравнении нет корней!')
        else:
            break

print('Корни вашего квадратного уравнения:', *solve(user_a,user_b,user_c))