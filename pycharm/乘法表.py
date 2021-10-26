x = int(input())
for i in range(1,x + 1):
    for j in range(i):
        j = j + 1
        print("%d*%d=%-3d" % (j,i,i * j),end = "")
    print("")
