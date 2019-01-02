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
'''
# 本函数用于将东财网下载的xls格式文本转为csv格式文本
# http://soft-f9.eastmoney.com/soft/gp18.php?code=60032301&exp=1
def e2csv(ct):
    ct = ct.replace('&nbsp;','').replace('--','0.00').replace(',','')
    ret=''
    rows = re.findall(r'<row.*?>(.*?)</row>',ct,re.S|re.I)
    for i in range(len(rows)):
        cells = re.findall(r'<data.*?>(.*?)</data>',rows[i],re.S|re.I)
        r = ','.join(cells)
        ret = ret + r + '\n'
    return ret

stock_code = '600499'
bs_url='http://soft-f9.eastmoney.com/soft/gp15.php?code={co}01&exp=1'.format(co=stock_code)
ct = ro.get(bs_url).text
r = e2csv(ct)
open('%s.csv'% stock_code,'w',encoding='gbk').write(r)

pd.read_csv('s.csv',encoding='gbk')



doc = pq(url='https://www.python.org/events/python-events/')

title = list(doc('.event-title').items())
time = list(doc('time').items())
location = list(doc('.event-location').items())

i = 0
for i in range(len(title)):
    print('会议: %s，\n会议时间：%s,\t会议地点：%s\n' % (title[i].text(), time[i].text(), location[i].text()))

'''

table_asset = pd.read_html('http://money.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/002258/ctrl/part/displaytype/4.phtml')
table_earn = pd.read_html('http://money.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/002258/ctrl/part/displaytype/4.phtml')
#table_cash = pd.read_html('http://money.finance.sina.com.cn/corp/go.php/vFD_CashFlow/stockid/002258/ctrl/part/displaytype/4.phtml')

#print (table_asset[13])
#print (table_earn[13])


df = table_earn[13].transpose()
#print (table_cash[13])
#table[13].to_csv('002258.csv',index=False)
df.to_csv('002258_earn.csv',index=False,encoding='gbk')
df = table_asset[13].transpose()

df.plot()
plt.show()
df.to_csv('002258_asset.csv',index=False,encoding='gbk')
