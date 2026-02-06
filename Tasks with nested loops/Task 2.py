print("Шахматная доска")
SIZE = 8

for i in range(SIZE):
    for j in range(SIZE):
        if (i + j) % 2 == 0:
            print("W", end=" ")
        else:
            print("B", end=" ")
    print()