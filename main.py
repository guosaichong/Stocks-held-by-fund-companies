import requests
from lxml import etree
from bs4 import BeautifulSoup

# url="http://fund.eastmoney.com/Company/tzzh/GsccQuarter?gsId=80000221&year=2020&quarter=3&ftype=0"
# url="http://fund.eastmoney.com/Company/tzzh/GsccQuarter?gsId=80000229&year=2020&quarter=3&ftype=0"
url="http://fund.eastmoney.com/Company/tzzh/GsccQuarter?gsId=80053708&year=2020&quarter=3&ftype=0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
res=requests.get(url,headers=headers)
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
print(len(soup.findAll("tr")))
for tr in soup.findAll("tr")[1:]:
    entry_data=[]
    for td in tr.findAll("td"):
        
        if td.string ==None:
            entry_data.append(td.findAll("a")[0].string)
            # print(td.findAll("a")[0].string)
        # print(td.string)
        entry_data.append(td.string)
    print(entry_data)
