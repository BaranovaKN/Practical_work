
B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100

amount_money = int(input("Введите количество денег которое хотите снять(кратно 100): "))

number_b5000 = amount_money//5000
rest_money = amount_money%5000
number_b2000 = rest_money//2000
rest_money = rest_money%2000
number_b1000 = rest_money//1000
rest_money = rest_money%1000
number_b500 = rest_money//500
rest_money = rest_money%500
number_b200 = rest_money//200
rest_money = rest_money%200
number_b100 = rest_money//100

print(f"Если вы снимете - {amount_money} руб. вы получите купюр: "
      f"\nкупюр по 5000 - {number_b5000}\nкупюр по 2000 - {number_b2000}\nкупюр по 1000 -{number_b1000}"
      f"\nкупюр по 500 - {number_b500}\nкупюр по 200 - {number_b200}\nкупюр по 100 - {number_b100}")