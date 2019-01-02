#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd
import datetime
import urllib
from urllib.request import urlopen
from urllib.request import Request
import re


#with open('.\stock.txt', 'w', encoding = 'utf-8') as f:
#    raw = f.read()



url ='http://quote.eastmoney.com/stocklist.html'

res = urlopen(url)
content = res.read().decode("gbk")


'''
<li><a target="_blank" href="http://quote.eastmoney.com/sh500016.html">基金裕元(500016)</a></li>
            
<li><a target="_blank" href="http://quote.eastmoney.com/sh500017.html">基金景业(500017)</a></li>
            
            
'''

#提取出 基金景业(500017)
pattern = re.compile(r'<li><a.*?href=.*?html">(.*?)</a></li>',re.S)
items = re.findall(pattern,content)


pattern2 = re.compile(r'[^()]+')
stocklist = []
for item in items:
    newitem = re.findall(pattern2,item)
    stocklist.append(newitem[1])

#print(items)
print(stocklist)





time1=datetime.datetime.now()
data1=ts.get_realtime_quotes(stocklist[2640:2648])
#data2=ts.get_realtime_quotes(stocks[880:1760])
#data3=ts.get_realtime_quotes(stocks[1760:2640])
#data4=ts.get_realtime_quotes(stocks[2640:-1])
time2=datetime.datetime.now()
print('开始时间：'+str(time1))
print('结束时间：'+str(time2))
print(data1)

print(ts.get_suspended())



