
try:
    temperature = float(input("Пожалуйста введите вашу температуру: "))
    pressure = int(input("Пожалуйста введите ваше давление: "))
    pulse = int(input("Пожалуйста введите ваш пульс: "))

except ValueError:
    print("\nВведены некорректные значения!")

else:
    NORMAL_TEMPERATURE_MIN = 36
    NORMAL_TEMPERATURE_MAX = 37
    MIDDLE_DEVIATION_TEMPERATURE_MIN = 35
    MIDDLE_DEVIATION_TEMPERATURE_MAX = 38
    NORMAL_PRESSURE_MIN = 110
    NORMAL_PRESSURE_MAX = 130
    MIDDLE_DEVIATION_PRESSURE_MIN = 105
    MIDDLE_DEVIATION_PRESSURE_MAX = 140
    NORMAL_PULSE_MIN = 60
    NORMAL_PULSE_MAX = 100
    MIDDLE_DEVIATION_PULSE_MIN = 55
    MIDDLE_DEVIATION_PULSE_MAX = 110

    print("\nВаше состояние здоровья на основе данных ответов: ")

    if (NORMAL_TEMPERATURE_MIN <= temperature <= NORMAL_TEMPERATURE_MAX
            and NORMAL_PRESSURE_MIN <= pressure <= NORMAL_PRESSURE_MAX
            and NORMAL_PULSE_MIN <= pulse <= NORMAL_PULSE_MAX):

        # условие if можно перенести на следующую строку если оно в скобках это позволяет:
        # 1. укоротить код
        # 2. сделать его визуально понятнее
        # благодаря этому в моей работе можно рассмотреть с удобством в каком диапазоне переменные

        print("Вы находитесь в нормальном состоянии")

    elif (temperature < MIDDLE_DEVIATION_TEMPERATURE_MIN or temperature > MIDDLE_DEVIATION_TEMPERATURE_MAX
          or pressure <  MIDDLE_DEVIATION_PRESSURE_MIN or pressure >  MIDDLE_DEVIATION_PRESSURE_MAX
          or pulse < MIDDLE_DEVIATION_PULSE_MIN or pulse > MIDDLE_DEVIATION_PULSE_MAX):
        print("Ваше состояние плохое. Необходим вызов врача!")

    else:
        print("У вас легкое недомогание")
