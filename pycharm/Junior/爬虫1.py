import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "connect error"


if __name__ == '__main__':
    # print(getHTMLText("http://wlacm.com"))

    payload={"key1":"value1"}
    r = requests.post("https://httpbin.org/post", params=payload,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'})
    print(r.text)