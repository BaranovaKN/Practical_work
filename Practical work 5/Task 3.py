
def convert_usd_to_rub(amount_usd):
    """
    Конвертирует сумму в долларах в рубли.

    Args:
         amount_usd (int): сумма в долларах.

    Returns:
        float: сумму в рублях.
    """
    USD_TO_RUB = 95.50
    return USD_TO_RUB * amount_usd

amount_usd = int(input("введите сумму в долларах: "))
amount_rub = convert_usd_to_rub(amount_usd)
print(f"Ваша сумма в долларах равна - {amount_rub} руб.")