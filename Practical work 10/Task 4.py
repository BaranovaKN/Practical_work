print("Кассовый аппарат")

sum_price = 0
DISCOUNT_PERCENTAGE = 0.1

while True:
    try:
        user_price = int(input("Введите цену товара: "))
    except ValueError:
        print("Ошибка! Введены некорректные данные!")
    else:
        if user_price == 0:
            break
        elif user_price < 0:
            print("Ошибка цены!")
            continue
        sum_price += user_price

if sum_price > 1000:
    sum_price *= (1-DISCOUNT_PERCENTAGE)
print(f"Сумма к оплате: {sum_price:.2f}")