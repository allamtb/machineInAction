from PIL import Image
from numpy import *
from numpy import linalg as la

from svd import svdRec

image_open = Image.open("test.jpg")
ndarray = array(image_open)
mean_X = ndarray.mean(axis=0)
X = ndarray - mean_X

U,Sigma,VT = la.svd(X)
arange()
SigRecon = mat(zeros((3, 3), dtype='object'))
for k in range(3):#construct diagonal matrix from vector
    SigRecon[k,k] = Sigma[k]
reconMat = U[:,:3]*SigRecon*VT[:3,:]

fromarray = Image.fromarray(reconMat)

fromarray.save('svdAfter.JPG')

