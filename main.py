import requests
from lxml import etree
from bs4 import BeautifulSoup
import xlwt


def get_gsId():
    """
    获得基金公司Id和名称
    """
    result_list = []
    url = "http://fund.eastmoney.com/company/default.html"
    res = requests.get(url, headers=headers).content.decode("utf-8")

    res_html = etree.HTML(res)
    a_href_list = res_html.xpath(
        '//table[@id="gspmTbl"]/tbody/tr/td[2]/a/@href')
    a_text_list = res_html.xpath(
        '//table[@id="gspmTbl"]/tbody/tr/td[2]/a/text()')
    # print(a_text_list)
    gsId_list = []
    for a in a_href_list:
        gsId_list.append(a.split("/")[2].split(".")[0])
    print(gsId_list)
    for result in zip(gsId_list, a_text_list):
        # print(result)
        result_list.append(result)
    print(result_list)
    print(f"共有{len(result_list)}家基金公司")
    return result_list


def get_data_list(gsId):
    """基金公司持有的股票情况"""
    # url="http://fund.eastmoney.com/Company/tzzh/GsccQuarter?gsId=80000221&year=2020&quarter=3&ftype=0"
    # url="http://fund.eastmoney.com/Company/tzzh/GsccQuarter?gsId=80000229&year=2020&quarter=3&ftype=0"
    url = f"http://fund.eastmoney.com/Company/tzzh/GsccQuarter?gsId={gsId}&year=2020&quarter=3&ftype=0"

    res = requests.get(url, headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text, "html.parser")
    # 持有股票数量len(soup.findAll("tr")-1
    print(f'当前基金公司持有股票数量：{len(soup.findAll("tr"))-1}')
    data_list = []
    for tr in soup.findAll("tr")[1:]:
        entry_data = []
        for td in tr.findAll("td"):

            if td.string == None:
                entry_data.append(td.findAll("a")[0].string)
                # print(td.findAll("a")[0].string)
            # print(td.string)
            entry_data.append(td.string)
        # print(entry_data)
        data_list.append(entry_data)
    print(data_list)
    return data_list


def write2excel(two_dimensional_data, filename):
    """写入到excel"""
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("sheet1")
    for i in range(len(two_dimensional_data)):
        for j in range(len(two_dimensional_data[i])):

            sheet.write(i, j, two_dimensional_data[i][j])
    wb.save(f"data/{filename}.xls")


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    # get_data_list(80000221)
    # 所有基金公司的Id
    fund_info = get_gsId()

    for f in fund_info:
        # get_data_list(f[0])
        write2excel(get_data_list(f[0]), f[1])
    # write2excel(get_data_list(80000221),)
