# coding=utf-8
"""
============================
Nearest Neighbors regression
============================

Demonstrate the resolution of a regression problem
using a k-Nearest Neighbor and the interpolation of the
target using both barycenter and constant weights.

"""
import gzip
import cPickle

print(__doc__)

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
# Fabian Pedregosa <fabian.pedregosa@inria.fr>
#
# License: BSD 3 clause (C) INRIA


###############################################################################
# Generate sample data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
#打开mnist手写字符集。
f = gzip.open('mnist.pkl.gz', 'rb')
training_data, validation_data, test_data = cPickle.load(f)
f.close()
#获得训练数据
data = training_data[0][0:6000]
#获得训练结果
training_result = training_data[1][0:6000]
#获得用于测试的数据
test = test_data[0][0:100]
#获得用于测试的数据结果
test_result = test_data[1][0:100]
print 'load over'
###############################################################################
# Fit regression model
n_neighbors = 5
knn = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
fit = knn.fit(data, training_result)

print 'fit over'
y_ = fit.predict(test)
print y_
print  test_result
count =0
for x,y in zip(y_,test_result):
    if(x!=y):
        count+=1
print "{0}/{1}".format(count,len(y_))









