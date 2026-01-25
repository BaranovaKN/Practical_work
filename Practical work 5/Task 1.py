
annual_income = float(input("Введите свой годовой доход: "))
TAX_RATE = 0.13

if annual_income >= 0:
    tax_amount = annual_income * TAX_RATE
    income_after_tax = annual_income - tax_amount

    print(f"\nВаша общая сумма дохода - {annual_income:,.2f} руб. \nСумма вашего налога - {tax_amount:,.2f} руб. "
          f"\nВаш доход после уплаты налогов - {income_after_tax:,.2f} руб.")

else:
    print("\nОшибка! Доход должен быть больше или равен 0")
