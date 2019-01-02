import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

import os

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

#model : 返回预测结果值
def model(X, theta):
    return sigmoid(np.dot(X, theta.T))

#cost : 根据参数计算损失
def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    right = np.multiply(1 - y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / (len(X))


def gradient(X, y, theta):
    grad = np.zeros(theta.shape)  # （1,3）
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):  # for each parmeter
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)

    return grad

path =  '.\LogiReg_data.csv'
pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
print(pdData.head())

positive = pdData[pdData['Admitted'] == 1] # returns the subset of rows such Admitted = 1, i.e. the set of *positive* examples
negative = pdData[pdData['Admitted'] == 0] # returns the subset of rows such Admitted = 0, i.e. the set of *negative* examples

print(positive)
print(negative)

fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')

plt.show()

nums = np.arange(-10, 10, step=1) #creates a vector containing 20 equally spaced values from -10 to 10
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(nums, sigmoid(nums), 'r')

plt.show()


pdData.insert(0, 'Ones', 1) # in a try / except structure so as not to return an error if the block si executed several times
# set X (training data) and y (target variable)
orig_data = pdData.as_matrix() # convert the Pandas seful for further computations
print(orig_data)


cols = 4
X = orig_data[:,0:cols-1]
y = orig_data[:,cols-1:cols]
print(X)
print(y)

# convert to numpy arrays and initalize the parameter array theta
#X = np.matrix(X.values)
#y = np.matrix(data.iloc[:,3:4].values) #np.array(y.values)
theta = np.zeros([1, 3])
print(theta)