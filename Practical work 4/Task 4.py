
students = int(input("введите количество студентов: "))
mandarin = int(input("введите количество мандаринов: "))

mandarin_for_student = mandarin//students
mandarin_rest = mandarin%students

print(f"студенты получили по {mandarin_for_student} мандаринов в руки, а в корзине осталось {mandarin_rest}")