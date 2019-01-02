
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = pd.DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])


print(data)
print(data.iloc[:, :3][data.three > 5])





s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

s4 = pd.concat([s1, s3])

print(pd.concat([s1, s4], axis=1))
print(pd.concat([s1, s4], axis=1, join='inner'))
print(pd.concat([s1, s2, s3], axis=1, join='inner'))


df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],'b': [np.nan, 2., np.nan, 6.],'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],'b': [np.nan, 3., 4., 6., 8.]})
print(df1)
print(df2)

data = pd.read_csv('macrodata.csv')
print(data.head())

periods = pd.PeriodIndex(year=data.year, quarter=data.quarter,name='date')
print(periods)
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
print(data.head())

#1959Q1  -> 1959-03-31
data.index = periods.to_timestamp('D', 'end')
print(data[:10])

#Stack,     df的列旋转为series的层次化行
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata[:10])


#long(unstacked) format  in DB - > wide format.
pivoted = ldata.pivot('date','item','value')
print(pivoted[:10])