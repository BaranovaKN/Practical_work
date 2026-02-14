
prices_str = '100 50 200 150 75 300'
prices_list = prices_str.split()
prices_list = [int(price) for price in prices_list]
prices_list.remove(max(prices_list))
prices_list.append(int(round(max(prices_list)/2)))
prices_list.sort()
print(f'Список цен: {','.join(map(str, prices_list))}')
print(f'Средняя цена: {sum(prices_list) / len(prices_list)}')
