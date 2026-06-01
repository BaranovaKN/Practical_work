import random

class Monster:
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_name(self, name):
        self.__name = name
        print(f'Установлдено имя: {self.__name}')

    def set_hp(self, hp):
        if hp < 0:
            print('ОШибка! Здоровье не может быть отрицательным')
            self.__hp = 0

        else:
            self.__hp = hp
        print(f'Текущее здоровье {self.get_name()}: {self.__hp}')

    def set_dmg(self, dmg):
        if dmg < 0:
            print('Ошибка! Сила атаки не может быть отрицательной')
            self.__dmg = 0

        else:
            self.__dmg = dmg
        print(f'Текущая сила атаки: {self.__dmg}')

    def is_alive(self):
        if self.get_hp() <= 0:
            return False
        else:
            return True

    def show_status(self):
        print(f'{self.get_name()}: {self.get_hp()}')

    def take_damage(self, damage):
        if damage > 0:
            self.set_hp(self.get_hp() - damage)

        else:
            print('Ошибка! Сила атаки не может быть отрицательной')

    def attack(self, hunter):
        print(f'{self.get_name()} атакует!\n')
        hunter.take_damage(self.get_dmg())


class Zombie(Monster):
    def __init__(self, name):
        super().__init__(name, hp = 120, dmg = 10)

    def take_damage(self, damage):
        super().take_damage(damage)
        print(f'У {self.get_name()} отваливается конечность!')

    def attack(self, hunter):
        print(f'{self.get_name()} кусает {hunter.get_name()}\n')
        hunter.take_damage(self.get_dmg())


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name, hp = 80, dmg = 15)

    def take_damage(self, damage):
        if damage > 0:
            self.set_hp(self.get_hp() - damage + 5)
            print(f'{self.get_name()} поглощает 5 урона!')

        else:
            print('Ошибка! Сила атаки не может быть отрицательной')

    def attack(self, hunter):
        print(f'{self.get_name()} кусает {hunter.get_name()} и пьет его кровь!\n')
        hunter.take_damage(self.get_dmg())


class Ghost(Monster):
    def __init__(self, name):
        super().__init__(name, hp = 60, dmg = 20)

    def take_damage(self, damage):
        if damage > 0:
            chance_dodge = random.randint(1,10)
            if chance_dodge > 3:
                self.set_hp(self.get_hp() - damage)
                print(f'{self.get_name()} пытается исчезнуть.')

            else:
                print(f'{self.get_name()} становится прозрачным и орудие проходит сквозь него')

        else:
            print('Ошибка! Сила атаки не может быть отрицательной')

    def attack(self, hunter):
        print(f'{self.get_name()} пролетает сквозь {hunter.get_name()}\n')
        hunter.take_damage(self.get_dmg())


class Werewolf(Monster):
    def __init__(self, name):
        super().__init__(name, hp = 100, dmg = 25)

    def transformation(self):
        print(f'{self.get_name()} Трансформируется')

    def take_damage(self, damage):
        if damage > 0:
            self.set_hp(self.get_hp() - damage)
            if self.get_hp() <= 25:
                self.transformation()
            print(f'{self.get_name()} рычит!')
        else:
            print('Ошибка! Сила атаки не может быть отрицательной')

    def attack(self, hunter):
        print(f'{self.get_name()} рычит и атакует когтями {hunter.get_name()}!\n')
        hunter.take_damage(self.get_dmg())


class Weapon:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

    def use(self, monster):
        print(f'{monster.get_name()} атакуется {self.name}\n')
        monster.take_damage(self.dmg)


class SilverSword(Weapon):
    def __init__(self):
        super().__init__(name = 'Серебряный меч', dmg = 30)

    def use(self, monster):
        print(f'{self.name} пронзает {monster.get_name()}!\n')
        monster.take_damage(self.dmg)


class HolyWater(Weapon):
    def __init__(self):
        super().__init__(name = 'Святая вода', dmg = 20)

    def use(self, monster):
        print(f'{self.name} жгет {monster.get_name()}!\n')
        monster.take_damage(self.dmg)


