import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
plt.rcParams['font.sans-serif'] = ['FangSong']

x = pd.read_csv("data3_接受距离.csv", header=None)
x = x.values

y = pd.read_csv("data3_热风速度.csv", header=None)
y = y.values

myx=np.zeros([2,25])
myx[0]=x.flatten()
myx[1]=y.flatten()

z = pd.read_csv("data3求平均.csv", header=None)
z = z.values
myz=z[:,0]
myz=myz.flatten()

# plt.plot(myx[0],myz,c='red')


def fun(x,k0,k1,k2):
    return k0*x[0,:]+k1*x[1,:]+k2

popt, pcov=curve_fit(fun, myx, myz)


y2=np.zeros([25])
for i in range(25):
    y2[i]=popt[0]*myx[0,i]+popt[1]*myx[1,i]+popt[2]

# plt.plot(myx[0],y2,c='blue')
# plt.show()
print(popt)



# #################################拟合优度R^2的计算######################################
def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_no_fitting]
    sst = sum(s_list)
    return sst


def __ssr(y_fitting, y_no_fitting):
    """
    计算SSR(regression sum of squares) 回归平方和
    :param y_fitting: List[int] or array[int]  拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 回归平方和SSR
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i])**2 for i in range(len(y_fitting))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fitting, y_no_fitting):
    """
    计算拟合优度R^2
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 拟合优度R^2
    """
    SSR = __ssr(y_fitting, y_no_fitting)
    SST = __sst(y_no_fitting)
    rr = SSR /SST
    return rr

print(goodness_of_fit(y2,myz))
# print(pcov)

p00=popt[0]
p10=popt[1]
p01=popt[2]
fig = plt.figure()
ax = plt.axes(projection="3d")

plotx=np.arange(start=20,stop=40,step=0.5)
ploty=np.arange(start=800,stop=1200,step=10)
plotx=plotx.reshape([-1,1])
# ploty=ploty.reshape([-1,1])
Z=popt[0]*plotx+popt[1]*ploty+popt[2]

ax.plot_surface(plotx,ploty,Z,alpha=0.8, cstride=1, rstride = 1, cmap='copper')

ax.scatter(myx[0],myx[1],myz,marker='.')



pre=pd.read_excel("pre.xlsx",header=None)
pre=pre.values

pre_results=np.zeros([8])
for i in range(8):
    x=pre[i,0]
    y=pre[i,1]
    pre_results[i]=popt[0]*x+popt[1]*y+popt[2]

ax.scatter(pre[:,0],pre[:,1],pre_results,marker='.',c='darkred')
ax.set_zlabel('厚度（mm）',fontsize=13)
# ax.view_init(0, 10)
plt.xlabel('接收距离(cm)',fontsize=13)
plt.ylabel('热风速度(r/min)',fontsize=13)
plt.show()


np.savetxt("厚度预测结果.csv",pre_results,delimiter=',')