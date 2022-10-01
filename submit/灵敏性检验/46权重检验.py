import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


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

    return -0.8 * xiaolv + 0.2 * zuli


myobj = lambda x: obj(x)


# def con1(X):
#     x = X[0]
#     y = X[1]
#     return -0.8648 + 0.05428 * x + 0.001844 * y

def con2(X):
    x = X[0]
    y = X[1]
    return -(-0.8648 + 0.05428 * x + 0.001844 * y - 3)


def con3(X):
    x = X[0]
    y = X[1]
    return 43.96 + 1.149 * x + 0.05897 * y - 0.02063 * x ** 2 + 2e-5 * x * y - 85 - 3.114e-5 * y ** 2


mycons = (
    {'type': 'ineq', 'fun': lambda x: con2(x)},
    {'type': 'ineq', 'fun': lambda x: con3(x)}
)
bound = []

bound.append((15, 45))
bound.append((600, 1300))
bound = tuple(bound)
xcall = []

x0 = np.arange(start=15, stop=45, step=3)
x1 = np.arange(start=600, stop=1300, step=10)

pre = 900
preinit = []
pre_zuizhong=[]
idx = np.arange(700)
maxidx = np.zeros([700])

p = 0
for i in range(len(x0)):
    for j in range(len(x1)):
        init = [x0[i], x1[j]]
        # print(init)
        res = minimize(myobj, init, bounds=bound, constraints=mycons, options={'disp': True, 'maxiter': 200},
                       callback=xcall.append)
        if pre >= res.fun:
            preinit = init
            pre = res.fun
            pre_zuizhong=res.x
        maxidx[p] = -pre
        p += 1
        # print(res.fun, '\n', res.success, '\n', res.x, res.message)  # 输出最优值、求解状态、最优解
print("最优值：",pre)
print("初始值:",preinit)
print("最优值取值：",pre_zuizhong)
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('搜索次数(次)', fontsize=13)
# plt.ylabel('过滤效率(%)',fontsize=13)

plt.plot(idx, maxidx, marker='.')

plt.show()

# res = minimize(myobj, [18, 890], bounds=bound, constraints=mycons, options={'disp': True, 'maxiter': 200},
#                callback=xcall.append)
# print(res.fun, '\n', res.success, '\n', res.x, res.message)  # 输出最优值、求解状态、最优解

# x0 = [18, 890]
#
# res = minimize(myobj, x0, bounds=bound, constraints=mycons, options={'disp': True, 'maxiter': 200},
#                callback=xcall.append)
#
# for i in range(len(xcall)):
#     np.savetxt("中间结果" + str(i) + ".csv", xcall[i])
#
# print(res.fun, '\n', res.success, '\n', res.x, res.message)  # 输出最优值、求解状态、最优解
