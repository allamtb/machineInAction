# coding=utf-8
import struct
import numpy as np


#文件路径
filename = 'train-images.idx3-ubyte'
#打开文件
binfile = open(filename , 'rb')
#读入缓存
buf = binfile.read()

#文件路径
trainLabels = 'train-labels.idx1-ubyte'
#打开文件
labelFile = open(trainLabels , 'rb')
#读入缓存
labBuf = labelFile.read()

dataList = []
for i in range(6000):

    dataStep =28*28
    index = 16+(i * dataStep)
    b = '>' + bytes(dataStep*dataStep) + 'B'
    data = struct.unpack_from(b, buf, index)

    labelStep = 1
    labelIndex = 8+(i * labelStep)
    label = struct.unpack_from('>' + bytes(labelStep) + 'B', labBuf, labelIndex)

    dataPair = data,label

    dataList.append(dataPair)

im = np.array(dataList)
print np.shape(dataList)





