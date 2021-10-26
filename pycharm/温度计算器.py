#c = eval(input())
#f = 5/9*c+32
#print(f)

s = input("请输入带符号的温度值：")

if s[-1] in {"C", "c"}:
    c = eval(s[0:-1])
    f = 1.8*c + 32
    print("温度%.2fF"%f)
elif s[-1] in {"F", "f"}:
    f = eval(s[0:-1])
    c = (f-32)/1.8
    print("温度%.2fC"%c)
else:
    print("格式错误")
