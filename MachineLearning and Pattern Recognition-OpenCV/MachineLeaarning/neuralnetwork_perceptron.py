import numpy as np;
import matplotlib.pyplot as plot
#building neurons
# x=(1,1)
# weights=(1,1)
# bias=-1.5
# z=np.dot(x,weights)
# add_bias=np.add(z,bias)
# print(z)
# print(add_bias)
#Class Assignment Testing
inputs=[1,0,1]
inputs_bias=np.asmatrix([-1,1,0,1])
W_hidden=np.asmatrix(([0,1,1],[1,2,2],[2,3,1],[3,4,2]))
# print(W_hidden)
# print(np.transpose(inputs))
Z=np.dot(inputs_bias,W_hidden)
# add_bias=np.insert(Z,0,-1)
np.place(Z,Z<=4,0)
np.place(Z,Z>4,1)
res=np.asarray(Z).flatten()
print(inputs)
print(res)
plot.xlim([-1,1])
plot.ylim([-1,1])
plot.step(inputs,res)
plot.show()
# print(add_bias)
# W_output=np.asmatrix(([1,0,1],[5,5,4],[3,3,5],[4,4,3]))
# print(W_output)
# final_res=np.dot(add_bias,W_output)
#
# print(final_res)

