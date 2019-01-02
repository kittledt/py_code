

from datetime import datetime,timedelta
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))


dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
ts = dt.timestamp()
print(ts)  # 把datetime转换为timestamp
print(datetime.fromtimestamp(ts))      #Beijing  time
print(datetime.utcfromtimestamp(ts))    #UTC Landon time

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

#
import struct
print(struct.pack('>I', 10240099))

print (struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

#bmp file
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
t = struct.unpack('<ccIIIIIIHH', s)
print (t)



