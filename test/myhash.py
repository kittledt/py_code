# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('abc999'.encode('utf-8'))
print(md5.hexdigest())
md5.update('abc999bobthe-Salt'.encode('utf-8'))
print(md5.hexdigest())



sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
'''
name	password
michael	123456
bob	    abc999
alice	alice2008

username	password
michael	    e10adc3949ba59abbe56e057f20f883e
bob	        878ef96e86145580c38c87f0410ad153
alice	    99b1c2188db85afee403b1536010c2c9

'''

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def calc_md5(password):
    pwd = hashlib.md5()
    pwd.update(password.encode('utf-8'))
    return md5.hexdigest()

def login(user, password):
    pwd_md5 = calc_md5(password)
    if pwd_md5 == db[user]:
        print('user %s pass' %user)
        return True
    else:
        print('user %s fail' %user)
        return False

#------------------------
#  add salt
db_salt = {}

def register(user, password):
    pwd = calc_md5(password  + user+'the-Salt')
    db_salt[user] = pwd
    pass

def login_salt(user, password):
    pwd_md5 = calc_md5(password)
    if pwd_md5 == db_salt[user]:
        print('user %s pass' %user)
        return True
    else:
        print('user %s fail' %user)
        return False

def main():
    login('bob','abc999')
    register('bob','abc999')
    login_salt('bob','abc999')

if __name__ == '__main__':
    main()