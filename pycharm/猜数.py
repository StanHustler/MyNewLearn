import random as r
import math as m

a, b = 1, 100
ans = r.randint(a, b + 1)
mx = m.ceil(m.log(b - a) / m.log(2))

print("请在[%d,%d]内猜一个数字" % (a, b))
m = 0
cont = 0
while True:
    x = eval(input())
    m += 1
    if x == ans:
        print("恭喜答对，共猜了%d次" % m)
        break
    elif x > ans:
        print("大了", end="，")
    else:
        print("小了", end="，")

    if cont == 0:
        if m < mx:
            print("还有%d次机会" % (mx - m))
        else:
            print("没机会了，", end="")
            if input("是否要继续猜(Y/N)：") in ("y", "Y"):
                cont += 1
            else:
                break
    else:
        print("额外的第%d次" % (m  - mx))
