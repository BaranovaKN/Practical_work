
print("Ведьмаку заплатите чеканной монетой")

COIN_DENOMINATIONS = [25, 10, 5, 1]

try:
    price_of_work = int(input("Введите цену за услуги ведьмака: "))
except ValueError:
    print("Ошибка! Введено некорректное значение")
else:
    coin_count = 0
    i = 0
    while i < len(COIN_DENOMINATIONS):
        if price_of_work >= COIN_DENOMINATIONS[i]:
            price_of_work -= COIN_DENOMINATIONS[i]
            coin_count += 1
        else:
            i += 1
    print(f"Необходимо {coin_count} чеканных монет")