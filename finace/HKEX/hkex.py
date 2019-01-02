#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
http://money.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/002258/ctrl/part/displaytype/4.phtml
http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/600499/ctrl/part/displaytype/4.phtml


http://money.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/002258/ctrl/part/displaytype/4.phtml
http://money.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/600499/ctrl/part/displaytype/4.phtml

http://money.finance.sina.com.cn/corp/go.php/vFD_CashFlow/stockid/002258/ctrl/part/displaytype/4.phtml
http://money.finance.sina.com.cn/corp/go.php/vFD_CashFlow/stockid/600499/ctrl/part/displaytype/4.phtml

'''

import requests as ro
import pandas as pd
import re
#use pyquery
from pyquery import PyQuery as pq
import html5lib

import numpy as np
import matplotlib.pyplot as plt
import os
import datetime


'''

函数说明:check stock data, if not up to date, download and save. 

Parameters:
	无
Returns:
	无
Author:
	dingtao
Blog:
	
Modify:
	2018-08-01

'''
def Get_SH_stock():

    #分析网页，得到stock数据是哪一天的。
    r = ro.get('http://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh')
    if (r.status_code == 200):
        print(r.text)

    #提取出 日期
    pattern = re.compile(r'持股日期: [0-9/]+',re.S)
    current_date = re.findall(pattern,r.text)
    print(current_date)

    #current_date is a list, need get[0] to string
    date_group = re.search(r'(\d{2})/(\d{2})/(\d{4})', current_date[0])
    date_index = date_group.group(3)+'-'+date_group.group(2) +'-'+ date_group.group(1)
    print(date_index)

    #get current today time
    #nowTime = datetime.datetime.now().strftime('%Y-%m-%d')          #return string of time
    nowTime = datetime.datetime.now()      #return datetime object
    stockTime = datetime.datetime.strptime(date_index, "%Y-%m-%d")


    # compare time , then down load data and save
    if (nowTime>stockTime):

        table_sh = pd.read_html('http://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh')
        new_tb = table_sh[2]

        #del row 0 and 1
        new_tb.drop(new_tb.index[[0,1]],inplace=True),

        #new_tb.rename(columns = {'0':'code', '1':'name', '2':'valumn','3':'percent'}, inplace = True)
        new_tb.columns = ['code','name','valumn','percent']

        new_tb.set_index('code', inplace=True) # column- code  set to row  index

        #print (sh_stock_tb)

        path = ".\\SH\\" + date_index +".csv"

        if not os.path.exists(path):
            #no such file, save
            new_tb.to_csv(path, encoding="utf_8_sig",sep=',')
            print("save file " + path )

    pass

def check_date_list(path ):
    #path = ".\\SH"
    file_list= []
    if os.path.exists(path):
        for file in os.listdir(path):
            #isfile() need a path ,not a string

            if  os.path.isfile(os.path.join(path, file)):
                (shotname, extension) = os.path.splitext(file)
                file_list.append(shotname)

    return file_list


'''

函数说明:. 
    处理percent 的%， 因为有%，所以是个string ，无法做减法

Parameters:
	stock_date, 带 percent的 series 

Returns:
	去掉 percent的 series 
Author:
	dingtao
Blog:

Modify:
	2018-08-01

'''

def trim_percent_symbol(s):
    for index in s.index:
        #print(index)
        str_percent = s.loc[index]

        value_percent = re.search(r'[0-9\.]+', str_percent)
        #print(value_percent.group(0))
        s.loc[index] = float(value_percent.group(0))
    return s


'''

函数说明:. 

Parameters:
	stock_date, string 需要计算的那一天日期
	stock_path , string ， SH目录，存放原始stock 文件
	delta_path,  string    SH——delta 目录，存放 delta stock 文件
	stock_file_list  需要计算的日期的list
	orignal_stock_list ，SH 目录里面的文件名组成的list
Returns:
	无
Author:
	dingtao
Blog:

Modify:
	2018-08-01

'''
def compute_stock_delta( stock_path ,delta_path,compute_stock_list,orignal_stock_list):

    #循环list里面每一个日期
    for stock_date in compute_stock_list:

        #得到前面一天的日期的index
        path2_index = orignal_stock_list.index(stock_date) - 1


        if path2_index>= 0:
            path2_date =  orignal_stock_list[path2_index ]
        else:
            print("No early date .")
            #need output a empty file, 为了文件占位
            df_empty = pd.DataFrame(np.random.randn(5, 5))
            df_empty.to_csv(delta_path + stock_date + ".csv", encoding="utf_8_sig", sep=',')
            continue


        path1 = stock_path + stock_date + ".csv"
        path2 = stock_path + path2_date + ".csv"

        df_stock1  = pd.read_csv(path1, index_col=0, sep=',')
        df_stock2  = pd.read_csv(path2, index_col=0, sep=',')

        delta_df = df_stock1
        delta_df["valumn"]    = df_stock1["valumn"] - df_stock2["valumn"]

        s_no_percent = trim_percent_symbol(df_stock1["percent"]) - trim_percent_symbol(df_stock2["percent"])
        #print(s_no_percent)

        delta_df["percent"] = s_no_percent


        #save to delta directory
        delta_df.to_csv(delta_path + stock_date + ".csv", encoding="utf_8_sig", sep=',')

    pass


if __name__ == '__main__':

    #download stock file up to date
    #Get_SH_stock()

    #check stock data of HKEK
    stock_file_list = []
    sh_path = ".\\SH"
    stock_file_list = check_date_list(sh_path)
    print(stock_file_list)

    #check delta stock , if not exist , then will compute
    stock_delta_list= []
    sh_delta_path = ".\\SH_Delta"
    stock_delta_list = check_date_list(sh_delta_path)
    print(sh_delta_path)

    compute_stock_set = set(stock_file_list) - set(stock_delta_list)

    compute_stock_list = list(compute_stock_set)
    #list 升序排序
    compute_stock_list.sort()

    # current date
    #nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # return string of time
    compute_stock_delta(".\\SH\\",".\\SH_Delta\\",compute_stock_list,stock_file_list)
    print(stock_file_list)






'''
url = 'http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh'
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "sc.hkexnews.hk",
    "Origin": "http://sc.hkexnews.hk",
    "Referer": "http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
d = {
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR": "",
    "__EVENTVALIDATION": "",
    "today": "20180801",
    "sortBy":"",
    "alertMsg": "",
    "ddlShareholdingDay": "29",
    "ddlShareholdingMonth": "07",
    "ddlShareholdingYear": "2018",
    "btnSearch.x": "21",
    "btnSearch.y": "13",
}
session=ro.session()
requ=session.post(url,headers=headers, data=d)
res=requ.text
print(res)

'''

