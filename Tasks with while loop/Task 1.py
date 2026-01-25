
print("Последовательность слов")

user_word = ""
count = -1

while user_word != "стоп" and user_word != "хватит" and user_word != "достаточно":
    user_word = input("Введите слово: ")
    count += 1
else:
    print(f"Количество слов: {count}")