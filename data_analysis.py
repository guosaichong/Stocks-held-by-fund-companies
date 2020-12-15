import os
import xlrd
from main import write2excel

file_name_list = os.listdir("data")
stocks_list = []
for f in file_name_list:
    table = xlrd.open_workbook("data/"+f).sheet_by_name("sheet1")
    for i in range(table.nrows):
        stocks_list.append(table.cell(i, 1).value)
print(stocks_list)
print(len(stocks_list))
stock_dic = {}
for stock in set(stocks_list):

    # print(stock,stocks_list.count(stock))
    stock_dic[stock] = stocks_list.count(stock)
print(stock_dic)
sorted_result = sorted(stock_dic.items(), key=lambda kv: (kv[1]))
print(sorted_result)

write2excel(sorted_result, "sorted_result")