class CrossbowBolt(Weapon):
    def __init__(self):
        super().__init__(name='Арбалет с болтом', dmg = 25)

    def use(self, monster):
        print(f'{self.name} заряжается и болт пронзает {monster.get_name()}\n!')
        monster.take_damage(self.dmg)


class Hunter:
    def __init__(self, name, hp = 100):
        self.__name = name
        self.__hp = hp
        self.__inventory = []

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_name(self, name):
        self.__name = name
        print(f'Установлдено имя: {self.__name}')

    def set_hp(self, hp):
        if hp < 0:
            print('ОШибка! Здоровье не может быть отрицательным')
            self.__hp = 0
        else:
            self.__hp = hp
        print(f'Текущее здоровье {self.get_name()}: {self.get_hp()}')

    def add_weapon(self, weapon):
        self.__inventory.append(weapon)
        print(f'{self.get_name()} получил {weapon.name}!')

    def show_inventory(self):
        if len(self.__inventory) > 0:
            for i in range(len(self.__inventory)):
                print(f'{i+1}. {self.__inventory[i].name}')

        else:
            print('Инвентарь пуст')


    def attack(self, weapon_index, monster):
        print(f'\n{self.get_name()} аттакует!')
        self.__inventory[weapon_index-1].use(monster)

    def is_alive(self):
        if self.get_hp() <= 0:
            return False
        else:
            return True

    def show_status(self):
        print(f'{self.get_name()}: {self.get_hp()}')
        print(f'Инвентарь {self.get_name()}:\n')
        self.show_inventory()

    def take_damage(self, damage):
        if damage > 0:
            self.set_hp(self.get_hp() - damage)
            print(f'{self.get_name()} получает урон!\n')

        else:
            print('Ошибка! Сила атаки не может быть отрицательной')


def run_games():
    h = Hunter('Ван Хельсинг')
    h.add_weapon(CrossbowBolt())
    h.add_weapon(SilverSword())
    h.add_weapon(HolyWater())
    h.add_weapon(Weapon('Читерский меч',100))
    monsters = [Zombie('Зомби'), Vampire('Дракула'), Ghost('Лизун'), Werewolf('Люкан')]

    i = 0
    round_num = 1
    while i < len(monsters) and h.is_alive():
        while monsters[i].is_alive() and h.is_alive():
            print('-'*30, f'\nРаунд {round_num}\n', '-'*30)
            round_num += 1
            h.show_status()
            try:
                user_weapon = int(input('\nВыберите номер оружия для атаки: '))

            except ValueError:
                print('Ошибка! Введены некорректные данные!')

            else:
                if not 0 < user_weapon <= len(monsters):
                    print(f'Ошибка выдолжны выбрать номер оружия от 1 до {len(monsters)}!')
                    continue

            h.attack(user_weapon, monsters[i])
            if monsters[i].is_alive():
                monsters[i].attack(h)
            else:
                print(f'{monsters[i].get_name()} погиб!')
                i +=1
                break

            if not h.is_alive():
                print(f'{h.get_name()} погиб в бою! Вы проиграли!')
                break

        if not h.is_alive():
            break
    else:
        print(f'Вы победили! Битва пройдена за {round_num} раундов')

run_games()
# h = Hunter('Ван Хельсинг')
# # h.show_inventory()
# # print(h.get_hp())
# # print(h.get_name())
# h.add_weapon(CrossbowBolt())
# h.show_status()
# h.add_weapon(CrossbowBolt())
# h.show_inventory()
# print(h.is_alive())
# h.set_hp(-20)
# print(h.is_alive())
# weapons = [SilverSword(), HolyWater(), CrossbowBolt()]
# zombie = Zombie("Зомби")
# for w in weapons:
#     w.use(zombie)

# m = Monster('Зомби', 100, 10)
# m.show_status()
# m.set_hp(-50)
# m.show_status()
# print(m.is_alive())
#
# v = Vampire("Дракула")
# v.take_damage(30)
#
# z = Zombie("Зомби")
# z.take_damage(30)

