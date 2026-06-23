user_path = input('Введите путь к вашему файлу: ').split('\\')
print('Путь вашего файла: ', *user_path, sep='\n')