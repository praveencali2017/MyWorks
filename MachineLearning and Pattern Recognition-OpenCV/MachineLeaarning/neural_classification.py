import sklearn as sk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
from random import shuffle

def sigmoid(x):
    return 1/(1+np.exp(-x))
def softmax(w):
    e_x = np.exp(w - np.max(w))
    return e_x / e_x.sum(axis=0)
# load data
target_data=[]
def sliceDataForMining(data, training_per=0.6, validation_per=0.2, test_per=0.2):
    random.seed(10)
    temp=data
    stage1=int(len(temp) * training_per)
    stage2=int(len(temp) * validation_per)
    stage3=int(len(temp))
    random.shuffle(temp, random.random)
    # print(temp)
    training_data = temp[0:stage1,:]
    validation_data=temp[stage1:stage1+stage2, :]
    test_data=temp[stage1+stage2:stage3,:]
    target_data.append(temp[:,-1])
    return training_data, validation_data, test_data

data_filename='iris.data'
root_path='D:\machinelearning_datasets\iris\\'
iris_data= pd.read_csv(root_path+data_filename)
features=['sepal-length','sepal-width','petal-length','petal-width','class']
targets_names={'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2}

# print(targets.keys())
data_array=np.asarray(iris_data)
targets=np.transpose(data_array[:,4])
#feeding data slices for training, validation and test
training_data, validation_data, test_data= sliceDataForMining(data_array)
# w_jo=np.asmatrix([5.215,5.215,5.215,5.215,5.215])
features=np.asmatrix(training_data[:,0:4])
features_bias=np.insert(features,0,-1,axis=1)
print(features_bias.shape)
w_ij=np.ones((features_bias.shape[1],features_bias.shape[1]-1))
w_ij=w_ij*5.215
w_jo=np.ones((5,1))*5.215
# print(w_jo)
print(w_ij.shape)
A=np.dot(np.asmatrix(features_bias),w_ij)
print(A.shape)
A_bias=np.insert(A,0,-1,axis=1)
print(A_bias.shape)
Z= np.dot(A_bias,w_jo)
# print(Z)
target_data=np.transpose(np.asmatrix(target_data))
for key in targets_names:
    target_data[target_data==key]=targets_names.get(key)
Afunc=softmax(np.asarray(Z,dtype=np.float64))
print(Afunc)
# plt.scatter(target_data[0:89,:],y="target")
plt.plot(target_data,'o')
plt.plot(Afunc)
plt.show()
