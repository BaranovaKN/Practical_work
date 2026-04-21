import random

num_list = [random.randint(-10, 10) for i in range(10)]
print('Исходный случайный массив:',*num_list)
min_num_index = 0
# min_num_index = num_list.index(min(num_list))
for i in range(len(num_list)):
    if num_list[i] < num_list[min_num_index]:
        min_num_index = i
num_list[0], num_list[min_num_index] = num_list[min_num_index], num_list[0]
print('Массив после смены первого и минимального элемента:',*num_list)