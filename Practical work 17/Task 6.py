import math

def solve(a, b, c):
    d = math.sqrt(math.pow(b,2) - 4*a*c)

    if (-b+d)/(2*a) > (-b-d)/(2*a):
        return (-b+d)/(2*a), (-b-d)/(2*a)
    else:
        return (-b-d)/(2*a), (-b+d)/(2*a)

print(*solve(1,-4,-5))
print(*solve(-2,7,-5))
print(*solve(1,2,1))
