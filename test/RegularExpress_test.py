import re
#(r'^\d{3}\-\d{3,8}$', '010-12345'):
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print('ok')       #匹配成功，返回match对象
else:
    print('failed')

#分隔符是至少一个空格字符
print(re.split(r'\s+', 'a b   c'))
#分隔符是至少一个空格，\，\；或者组合
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

print(re.split(r'A|B', 'aAb;; c  Bd'))
print(re.split(r'[AB]+', 'aAb;; c  Bd'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

#提取时间
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

#提取日期，但是对于'2-30'，'4-31'这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。
d = '2-28'
m = re.match(r'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$', d)
print(m.groups())

m = re.match(r'^(\d+?)(0*)$', '102300')
# \d+ 贪婪匹配
# \d+? ('1023', '00')
print(m.groups())

s = '<html><head><title>Title</title>'
m = re.match(r'(<.*>)', s)
print(m.groups())

m = re.match(r'(<.*?>)', s)
print(m.group())
print(m.groups())