import numpy as np
import matplotlib.pyplot as plt
'''


面积(m^2)	销售价钱（万元）
123	            250
150	            320
87	            180
'''
'''
y=2 * (x1) + (x2) + 3
也就是求解:
y=ax1+bx2+c

中的a，b，c三个参数 。
'''
# 这里rate 代表学习率，表示每次向着J最陡峭的方向迈步的大小
rate = 0.001
x_train = np.array([    [1, 2],    [2, 1],    [2, 3],    [3, 5],    [1, 3],    [4, 2],    [7, 3],    [4, 5],    [11, 3],    [8, 7]    ])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
x_test  = np.array([    [1, 4],    [2, 2],    [2, 5],    [5, 3],    [1, 5],    [4, 1]    ])
#我们随机初始化weigths，然后不断反复的更新weights使得误差函数减小，直到满足要求时停止。这里更新算法我们选择梯度下降算法，利用初始化的weights并且反复更新weights：
a = np.random.normal()
b = np.random.normal()
c = np.random.normal()

def h(x):
    return a*x[0]+b*x[1]+c

for i in range(500):
    sum_a=0
    sum_b=0
    sum_c=0
    for x, y in zip(x_train, y_train):
        sum_a = sum_a + rate*(y-h(x))*x[0]
        sum_b = sum_b + rate*(y-h(x))*x[1]
        sum_c = sum_c + rate*(y-h(x))
    a = a + sum_a
    b = b + sum_b
    c = c + sum_c
    plt.plot([h(xi) for xi in x_test])

print(a)
print(b)
print(c)

result=[h(xi) for xi in x_train]
print(result)

result=[h(xi) for xi in x_test]
print(result)

plt.show()