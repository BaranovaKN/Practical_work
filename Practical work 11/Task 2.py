PRICE_BULL = 10
PRICE_COW = 5
PRICE_CALF = 0.5
AMOUNT_MONEY = 100
count = 0
print(f'На {AMOUNT_MONEY} можно купить:')
for b in range(AMOUNT_MONEY // PRICE_BULL + 1):
    for k in range(AMOUNT_MONEY // PRICE_COW + 1):
        for t in range(AMOUNT_MONEY // PRICE_COW + 1):
            if PRICE_BULL * b + PRICE_COW * k + PRICE_CALF * t == 100 and b + k + t >= 1:
                print(f'{b} быков, {k} коров и {t} телят')
                break

