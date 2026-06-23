allowed_id = set(map(int, input('Введите строку разрешнных id: ').split()))
incoming_id = set(map(int, input('ВВедите строку id которые хотите добавить: ').split()))

for id in incoming_id:
    if id not in allowed_id:
        print(f'id {id} добавлен')
        allowed_id.add(id)
    else:
        print(f'id {id} уже есть в списке')
