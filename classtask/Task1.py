class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 100, dmg = 10):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстр создан!\nМонстр: {name}\nHP: {hp}\nDMG: {dmg}\n\n")

    def show_info(self):
        print(f'Информация о монстре:\n Имя: {self.name}\n Здоровье❤️: {self.hp}\n Урон⚔️: {self.dmg}\n','-'*15)


def create():
    while True:
        user_monster = input('Введите через пробел имя hp и dmg монстра: ').split()
        if len(user_monster) != 3:
            return Monster()
        else:
            try:
                name, hp, dmg = user_monster
                hp, dmg = int(hp), int(dmg)
                return Monster(name, int(hp), int(dmg))
            except ValueError:
                print('Введите нормальные значения >:/')

Gargoyle = create()
Gargoyle.show_info()
