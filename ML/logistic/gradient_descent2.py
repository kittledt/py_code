#coding=utf-8

import numpy as np
import random
from numpy import genfromtxt
import pandas as pd

def getData(dataSet):
    m, n = np.shape(dataSet)
    trainData = np.ones((m, n))
    trainData[:,:-1] = dataSet[:,:-1]   #第三列不复制，仍然是初始化的1
    trainLabel = dataSet[:,-1]
    return trainData, trainLabel
'''
https://www.cnblogs.com/pinard/p/5970503.html

h(x) = Xθ

θ=θ−αXT(Xθ−Y)

'''


def batchGradientDescent(x, y, theta, alpha, m, maxIterations):
    xTrains = x.transpose()
    for i in range(0, maxIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        # print loss
        gradient = np.dot(xTrains, loss) / m
        theta = theta - alpha * gradient
    return theta

def predict(x, theta):
    m, n = np.shape(x)
    xTest = np.ones((m, n+1))
    xTest[:, :-1] = x
    yP = np.dot(xTest, theta)
    return yP

dataPath = './house1.csv'
dataSet = genfromtxt(dataPath, delimiter=',')
#df =  pd.read_csv(dataPath)
trainData, trainLabel = getData(dataSet)
m, n = np.shape(trainData)
theta = np.ones(n)
alpha = 0.1
maxIteration = 5000
#x为自变量训练集，y为自变量对应的因变量训练集；theta为待求解的权重值，需要事先进行初始化；alpha是学习率；m为样本总数；maxIterations为最大迭代次数
#在原有自变量的基础上，需要主观添加一个均为1的偏移量，即公式中的x0。原始数据的前n-1列再加上添加的偏移量组成自变量trainData，最后一列为因变量trainLabel
theta = batchGradientDescent(trainData, trainLabel, theta, alpha, m, maxIteration)

#解出theta ，新来一个test 集合，做预测
'''

[3.1, 5.5，9.5], 
[3.3, 5.9,10.2], 
[3.5, 6.3,10.9], 
[3.7, 6.7,11.6], 
[3.9, 7.1,12.3]

'''
x = np.array([[3.1, 5.5], [3.3, 5.9], [3.5, 6.3], [3.7, 6.7], [3.9, 7.1]])
print( predict(x, theta))