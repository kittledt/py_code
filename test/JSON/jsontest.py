# -*-coding=utf-8-*-
import json

with open('finance_company.json', encoding='utf-8') as f:
    line = f.readline()
    d = json.loads(line)
    name = d['name']
    company_url = d['company_url']
    telephone = d['telphone']
    crawl_time = d['crawl_time']
    print(name, company_url, telephone, crawl_time)
    d['name'] = '易捷金融'

with open('finance_company2.json','w',encoding='utf-8') as f:
    json.dump(d,f,ensure_ascii=False)             #默认的 ensure_ascii=True ,我们的中文自动转义了， 变成了ASCII码，

with open('finance_company2.json', encoding='utf-8') as f:
    line = f.readline()
    d = json.loads(line)
    name = d['name']
    company_url = d['company_url']
    telephone = d['telphone']
    crawl_time = d['crawl_time']
    print(name, company_url, telephone, crawl_time)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

with open('student.json','w',encoding='utf-8') as f:
    json.dump(s,f,default=lambda obj: obj.__dict__)       #可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

with open('student.json', encoding='utf-8') as f:
    line = f.readline()
    print(line)                                              #loads()把str转dict，object_hook把dict转student
    s = json.loads(line ,object_hook=dict2student)
    print(s)