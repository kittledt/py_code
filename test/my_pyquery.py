from pyquery import PyQuery as pq

doc = pq(url='https://www.python.org/events/python-events/')

title = list(doc('.event-title').items())
time = list(doc('time').items())
location = list(doc('.event-location').items())

i = 0
for i in range(len(title)):
    print('会议: %s，\n会议时间：%s,\t会议地点：%s\n' % (title[i].text(), time[i].text(), location[i].text()))