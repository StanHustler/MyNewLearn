import requests
url="https://p0.ssl.qhimgs4.com/t016d368e4d7f809aa0.jpg"
kv={"User-Agent":"Mozilla/5.0"}
path="D://1.jpg"
try:
    r=requests.get(url,headers=kv)
    r.raise_for_status()            #判断状态是否为200
    with open(path,"wb") as f:      #with会自动close，w=write，b=binary
        f.write(r.content)          #content 二进制
    print("complete!")
except:
    print("errrrrr!!")
