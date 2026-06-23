DAYS_IN_YEAR = 365
DAYS_IN_MONTH_1 = 28
DAYS_IN_MONTH_2 = 30
DAYS_IN_MONTH_3 = 31

print('возможное количество месяцев с разным количеством дней в году\n')

for n in range(DAYS_IN_YEAR // DAYS_IN_MONTH_1 + 1):
    for k in range(DAYS_IN_YEAR // DAYS_IN_MONTH_2 + 1):
        for m in range(DAYS_IN_YEAR // DAYS_IN_MONTH_3 + 1):
            if DAYS_IN_MONTH_1*n + DAYS_IN_MONTH_2 * k + DAYS_IN_MONTH_3 * m == 365:
                print(f'Год состоящий из: {n} месяцев стоящих из {DAYS_IN_MONTH_1} дней,'
                      f'{k} месяцев стоящих из {DAYS_IN_MONTH_2} дней и {m} месяцев стоящих из {DAYS_IN_MONTH_3} дня')
                break