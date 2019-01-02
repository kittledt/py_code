# -*- coding: utf-8 -*-
import itertools


'''   计算pi的值 
    def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
    
    return 3.14
'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

natuals = itertools.count(1, 2)
ns = itertools.takewhile(lambda x: x <= (2 * 10 - 1), natuals)
print(list(ns))

def pi(n):
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda x: x <= (2 * n-1), natuals)
    L = list(ns)
    L1 = [pow(-1, i) * (4.0 / L[i]) for i in range(len(L))]

    return sum(L1)


def main():
    print(pi(100000))

if __name__=='__main__':
    main()

