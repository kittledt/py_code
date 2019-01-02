import requests

r = requests.get('https://www.douban.com/',timeout=2.) # 豆瓣首页
print(r.status_code)


print(r.text) # text属性是string

#对于带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# 实际请求的URL  'https://www.douban.com/search?q=python&cat=1001'

print(r.url)
print(r.encoding)
print(r.content)    # text属性是bytes

import json
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
js = r.json()
print(js)
#d = json.load(js)
#print(type(d))

# add header
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

#post
print('start post ...')
r = requests.post('https://accounts.douban.com/login',data={'form_email': 'abc@example.com', 'form_password': '123456'})
