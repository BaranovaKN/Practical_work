class Monster:
    def __init__ (self, name):
        self.name = name

    def introduce(self): # Отстутсвует ссылка на объект класса
        print(f'я {self.name}, и я хочу кушать!')


m = Monster('Упырь')
m.introduce()