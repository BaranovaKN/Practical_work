
import random

num = random.randint(1,10)
total_attempts = 3

print("Было загадано число от 1 до 10 попробуйте его отгдать за 3 попытки!\n")
for i in range(total_attempts):
    user_attempt = int(input("Введите число: "))
    if user_attempt == num:
        print("Угадали!")
        break
    elif user_attempt > num:
        print("Неверно! Загаданное число меньше")
    else:
        print("Неверно! Загаданное число больше")

if total_attempts == i + 1:
    print(f"Вы проиграли! Загаданное число было {num}")