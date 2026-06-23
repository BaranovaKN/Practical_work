logs_1 = set(input('Введите адреса для проверки из 1 сервера: ').split())
logs_2 = set(input('Введите адреса для проверки из 2 сервера: ').split())
logs_3 = set(input('Введите адреса для проверки из 3 сервера: ').split())
all_logs = logs_1 | logs_2 | logs_3
same_logs = logs_1 & logs_2 & logs_3
all_logs -= same_logs
print('IP-адресса, которые не засветили на всех 3 серверах: ', *all_logs)