import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def obj(X):
    x = X[0]
    y = X[1]
    k1 = 15.9
    k2 = 3.27944218
    k3 = -5.60411769
    k4 = 10.76586634
    return -(25 / (1 + 1.5 * np.exp(-k1 * x / 10)) + 25 / (1 + 1.5 * np.exp(-k2 * y / 1000)) + 50 / (
            1 + 1.5 * np.exp(-k3 * x / 10 - k4 * y / 1000)))
X=np.zeros([29,2])
X[0,0]=10
X[0,1]=1000
for i in range(28):
    data=pd.read_csv("中间结果"+str(i)+".csv",header=None)
    X[i+1,:]=data.values.flatten()

Y=np.zeros([29,1])

for i in range(29):
    Y[i,0]=obj(X[i,:])
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
idx=np.arange(29)
plt.plot(idx,-Y,marker='.')
plt.xlabel('迭代次数(次)',fontsize=13)
plt.ylabel('过滤效率(%)',fontsize=13)
plt.show()

