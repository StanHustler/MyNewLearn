l,r = map(eval,input().split())
count=0
for i in range(l,r+1):
    n=i
    while n>0:
        if n%10 ==2:
            count+=1
        n//=10
print(count)