n = eval(input())
a,b = 1,1
if n==1:
    print(1)
elif n==2:
    print(1,1)
else:
    print(1,1,end=" ")
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")