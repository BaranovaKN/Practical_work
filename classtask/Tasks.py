class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 100, dmg = 10):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстр создан!\nМонстр: {name}\nHP: {hp}\nDMG: {dmg}\n\n")


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

def battle(m1, m2):

    while True:
        print(f"{m1.name} наносит удар!")
        m2.hp -= m1.dmg
        if m2.hp <= 0:
            winner = m1.name
            m2.hp = 0
            break
        print(f"У {m2.name} осталось {m2.hp} здоровья")
        print(f"{m2.name} наносит удар!")
        m1.hp -= m2.dmg
        if m1.hp <= 0:
            winner = m2.name
            m1.hp = 0
            break
        print(f"У {m1.name} осталось {m1.hp} здоровья")

    print(f"У {m1.name} осталось {m1.hp} здоровья")
    print(f"У {m2.name} осталось {m2.hp} здоровья")
    print(f"Победил: {winner}")

m1 = create()
m2 = create()

battle(m1, m2)
