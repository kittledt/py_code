import os

print(os.name)                #'posix' , 'nt'
print(os.environ.get('PATH'))
os.path.abspath('.')              #current absolute dir

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
s =  os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'

s =  os.path.join(os.path.abspath('.'), 'testdir')
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

[x for x in os.listdir('.') if os.path.isdir(x)]

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']