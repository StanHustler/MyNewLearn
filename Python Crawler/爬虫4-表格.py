import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLtext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()            #判断状态是否为200
        r.encoding=r.apparent_encoding  #encoding是header的charset，如没有，返回ISO-8859-1
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):      #筛选tr标签
            tds=tr.find_all("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    print("{0:^10}\t{1:^15}\t{2:^10}".format("排名","学校名称","省份"))
    for i in range(num):
        u=ulist[i]
        print("{0:^10}\t{1:^15}\t{2:^10}".format(u[0],u[1],u[2]))


uinfo=[]
url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
html=getHTMLtext(url)
fillUnivList(uinfo,html)
printUnivList(uinfo,20)
