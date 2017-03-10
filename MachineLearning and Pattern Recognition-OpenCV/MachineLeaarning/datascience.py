import numpy as np
import matplotlib.pyplot as plt
inputs=np.asmatrix([[1,2],[1,4],[1,5],[1,6],[1,7],[1,8]])
target=[5,9,11,13,15,17]
coe=np.asmatrix([[1.5,1.5],[1.9,1.9]])
multiply=np.dot(inputs,coe)
plt.plot(inputs[:,1],target)
plt.scatter(inputs[:,1],multiply[:,1],c='r')
plt.xlabel('target')
plt.ylabel('predicted')
plt.title("Predictor")
plt.legend()
plt.show()



