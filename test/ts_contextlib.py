from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name
        print('init name = %s' %name)

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()



'''
import urllib, sys
from contextlib import closing

with closing(urllib.urlopen('http://www.yahoo.com')) as f:
    for line in f:
        sys.stdout.write(line)
'''

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

'''
可以的，这个用爬去http的可以的，如果要爬去https的需要导入ssl
然后设置context=ssl._create_unverified_context()
具体代码是下面这样的：
'''

from contextlib import closing
from urllib.request import urlopen
import ssl

with closing(urlopen('https://www.python.org',context=ssl._create_unverified_context())) as page:
    for line in page:
        print(line)