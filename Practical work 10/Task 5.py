print("Банкомат")

user_balance = 1000

while True:
    print(f"\n{"="*5}Выберите действие{"="*5}\n \n    1. Узнать баланс\n    2. Снять 100 рублей"
          f"\n    3. Положить 100 рублей\n    4.Выход\n{"="*27}\n")
    user_choice = input("Выберите действие: ")

    match user_choice:
        case "1":
            print(f"Ваш баланс: {user_balance}")
        case "2":
            if user_balance >= 100:
                user_balance -= 100
                print("Деньги успешно сняты")
            else:
                print("Ошибка! Недостаточно средств!")
        case "3":
            user_balance += 100
        case "4":
            print("До свидания!")
            break
        case _:
            print("Неверная команда!")