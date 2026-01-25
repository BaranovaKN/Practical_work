
height, weight = map(float, input("Пожалуйста введите ваш рост(в метрах) "
                                  "и вес (в кг) в одной строке через пробел: ").split())
bmi = weight / (height * height)
print(f"\nваш Индекс Массы Тела - {bmi:.1f}")