print("Цифровой корень")

try:
    n = int(input("Введите число для вычисления цифрового корня: "))
except ValueError:
    print("ОШИБКА! ВВЕДЕНО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!")
else:
    print(f"Цифровой корень числа {n} равен", end=" ")
    while n > 9:
        res = 0
        while n//10 != 0:
            res += n%10
            n //=10
        res += n
        n = res
    print(n)

