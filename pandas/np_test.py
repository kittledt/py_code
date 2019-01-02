import numpy as np
import matplotlib.pyplot as plt
import random
'''
通过位置匹配参数
'{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'
'''
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))

values = 1, 2, 3, 4, 5
a, b, *rest = values
c, d, *_ =values

print(a,b)
print(rest)
print(type(rest))
print(_)


seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[3:4]
print(seq[3:4])

x = np.arange(-2,2)
y = np.arange(0,3)#生成一位数组，其实也就是向量

z,s = np.meshgrid(x,y)#将两个一维数组变为二维矩阵
print(z)
print(s)

points = np.arange(-5, 5, 0.01) # 1000
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()


xvalues = np.array([0, 1, 2, 3, 4])
yvalues = np.array([0, 1, 2, 3, 4])

xx, yy = np.meshgrid(xvalues, yvalues)

plt.plot(xx, yy, marker='.', color='k', linestyle='none')
plt.show()

print(xx)
print(xx.sum(axis=0))
print(xx.mean(axis=1))


arr = np.random.randn(5)
print(arr)
print((arr>0).sum())


#

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
print(walk)

plt.plot(walk[:100])
plt.show()

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
print(draws)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

print(walk.min())
print(walk.max())
print((np.abs(walk) >= 10).argmax())

plt.plot(walk[:100])
plt.show()

#同时随即漫步 5000次


nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))   # 0 or 1
steps = np.where(draws > 0, 1, -1)                       #-1 or 1
walks = steps.cumsum(1)

hits30 = (np.abs(walks) >= 30).any(1)    #5000次，哪一次超过+-30，超过了是true
print(hits30)
print(hits30.sum()) # Number that hit 30 or -30