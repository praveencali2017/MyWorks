import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
hidden_layer_num=5
number_of_iteration=1500
cost_history=np.ones([number_of_iteration])
def sliceDataForMining(data, training_per=0.6, validation_per=0.2, test_per=0.2):
    # random.seed(10)
    temp=data
    stage1=int(len(temp) * training_per)
    stage2=int(len(temp) * validation_per)
    stage3=int(len(temp))
    # random.shuffle(temp, random.random)
    training_data = temp[0:stage1,:]
    validation_data=temp[stage1:stage1+stage2, :]
    test_data=temp[stage1+stage2:stage3,:]
    return training_data, validation_data, test_data

def normalise(X):
    features=np.asmatrix(X).shape[1]
    means=np.ones((1,features))
    stdivs=np.ones((1,features))
    X_norm=X
    for i in range(0,features):
        means[0,i] =np.mean(X_norm[:,i])
        stdivs[0,i]=np.std(X_norm[:,i])
        X_norm[:,i]=((X_norm[:,i]-means[0,i])/stdivs[0,i])
    return X_norm,means,stdivs
def forward(X,weights):
    hypothesis=np.dot(X,weights)
    return applyactivation(hypothesis)
def errorestimation(X,y):
    errors=X-y
    return errors
def applyactivation(X):
    return 1/(1+np.exp(-X))
def initialise_weights(m,n):
    global W_ij, W_jk
    W_ij = np.zeros((m, n))
    W_ij[:,0]=-1
    W_jk = np.zeros((m,1))
    W_jk [0,0]=-1

def calculatecost(targets,outputs):
    J=0.5*sum(np.square(targets-outputs))
    return np.asscalar(J)

def updateWeights(alpha,W_ij,W_jk):
    samples = np.asmatrix(X_inputs).shape[0]
    W_ij = W_ij - np.transpose((alpha / samples) * np.transpose((X_inputs * W_ij) - T_target) * X_inputs)
    W_jk=W_jk - (alpha / samples) *np.transpose(np.transpose((X_inputs * W_jk) - T_target)*X_inputs)
    cost_history.append(calculatecost(T_target,(X_inputs*W_jk)))
    return W_ij,W_jk

def createPattern(W_ij,W_jk,alpha,iterations):
   for i in range(0,iterations):
    V_ij= forward(X_inputs,W_ij)
    V_ij = np.insert(V_ij,0,1,1)
    V_jk=forward(V_ij,W_jk)
    W_ij,W_jk=updateWeights(alpha, W_ij, W_jk)
   return  W_ij,W_jk
# read data
data=pd.read_csv('D:\machinelearning_datasets\\airfoil_self_noise.dat',sep='\t', header=None)
dataFrame=pd.DataFrame(data)
cost_history=[]
data_mat=np.asmatrix(dataFrame)
global training_data, validation_data, test_data
training_data,validation_data,test_data=sliceDataForMining(data_mat)
X_inputs,means,stdivs=normalise(training_data[:,:-1])
# plt.plot(X_inputs,training_data[:,-1],'x')
X_inputs=np.insert(X_inputs,0,1,1)
m=np.asmatrix(X_inputs).shape[1]
initialise_weights(m,m-1)
T_target=training_data[:,-1]
W_ij,W_jk=createPattern(W_ij,W_jk,0.01,number_of_iteration)
plt.plot(range(0,number_of_iteration),cost_history,'r--')
plt.show()

#From 902
#Validation Fit
validation_fit=validation_data[:,:-1]
validation_fit=(validation_fit-means)/stdivs
validation_fit=np.insert(validation_fit,0,1,1)
print("predicted sound pressures level for validation data---->")
print(validation_fit*W_jk)


###Testing
Test=np.asmatrix([6300,15.6,0.1016,39.6,0.0528487])
# print(validation_data[:,:])
Test=(Test-means)/stdivs
Test=np.insert(Test,0,1,1)
print('predicted sound pressure level--->{} dB'.format(np.asscalar(Test*W_jk)))
# plt.plot(validation_data[:,-1],Test*W_jk,'-')
# plt.show()









