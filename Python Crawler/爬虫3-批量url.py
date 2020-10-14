import requests
from bs4 import BeautifulSoup
url="https://www.bilibili.com/video/av9784617?p=29"

r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")  #解释器

for link in soup.find_all("a"):         #返回列表[]
    print(link.get("href"))            