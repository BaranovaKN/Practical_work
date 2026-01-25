
num = int(input("Введите четырехзначное число: "))

num_thousand = num//1000
num_hundred = (num-num_thousand*1000)//100
num_tens = (num-num_thousand*1000-num_hundred*100)//10
num_units = num-num_thousand*1000-num_hundred*100-num_tens*10

print(f"Цифра в позиции тысяч равна {num_thousand} "
      f"\nЦифра в позиции сотен равна {num_hundred} "
      f"\nЦифра в позиции десятков равна {num_tens} "
      f"\nЦифра в позиции единиц равна {num_units} ")