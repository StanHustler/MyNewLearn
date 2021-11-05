""" format Most_Ch:Times

txt = open("命运.txt", "r", encoding="utf-8").read()
for ch in "，。？；！":
    txt = txt.replace(ch, "")
d = {}
for ch in txt:
    d[ch] = d.get(ch, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[-1], reverse=True)
# print(ls[0][0], ls[0][1], sep=":")
a, b = ls[0]
print(f"{a}:{b}")
"""

""" format 1st_Ch2nd_Ch...10rd_Ch

txt = open("命运.txt", "r", encoding="utf-8").read()
for ch in "\n":
    txt = txt.replace(ch, "")
d = {}
for ch in txt:
    d[ch] = d.get(ch, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x:x[-1],reverse=True)
for i in range(10):
    print(ls[i][0],end="")
"""


txt = open("命运.txt", "r", encoding="utf-8").read()
for ch in "\n ":
    txt=txt.replace(ch,"")
d={}
for ch in txt:
    d[ch]=d.get(ch,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
string=""
for i in range(len(ls)):
    string+=ls[i][0]+":"+str(ls[i][1])+","
string = string[:-1]
f=open("命运-频次排序.txt","w",encoding="utf-8")
f.write(string)
f.close()
