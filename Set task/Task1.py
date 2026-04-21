group_1 = {'Иван', 'Мария', 'Петр', 'Сергей', 'Анна'}
group_2 = {'Мария', 'Анна', 'Дмитрий', 'Елена', 'Сергей'}

group_intersection = group_1.intersection(group_2)
print('Студенты, которые находятся в обоих группах:', *group_intersection, sep=' ')
group_just_1 = group_1.difference(group_2)
print('Студенты, которые находятся только в первой группе:', *group_just_1, sep=' ')
group_just_2 = group_2.difference(group_1)
print('Студенты, которые находятся только во второй группе:', *group_just_2, sep=' ')
group_union = group_1.union(group_2)
print('Студенты, которые учатся хотя бы в одной из групп:', *group_union, sep=' ')
group_difference = group_1.symmetric_difference(group_2)
print('Студенты, которые учатся только в одной из групп:', *group_difference, sep=' ')
