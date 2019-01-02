# -*- coding: utf-8 -*-

import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())




import  random


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {}

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

def register(username, password):
    db[username] = User(username, password)
    return True

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

assert register('michael', '123456')
assert register('bob', 'abc999')
assert register('alice', 'alice2008')
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
print(db)

for k,v  in db.items():
    print('{key}:{value}'.format(key=k, value=v))
