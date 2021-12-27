a,b=map(eval,input().split())

ls=[]
for i in range(eval(input())):
    ls.append(eval(input()))

n = int(input())
matrix = [[eval(j) for j in input().split()] for i in range(n)]

##########Function##########
def factorial(num: int) -> int:
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

def isPrime(num: int) -> bool:
    if num == 1 or num==4:
        return False
    elif num==2 or num==3:
        return True
    else:
        # 大于等于5的质数一定和6的倍数相邻
        # 不在6的倍数两侧的一定不是质数
        if num%6!=1 and num%6!=5:
            return False
        # 在6的倍数两侧的也可能不是质数
        # 在6的俩侧如果不是素数，那么就是5或者7的倍数，只需要判断是否为这俩个数的倍数即可
        for i in range(5,int(num**0.5)+1,6):
            if num%i==0 or num%(i+2)==0:
                return False
        return True
def Goldbach(n:int)->str:
    for i in range(n):
        if isPrime(i) and isPrime(n-i):
            return ("{} = {} + {}".format(n,i,n-i))

def decomposingFactor(num: int)->str:
    for i in range(2,num):
        if num%i ==0:
            return str(i)+"*"+str(decomposingFactor(num//i))
    return num

def Fibonacci(max:int):
    a, b = 1, 1
    print(1,1,end=" ")
    while b <= max:
        a, b = b, a + b
        print(b,end=" ")

def gcd(a:int,b:int)->int:
    return a if b==0 else gcd(b,a%b)
def lcm(a, b)->int:
    return a / gcd(a, b) * b

def josephus(num:int,gap:int)->int:
    index=0
    ls=[x for x in range(1,num+1)]
    while len(ls)>1:
        index=(index+(gap-1))%len(ls)
        # print('kill:',ls[index])
        del ls[index]
    return ls[0]



