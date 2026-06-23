import math
MAX_NUM = 150

for a in range(MAX_NUM+1):
    for b in range(a, MAX_NUM+1):
        for c in range(b, MAX_NUM+1):
            for d in range(c, MAX_NUM+1):
                sum = math.pow(a,5) + math.pow(b,5) + math.pow(c,5) + math.pow(d,5)
                e = round(math.pow(sum, 1/5))
                if e**5 == sum and e <= 150 :
                    print(f'Сумма подходящих чисел: {a+b+c+d+e}')