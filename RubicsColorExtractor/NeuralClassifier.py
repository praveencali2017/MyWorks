import numpy as np
from numpy import random
import matplotlib.pyplot as plot
class Neuralnetwork:
    noOfInputNodes=3
    noOfHiddenNodes=3
    noOfOutputNodes=6
    learning_rate=0.01
    colorsdict={0:'Red', 1:'Green', 2:'Blue', 3:'Yellow', 4: 'Orange', 5:'White'}
    weights1=random.random((noOfInputNodes+1,3))
    weights2=random.random((noOfHiddenNodes+1,6))
    def forwardTrace(self, inputs,targets,finalrun=False):
        self.inputs=inputs
        self.inputs=np.asmatrix(inputs)
        self.inputs=np.insert(self.inputs,0,1,1)
        self.z2=self.inputs*self.weights1
        self.a2= self.softmax(self.z2)
        self.a2=np.insert(self.a2,0,1,1)
        self.z3=self.a2*self.weights2
        self.a3=self.softmax(self.z3)
        if not finalrun:
            self.updateWeights(self.a3,targets)
        else:
            return self.getPredictions(self.a3)
    def softmax(self, z):
        scoreMatExp = np.exp(np.asarray(z))
        return scoreMatExp / scoreMatExp.sum(0)
    def sigmoid(self,z):
        return  1 / (1 + np.exp(-z))
    def computeCost(self,outputs,targets):
        m=outputs.shape[0]
        cost=(sum(self.computeCrossEntropy(outputs,targets)))/m
        return cost
    def computeCrossEntropy(self,outputs,target):
        entropy=-1*(sum(np.asarray(np.multiply(target,np.log(np.asmatrix(outputs))))))
        return entropy
    def updateWeights(self,outputs,targets):
        m=outputs.shape[0]
        delta3=np.multiply(-1,(outputs-targets)),self.primeSigmoid(self.z3)
        self.weights2=self.weights2-(self.learning_rate*np.dot(np.transpose(self.a2),delta3))
        weight_rmbias=self.weights2.T[:,1:self.weights2.shape[1]]
        delta2=np.multiply(np.dot(delta3,weight_rmbias),self.primeSigmoid(self.z2))
        self.weights1=self.weights1-(self.learning_rate*np.dot(self.inputs.T,delta2))
    def primeSigmoid(self,z):
        return np.multiply(self.sigmoid(z),(1-self.sigmoid(z)))

    def trainModel(self,learning_rate, iterations,inputs, targets):
        self.learning_rate=learning_rate
        cost=[]
        for i in range(0,iterations):
            self.forwardTrace(inputs, targets)
            cost.append(self.computeCost(self.a3,targets))
        plot.plot(range(0,iterations),cost)
        plot.ylabel("Cost")
        plot.xlabel("iterations")
        plot.show()
        print(cost)
        return self.forwardTrace(inputs,targets,True)
    def getPredictions(self,outputs):
        # return outputs
        return outputs

