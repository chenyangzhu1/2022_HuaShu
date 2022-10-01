import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


def obj(X):
    x = X[0]
    y = X[1]
    k1 = 15.9
    k2 = 3.27944218
    k3 = -5.60411769
    k4 = 10.76586634
    return -(25 / (1 + 1.5 * np.exp(-k1 * x / 10)) + 25 / (1 + 1.5 * np.exp(-k2 * y / 1000)) + 50 / (
            1 + 1.5 * np.exp(-k3 * x / 10 - k4 * y / 1000)))


myobj = lambda x: obj(x)

bound = []

bound.append((0, 100))
bound.append((0, 2000))
bound = tuple(bound)
xcall = []

# x0 = np.arange(start=0, stop=100, step=10)
# x1 = np.arange(start=0, stop=2000, step=100)
#
#
# pre=900
# preinit=[]
#
# idx=np.arange(200)
# maxidx=np.zeros([200])
#
# p=0
# for i in range(len(x0)):
#     for j in range(len(x1)):
#         init = [x0[i], x1[j]]
#         # print(init)
#         res = minimize(myobj, init, bounds=bound, options={'disp': True, 'maxiter': 200}, callback=xcall.append)
#         if pre>=res.fun:
#             preinit=init
#             pre=res.fun
#         maxidx[p]=-pre
#         p+=1
#         # print(res.fun, '\n', res.success, '\n', res.x, res.message)  # 输出最优值、求解状态、最优解
#
# print(pre)
# print(preinit)
# plt.rcParams['font.sans-serif'] = ['FangSong']
# plt.rcParams['axes.unicode_minus'] = False
#
# plt.xlabel('搜索次数(次)',fontsize=13)
# plt.ylabel('过滤效率(%)',fontsize=13)
#
# plt.plot(idx,maxidx,marker='.')
#
# plt.show()

x0 = [10,1000]

res = minimize(myobj, x0, bounds=bound, options={'disp': True, 'maxiter': 200}, callback=xcall.append)

for i in range(len(xcall)):
        np.savetxt("中间结果" + str(i) + ".csv", xcall[i])

print(res.fun, '\n', res.success, '\n', res.x, res.message)  # 输出最优值、求解状态、最优解
