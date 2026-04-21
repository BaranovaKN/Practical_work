prices = [1500, 500, 2000, 3500, 1000, 4500]
max_price = max(prices)
min_price = min(prices)
sum_price = sum(prices)
average_price = sum_price / len(prices)

print('Ваш список цен товаров:\n',*prices)
print(f'Самый дорогой товар стоит - {max_price}\n'
      f'Самый дешевый товар стоит - {min_price}\n'
      f'Общая стоимость всех товаров - {sum_price}\n'
      f'Средняя цена товаров - {average_price:.2f}')