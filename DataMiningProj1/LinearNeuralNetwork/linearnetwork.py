from terminaltables import AsciiTable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Number of iterations for epoch
number_of_iteration=800
#Learning rate
alpha=0.01
#Initialising cost array
cost_history=np.ones([number_of_iteration])

'''
Inputs: data (data), slices needed for training (training_per), validation (validation_per) and test (test_per)
Functionality: Slices out the given data into Training, Validation and Testing
Returns: Array of sliced data (training_data, validation_data, test_data)
'''
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

'''
Inputs: Features (X)
Functionality: Normalise the given values for each feature
Returns: Normalised values with mean (means) and standard deviation (stdivs) for each feature
'''

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

'''
Inputs: Features (X) and Weights (weights)
Functionality: performs hypothesis and calls sigmoid function
Returns: Values ranging from 0 to 1 for the given matrix
'''
def forward(X,weights):
    hypothesis=np.dot(X,weights)
    return applyactivation(hypothesis)


'''
Inputs: Hypothesis (X)
Functionality: Applies sigmoid function for the given matrix
Returns: Values ranging from 0 to 1 for the given matrix
'''
def applyactivation(X):
    return 1/(1+np.exp(-X))


'''
Inputs: Size row(m) and columns(n)
Functionality: Initialise the default weights for the layers
Returns: void
'''
def initialise_weights(m,n):
    global W_ij, W_jk
    W_ij = np.zeros((m, n))
    W_ij[:,0]=-1
    W_jk = np.zeros((m,1))
    W_jk [0,0]=-1

'''
Inputs: Target (targets) and Outputs (outputs)
Functionality: calculates the error cost
Returns: The calculated cost as scalar value (J)
'''
def calculatecost(targets,outputs):
    J=0.5*sum(np.square(targets-outputs))
    return np.asscalar(J)

'''
Inputs: Weights between layers(W_ij, W_jk)
        Learning rate (alpha)
Functionality: Updates weights for back propagation, while adding the updated costs
Returns: Updated Weights
'''
def updateWeights(alpha,W_ij,W_jk):
    samples = np.asmatrix(X_inputs).shape[0]
    W_ij = W_ij - np.transpose((alpha / samples) * np.transpose((X_inputs * W_ij) - T_target) * X_inputs)
    W_jk=W_jk - (alpha / samples) *np.transpose(np.transpose((X_inputs * W_jk) - T_target)*X_inputs)
    cost_history.append(calculatecost(T_target,(X_inputs*W_jk)))
    return W_ij,W_jk

'''Inputs: Weights between first and last layer(W_ij, W_jk)
           Learning rate(alpha)
           epoch (iterations)
   Functionality: Creates a pattern of forward and backward propagation
   Returns: Updated weights (W_ij, W_jk)'''
def createPattern(W_ij,W_jk,alpha,iterations):
   for i in range(0,iterations):
    V_ij= forward(X_inputs,W_ij)
    V_ij = np.insert(V_ij,0,1,1)
    V_jk=forward(V_ij,W_jk)
    W_ij,W_jk=updateWeights(alpha, W_ij, W_jk)
   return  W_ij,W_jk

# Read data, should change the path as desired
data=pd.read_csv('D:\machinelearning_datasets\\airfoil_self_noise.dat',sep='\t', header=None)
dataFrame=pd.DataFrame(data)
cost_history=[]
data_mat=np.asmatrix(dataFrame)
global training_data, validation_data, test_data
#Slice the given data into training, validation and testing
#(Options can even pass percentage of data to split by default it's 60,20,20)
training_data,validation_data,test_data=sliceDataForMining(data_mat)
#Normalising input variables
X_inputs,means,stdivs=normalise(training_data[:,:-1])
#Adding bias inputs
X_inputs=np.insert(X_inputs,0,1,1)
#Defining weights for the network
m=np.asmatrix(X_inputs).shape[1]
initialise_weights(m,m-1)
#Slicing out target variables from training data
T_target=training_data[:,-1]
#Create a pattern of forward and backward pass by updating weights for each epoch
W_ij,W_jk=createPattern(W_ij,W_jk,alpha,number_of_iteration)


#From 902
#Validation Fit
validation_fit=validation_data[:,:-1]
validation_fit=(validation_fit-means)/stdivs
validation_fit=np.insert(validation_fit,0,1,1)

#Printing Predicted and Target Values side by side
print("Predicted sound pressures levels for validation data---->")
targets_validation=validation_data[:,-1]
predicted_validation=validation_fit*W_jk
final_all=np.asmatrix(np.ones((targets_validation.shape[0],2)))
final_all[:,0]=targets_validation
final_all[:,1]=predicted_validation
final_all=np.asarray(final_all).tolist()

data_values=[['Target values in dB (Validation)','Predicted values in dB (Validation)']]
for i in range(1,len(final_all)):
    data_values.insert(i,final_all[i-1])
# print(data_values)
table=AsciiTable(data_values)
print(table.table)




###Testing
Test=np.asmatrix([6300,15.6,0.1016,39.6,0.0528487])
# print(validation_data[:,:])
Test=(Test-means)/stdivs
Test=np.insert(Test,0,1,1)
print('Predicted sound pressure level--->{} dB'.format(np.asscalar(Test*W_jk)))


#Plotting cost history for gradient descent
plt.title("Gradient Descent")
plt.plot(range(0,number_of_iteration),cost_history,'r--')
plt.xlabel("Epochs--------->")
plt.ylabel("J(Cost)-------->")
plt.show()







