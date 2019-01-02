import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#通过传递一个list对象来创建一个Series，pandas会默认创建整型索引
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)
#通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

#传递一个能够被转换成类似序列结构的字典对象来创建一个DataFrame
df2 = pd.DataFrame(
    { 'A' : 1.,
    'B' : pd.Timestamp('20130102'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })
print(df2)
#查看不同列的数据类型
print(df2.dtypes)
print(df.head(3))
print(df.tail(2))

#显示数据框的索引，列名和值
print(df.index,df.columns,df.values)

#描述性显示关于数据的简短统计摘要
print(df.describe())

#转置数据
print(df.T)

#通过值来sort
print(df.sort_values(by='B'))

#方括号中输入这个单一的列名，来获得一个Series，该操作相当于df.A
print(df['A'])

#通过对行切片来获取数据
df[0:3]
df['20130102':'20130104']
df.loc[dates[0]]
df.loc[:,['A','B']]

df.loc['20130102':'20130104',['A','B']]

#c 是个series
c = df.loc['20130102',['A','B']]
print(c)

df.loc[dates[0],'A']

#通过适合的整数来代表位置进行索引
df.iloc[3]

df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]

df.iloc[1,1]
df.iat[1,1]


df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

#过滤数据
df2[df2['E'].isin(['two','four'])]

df.at[dates[0],'A'] = 0
df.iat[1,1] = 0
print(df)

#删除所有含有缺失值的行
df.dropna(how='any')

#替换缺失值
df.fillna(value=5)

print(df.mean(1))

df = pd.DataFrame(np.random.randn(3, 4), columns=['A','B','C','D'])

print(df)
#列均值
print(df.mean())
print(df.mean(0))
#行均值
print(df.mean(1))

#dataframe append row
print(df)
s = df.iloc[1]
print(s)

print(df.append(s, ignore_index=True))

df.plot.bar()
plt.show()