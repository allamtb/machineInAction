# coding=utf-8
from numpy import *
import data.svdData as svdData
import svdRec

#svd原理
def svdPrincple():
    data = svdData.loadData()
    print '原始数据'
    print data
    U, Sigma, VT = linalg.svd(data)
    #取平方是为了避免正负数干扰结果。
    sigma_2 = Sigma ** 2
    #sigma的能量和
    print sum(sigma_2)
    #前三个的能量和
    print(sum(Sigma[:3]**2))
    # 观察 Sigma后，取得有效的前三位。
    sig3 = mat([
        [Sigma[0], 0, 0],
        [0, Sigma[1], 0],
        [0, 0, Sigma[2]]
    ])
    print 'U等于'
    print U
    print 'U：3等于获取所有行,列取到3列'
    print U[:, :3]
    print '最终矩阵'
    print U[:, :3] * sig3 * VT[:3, :]


def recommendApp():
    global data
    data = mat(svdData.loadData2())
    recommend = svdRec.recommend(data, 2)
    print recommend
    recommend = svdRec.recommend(data, 2,simMeas=svdRec.ecludSim)
    print recommend
    recommend = svdRec.recommend(data, 2,simMeas=svdRec.pearsSim)
    print recommend




#图像压缩  ---用真实图像实验下。
#svdRec.imgCompress(2)

#svd原理
svdPrincple()










