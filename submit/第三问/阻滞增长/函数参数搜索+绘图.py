import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

x = pd.read_csv("data3_接受距离.csv", header=None)
x = x.values

y = pd.read_csv("data3_热风速度.csv", header=None)
y = y.values

myx = np.zeros([2, 25])
myx[0] = x.flatten() / 10
myx[1] = y.flatten() / 1000

z = pd.read_csv("data3求平均.csv", header=None)
z = z.values
myz = z[:, 4]
myz = myz.flatten()


def fun(X, k1, k2, k3, k4):
    x = X[0, :]
    y = X[1, :]
    return 25 / (1 + 1.5 * np.exp(-k1 * x)) + 25 / (1 + 1.5 * np.exp(-k2 * y)) + 50 / (
            1 + 1.5 * np.exp(-k3 * x - k4 * y))


init = [15.9, 3.281, -5.605, 10.77]
# init = [[15.9, 2.29426109, -3.9162163, 6.95940933]]
popt, pcov = curve_fit(fun, myx, myz, p0=init)

print(popt)

y2 = np.zeros([25])
k1 = popt[0]
k2 = popt[1]
k3 = popt[2]
k4 = popt[3]

for i in range(25):
    x = myx[0, i]
    y = myx[1, i]
    y2[i] = 25 / (1 + 1.5 * np.exp(-k1 * x)) + 25 / (1 + 1.5 * np.exp(-k2 * y)) + 50 / (
            1 + 1.5 * np.exp(-k3 * x - k4 * y))


# #################################拟合优度R^2的计算######################################
def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list = [(y - y_mean) ** 2 for y in y_no_fitting]
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
    s_list = [(y - y_mean) ** 2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i]) ** 2 for i in range(len(y_fitting))]
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
    rr = SSR / SST
    return rr


print(goodness_of_fit(y2, myz))
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
ax = plt.axes(projection="3d")

plotx = np.arange(start=0, stop=100, step=1)
ploty = np.arange(start=0, stop=2000, step=20)
plotx = plotx.reshape([-1, 1])

Z = 25 / (1 + 1.5 * np.exp(-k1 * plotx/10)) + 25 / (1 + 1.5 * np.exp(-k2 * ploty/1000)) + 50 / (
        1 + 1.5 * np.exp(-k3 * plotx/10 - k4 * ploty/1000))

ax.plot_surface(plotx,ploty,Z,alpha=0.8, cstride=1, rstride = 1, cmap='rainbow')
ax.scatter(myx[0]*10,myx[1]*1000,myz,marker='.',c='black')

ax.set_zlabel('过滤效率（%）',fontsize=13)
ax.view_init(20, -100)
plt.xlabel('接收距离(cm)',fontsize=13)
plt.ylabel('热风速度(r/min)',fontsize=13)
plt.show()
