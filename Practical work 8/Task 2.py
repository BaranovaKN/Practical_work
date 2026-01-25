
res = "YES"
for i in range(10):
    if int(input("Введите число: ")) % 2 == 1:
        res = "NO"
print(res)