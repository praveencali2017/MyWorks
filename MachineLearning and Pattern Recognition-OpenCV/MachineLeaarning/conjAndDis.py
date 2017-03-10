import numpy as np
from astropy.table import Table
columnStr=[]
def checkThreshold(val):
    #And operation every inputs has to be one
    if choice == 1:
        for x in range(0,noOfItems):
            evaluateCaseConjunction(tabular[x,:])
    elif choice == 2:
        for x in range(0, noOfItems):
            evaluateCaseDisjunction(tabular[x,:])
def evaluateCaseConjunction(val):
    if len(val)-1 == sum(val):
        val[-1]=1

def evaluateCaseDisjunction(val):
    if sum(val)>=1:
        val[-1]=1
def generateColumnStr():
    for x in range(0, noOfItems):
        columnStr.append("I"+str(x+1))


choice=int(input("Enter Your Choice 1 for Conjunction and 2 for Disjunction\n"))
noOfInputs= int(input("Enter input size\n"))
noOfItems=int(input("Enter number of items\n"))
print("Start entering your inputs")
tabular=np.zeros((noOfItems,noOfInputs+1))
for x in range(0,noOfItems):
    print("Enter your items for row:{0}\n".format(x))
    for y in range(0, noOfInputs):
        tabular[x][y]=input("?")
checkThreshold(tabular)
generateColumnStr()
columnStr.append("O")
table=Table(tabular,names=columnStr)
print(table)


