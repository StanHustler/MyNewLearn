for i in range(1,501):
    with open(str(i)+'.txt',"r") as f:  
        str1 = f.read()
        if 'key{' in str1:
            print(i)