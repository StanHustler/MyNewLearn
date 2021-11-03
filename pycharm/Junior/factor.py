import math as m

while True:
    n = eval(input())
    if n < 2:
        print(f"{n} is a prime")
    else:
        f = True
        for i in range(2, m.ceil(m.sqrt(n)) + 1):
            if n % i == 0:
                f = False
                break
        print(f"{n} is a prime" if f else f"{n} isn't a prime")
