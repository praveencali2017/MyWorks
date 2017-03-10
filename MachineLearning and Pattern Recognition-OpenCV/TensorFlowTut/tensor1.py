
import numpy as np
import tensorflow as tf
# x=tf.constant(35,name="x")
# y=tf.Variable(x+5,name="y")
#
# model=tf.initialize_all_variables()
#
# with tf.Session() as session:
#     session.run(model)
#     print(session.run(y))
# x = tf.constant([35, 40, 45], name='x')
# y = tf.Variable(x + 5, name='y')
#
#
# model = tf.initialize_all_variables()
#
# with tf.Session() as session:
# 	session.run(model)
# 	print(session.run(y))
#
# data=np.random.randint(1000,size=10000)
#
# x=tf.constant(data,name="x")
# y=tf.Variable(5*(x*x)-(3*x)+15, name="y")
#
# model = tf.initialize_all_variables()
#
# with tf.Session() as session:
# 	session.run(model)
# 	print(session.run(y))

a = tf.add(1, 2,)
b = tf.multiply(a, 3)
c = tf.add(4, 5,)
d = tf.multiply(c, 6,)
e = tf.multiply(4, 5,)
f = tf.div(c, 6,)
g = tf.add(b, d)
h = tf.multiply(g, f)

#with tf.Session() as sess:
#print(sess.run(h))
#tensorboard---------------pending will review tonight
with tf.Session() as sess:
	merger=tf.summary.merge_all()
	writer = tf.summary.FileWriter("/mypath/myfiles/output", sess.graph)
	model=tf.global_variables_initializer()
	sess.run(model)
	print(sess.run(h))