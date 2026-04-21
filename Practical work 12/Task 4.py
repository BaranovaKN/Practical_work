marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

count_5 = 0
count_2 = 0

for mark in marks:
    if mark == 5:
        count_5 += 1
    elif mark == 2:
        count_2 += 1

print(f'Количество оценок 5 - {count_5}\nКоличество оценок 2 - {count_2}')