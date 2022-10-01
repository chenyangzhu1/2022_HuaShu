import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def obj(X):
    x = X[0]
    y = X[1]
    zuli = 4.05950528e+01 + 8.46631161e-01 * x - \
           1.93679792e-02 * y - 2.29699455e-02 * x ** 2 \
           + 1.36511669e-04 * x * y
    zuli /= 36.47

    k1 = 15.9
    k2 = 3.27944218
    k3 = -5.60411769
    k4 = 10.76586634
    xiaolv = 25 / (1 + 1.5 * np.exp(-k1 * x / 10)) \
             + 25 / (1 + 1.5 * np.exp(-k2 * y / 1000)) \
             + 50 / (1 + 1.5 * np.exp(-k3 * x / 10 - k4 * y / 1000))

    xiaolv /= 82.98

    return zuli,xiaolv

X=np.zeros([20,2])
X[0,0]=18
X[0,1]=890

for i in range(19):
    data=pd.read_csv("中间结果"+str(i)+".csv",header=None)
    X[i+1,:]=data.values.flatten()


Zuli=np.zeros([20,1])
Xiaolv=np.zeros([20,1])
for i in range(20):
    Zuli[i,:],Xiaolv[i,:]=obj(X[i,:])


plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

idx=np.arange(20)

plt.plot(idx,Zuli*36.47,marker='.')

plt.xlabel('迭代次数(次)',fontsize=13)
plt.ylabel('过滤阻力Pa',fontsize=13)
plt.show()

plt.plot(idx,Xiaolv*82.98,marker='.')
plt.xlabel('迭代次数(次)',fontsize=13)
plt.ylabel('过滤效率（%）',fontsize=13)
plt.show()
