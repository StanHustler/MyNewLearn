x=input('input the string:')
for i in range(1,x,1):
    if x % i == 0 :
        print(str(i)+'  x  '+str( x / int(i)))
