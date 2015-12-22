# coding=utf-8
import numpy as np
import struct
import matplotlib.pyplot as plt

a=[1,2,3,4,5,6,7,8,9,10]
a=np.array(a)
b=a.reshape(2,5)
c=a.reshape(5,2)
print b
print c
#文件路径
filename = 'train-images.idx3-ubyte'
#打开文件
binfile = open(filename , 'rb')
#读入缓存
buf = binfile.read()
index = 0
magic, numImages , numRows , numColumns = struct.unpack_from('>IIII' , buf , index)
index += struct.calcsize('>IIII')

numbers =1
shape = 28
allCount = shape * shape * numbers
b = '>' + bytes(allCount) + 'B'
im = struct.unpack_from(b, buf, index)

im = np.array(im)
imb = im.reshape(28,allCount/28)
ig = plt.figure(figsize=(60,60))
plt.imshow(imb , cmap='gray')
plt.show()


#文件路径
filename = 'train-Labels.idx1-ubyte'
#打开文件
labelFile = open(filename , 'rb')
#读入缓存
buf = labelFile.read()



