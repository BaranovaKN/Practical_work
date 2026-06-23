class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 100, power = 10):
        self.name = name
        self.hp = hp
        self.power = power
        print(f"Монстр создан!\nМонстр: {name}\nHP: {hp}\nPower: {power}\n\n")

    def show_info(self):
        print(f'Информация о монстре:\n Имя: {self.name}\n Здоровье❤️: {self.hp}\n Урон⚔️: {self.power}\n','-'*15)

    def mutate(self):
        self.power += 5
        print(f'{self.name} мутирует! Сила увеличена!\n⚔️: {self.power}')

    def rest(self):
        self.hp += 5
        print(f'{self.name} отдыхает в склепе! Здоровье восстановлено!\n❤️: {self.hp}')


def create():
    while True:
        user_monster = input('Введите через пробел имя hp и силу монстра: ').split()
        if len(user_monster) != 3:
            return Monster()
        else:
            try:
                name, hp, power = user_monster
                hp, power = int(hp), int(power)
                return Monster(name, hp, power)
            except ValueError:
                print('Введите нормальные значения >:/')

m1 = create()
m1.show_info()
m1.mutate()
m1.rest()