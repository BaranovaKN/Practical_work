server_a = set(input('Введите имена файлов с сервера А: ').split())
server_b = set(input('Введите имена файлов с сервера В: ').split())
print('Общие файлы с двух серверов: ',*server_a.intersection(server_b))
print('Файлы, которые были утеряны на сервере B: ',*server_a.difference(server_b))