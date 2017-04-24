import numpy as np


def softmax(z):
    scoreMatExp = np.exp(np.asarray(z))
    return scoreMatExp / scoreMatExp.sum(0)



inputs=[[0.07, 0.22, 0.28],[0.35,0.78, 1.12],[-0.33, -0.58, -0.92],[-0.39, -0.7, -1.1]]
scores = [3.0, 1.0, 0.2]
print(softmax(inputs))