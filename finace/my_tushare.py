#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import tushare as ts
import os
import time

'''
df = ts.get_hist_data('002258') # 获取全部日线数据
report = ts.get_report_data(2017,4)
report.to_csv('report2017q4.csv')
df.to_csv('data.csv')
'''

'''
stock_info=ts.get_stock_basics()
def get_all_stock_id():
#获取所有股票代码
for i in stock_info.index:
print i

'''


all_share = ts.get_today_all()
print("all share in market",all_share.shape[0])


#all available_share today 没有停牌的股票
available_share = all_share[all_share.amount > 0.0]
print("没有停牌的股票数",available_share.shape[0])

middle_share_number = int(available_share.shape[0] / 2)

#按照列amount  成交量 降序排列数据
available_share.sort_values(by='amount', ascending=False)

middle_share= available_share.iloc[middle_share_number]

middle_code = middle_share.code
middle_amount  = middle_share.amount

# 格式化成2016-03-20 11:45:39形式
current_date = time.strftime("%Y-%m-%d", time.localtime())

stock = {'code': middle_code, 'amount': middle_amount}
#index = [current_date]

# 建立dataframe用时间作为索引
#date_index = pd.to_datetime(index)
current_date_value = pd.DataFrame(data=stock, index=[current_date])

'''
#amount column  series
amount_list  = available_share.amount
'''
if os.path.exists('middle_amount.csv'):
    #：从CSV文件导入数据
    history_value  = pd.read_csv('middle_amount.csv',encoding = "utf_8_sig",index_col=0,sep=',')
    new_value = history_value.append(current_date_value)
    new_value.to_csv('middle_amount.csv', encoding="utf_8_sig",sep=',')
else:
    current_date_value.to_csv('middle_amount.csv', encoding="utf_8_sig",sep=',')




