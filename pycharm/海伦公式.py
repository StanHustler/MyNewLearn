# 海伦公式S=√p(p-a)(p-b)(p-c)，p为半周长

import math

a, b, c = map(int, input().split())  # 边长
p = (a + b + c)/2

s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("%.6f"%s)
