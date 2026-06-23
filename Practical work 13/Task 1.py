num_1 = 5
num_2 = 17
numbers = [10, 5, 17, 3, 8]
numbers.extend([2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6,
               14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5])
print(f'Длинная списка: {len(numbers)} \nПоследний элемеент списка: {numbers[-1]} '
      f'\nСписок в обратном порядке:\n',*numbers[::-1])
if num_1 in numbers and num_2 in numbers:
    print("YES")
else:
    print("NO")
del numbers[0]
del numbers[-1]
print('Список без первого и последнего элемента:\n',*numbers)


