
def fuel_consumption_calculation(distance, fuel_consumption_per_100_km):

    """
    Вычисляет количество топлива которое понадобится в дороге и его цену.

    Args:
        distance (float): Расстояние, которое планируется проехать.
        fuel_consumption_per_100_km (float): Расход топлива за 100 км.

    Returns:
        float: Количество топлива которое необходимо для преодоления пути и цена этого топлива
    """

    FUEL_PRICE = 49.5
    amount_fuel = (distance/100)* fuel_consumption_per_100_km
    total_fuel_price = amount_fuel * FUEL_PRICE
    return amount_fuel, total_fuel_price

distance = float(input("Введите расстояние, которое планируете проехать на машине: "))
fuel_consumption_per_100_km = float(input("Введите расход топлива в вашей машине на 100 км в литрах: "))

amount_fuel, total_fuel_price = fuel_consumption_calculation(distance, fuel_consumption_per_100_km)

print(f"Для такой поездки понадобится - {amount_fuel:.2f} л топлива и это будет стоить - {total_fuel_price:.2f} руб.")
