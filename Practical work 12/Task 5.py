data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three_el = data[0:3]
last_three_el = data[len(data)-3:len(data)]
reverse_list = data[::-1]
odd_index_list = data[1::2]
print('Первая тройка чисел:',*first_three_el)
print('Последняя тройка чисел:',*last_three_el)
print('Список в обратном порядке:',*reverse_list)
print('Только элементы с нечетными индексами:',*odd_index_list)