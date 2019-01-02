__author__ = 'rocky'
import zipfile

filename="bb.zip"

dictFile="pwdict.txt"

password=open(dictFile,'r')
zf = zipfile.ZipFile(filename)

for p in password:
    p=p.strip('\n')
    try:
        zf.extractall(path="./sample",pwd=p)
        print ("crash. Password is %s" %p)
        exit(0)
    except:
        pass



