#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
        self.h3_flag = False

    def _attrs(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        #print(attrs)
        if tag == 'h3' and  self._attrs(attrs, 'class') =="event-title":
            self.h3_flag = True
        if tag == 'time':
            print("会议时间：")
            self.flag = True
        if tag == 'span' and self._attrs(attrs, 'class') == 'event-location':
            print("会议地点：")
            self.flag = True


    def handle_endtag(self, tag):
        self.flag = False
        self.h3_flag = False
        #print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
        #print('<%s/>' % tag)
        pass

    def handle_data(self, data):
        if self.h3_flag == True and self.lasttag == 'a':
            print('会议名称：', data)
        if self.flag == True:
            print(data)


    def handle_comment(self, data):
        #print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        print('&%s:' % name)

    def handle_charref(self, name):
        print('&#%s:' % name)

parser = MyHTMLParser()
with open('html.txt', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

#use pyquery
from pyquery import PyQuery as pq

doc = pq(url='https://www.python.org/events/python-events/')

title = list(doc('.event-title').items())
time = list(doc('time').items())
location = list(doc('.event-location').items())

i = 0
for i in range(len(title)):
    print('会议: %s，\n会议时间：%s,\t会议地点：%s\n' % (title[i].text(), time[i].text(), location[i].text()))