
import math

num_seat = int(input("введите номер места: "))
place_in_coupe = 4

num_coupe = math.ceil(num_seat/place_in_coupe)

print(f"при номере места {num_seat} пассажир будет в {num_coupe} купе")