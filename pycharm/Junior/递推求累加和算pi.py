# 1-1/3+1/5+~~+
s = 0
t = 1
tt = 1
flag = 1

while abs(t) >= 1e-4:
    s += t
    flag = -flag
    tt += 2
    t = 1.0 / tt * flag
print("%.6f" % (4 * s))
print("loop %d times"%((tt+1)/2))
