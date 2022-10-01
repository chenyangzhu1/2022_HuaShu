import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_excel("因子分析后两个指标.xlsx", header=None)

data = data.values

myx1 = data[:, 0]

myx2 = data[:, 1]

myX = np.zeros([3, 25])
myX[0, :] = myx1
myX[1, :] = myx2

target = pd.read_csv("data3求平均.csv", header=None)
target = target.values

my_y = target[:, 4]

myX[0, :] = target[:, 0]
myX[1, :] = target[:, 1]
myX[2, :] = target[:, 2]


def fun(X, p00, p10, p01, p20, p11, p31, p32, p33):
    x = X[0, :]
    y = X[1, :]
    z = X[2, :]
    return p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p31 * z + p32 * z + p33 * z


popt, pcov = curve_fit(fun, myX, my_y)

p00 = popt[0]
p10 = popt[1]
p01 = popt[2]
p20 = popt[3]
p11 = popt[4]
p31 = popt[5]
p32 = popt[6]
p33 = popt[7]
y2 = np.zeros([25])

for i in range(25):
    x = myX[0, i]
    y = myX[1, i]
    z = myX[2, i]
    y2[i]= p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p31 * z + p32 * z + p33 * z

print(popt)


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


print(goodness_of_fit(y2, my_y))

# fig = plt.figure()
# ax = plt.axes(projection="3d")
#
# plotx = np.arange(start=-2.5, stop=1.5, step=0.1)
# ploty = np.arange(start=-2, stop=2, step=0.1)
# plotx = plotx.reshape([-1, 1])
# Z = p00 + p10 * plotx + p01 * ploty + p20 * plotx ** 2 + p11 * plotx * ploty
#
# ax.plot_surface(plotx, ploty, Z, alpha=0.8, cstride=1, rstride=1, cmap='copper')
#
# ax.scatter(myX[0], myX[1], my_y, marker='.')
# ax.view_init(10, 80)
#
# plt.rcParams['font.sans-serif'] = ['FangSong']
# plt.rcParams['axes.unicode_minus'] = False
#
# ax.set_zlabel('过滤阻力Pa', fontsize=13)
# # ax.view_init(0, 10)
# plt.xlabel('因子1', fontsize=13)
# plt.ylabel('因子2', fontsize=13)
# plt.show()
