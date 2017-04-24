from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
colorsdict={0:'Red', 1:'Green', 2:'Blue', 3:'Yellow', 4: 'Orange', 5:'White'}
data=pd.read_csv("D:\myworkspace\MyWorks\\test-color.csv")
inputs=np.asmatrix(data)[:,0:3]
targets=np.asarray(data)[:,-1]
X,Y = inputs, targets
"""Configuring Multilayer Perceptron"""
mlp = MLPClassifier()
# iterations=500
# mlp.early_stopping=True
mlp.learning_rate='adaptive'
mlp.fit(X, Y)

"""Plotting cost/gradient descent"""
plot.plot(range(0,len(mlp.loss_curve_)),mlp.loss_curve_)
plot.xlabel("iterations")
plot.ylabel("cost")
# plot.show()
"""Predicts H,S,V"""
# print mlp.best_validation_score_
print(colorsdict.get(np.asscalar(mlp.predict(np.asarray([0,0,100]).reshape(1, -1)))))
# print(mlp.predict(X))
# print(np.argmax(mlp.predict_proba(np.asarray([120,100,40]).reshape(1, -1)),axis=1))