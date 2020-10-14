import requests
url="https://www.baidu.com"
kv={"User-Agent":"Mozilla/5.0"}
try:
    r=requests.get(url,headers=kv)
    r.encoding=r.apparent_encoding  #encoding是header的charset，如没有，返回ISO-8859-1
    r.raise_for_status()            #判断状态是否为200
    print(r.text)
except:
    print("errrrrr!!")
