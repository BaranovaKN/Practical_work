class Zombie:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def bite(self):
        while True:
            try:
                damage= int(input('Введите силу укуса:'))
                if damage < 0:
                    print('введены некорректные данные!')
                    continue
                break
            except ValueError:
                print('введены некорректные данные!')

        self.hp -= damage
        print(f'Остаток здоровья {self.name}: {self.hp}')


def create():
    while True:
        user_zombie = input('Введите через пробел имя здоровье зомби: ').split()
        if len(user_zombie) != 2:
            print('Введите нормальные значения >:/')
            continue
        else:
            try:
                name, hp = user_zombie
                hp = int(hp)
                return Zombie (name, hp)
            except ValueError:
                print('Введите нормальные значения >:/')

m1 = create()
m1.bite()