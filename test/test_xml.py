# -*- coding:utf-8 -*-
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)
#raw string
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 生成xml
'''
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & data'))
L.append(r'</root>')
a =  ''.join(L)
'''

'''
请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：

https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml

参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。
'''

from xml.parsers.expat import ParserCreate
from urllib import request

class CitySaxHandler(object):
    def __init__(self):
        self.city = None
        self.forecast = []

    def start_element(self, name, attrs):

        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if 'city' in attrs:
            self.city = attrs['city']
        if name == "yweather:forecast":
            date = attrs["date"]
            high = attrs["high"]
            low = attrs["low"]
            weatherdate = {'date': date, 'high': high, 'low': low}
            self.forecast.append(weatherdate)
        pass
    def end_element(self, name):
        print('sax:end_element: %s' % name)
        pass
    def char_data(self, text):
        print('sax:char_data: %s' % text)
        pass

def parseXml(xml_str):
    handler = CitySaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    print(xml_str)
    return {
        'city': handler.city,
        'forecast': handler.forecast
    }
# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print (result['forecast'])