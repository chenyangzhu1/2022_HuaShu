import numpy as np
from scipy.optimize import minimize

gongyi_houdu = [0.05419093, 0.00184155, -0.86020508]

gongyi_kongxilv = [7.50643042e+01, 3.51974149e-01, 2.60499105e-02, -1.54168336e-03,
                   -1.75355368e-04, -8.89120195e-06]

gongyi_yasuohuitan = [4.39577299e+01, 1.15386219e+00, 5.88017537e-02, -2.07223498e-02,
                      2.06636726e-05, -3.10795521e-05]


def obj(X):
    x = X[0]
    y = X[1]
    xx = X[0] ** 2
    xy = X[0] * X[1]
    yy = X[1] ** 2

    houdu = -0.8602 + 0.0542 * x + 0.0018 * y

    kongxilv = 7.50643042e+01 + 3.51974149e-01 * x + 2.60499105e-02 * y - 1.54168336e-03 * xx - 1.75355368e-04 * xy - 8.89120195e-06 * yy

    yasuohuitan = 4.39577299e+01 + 1.15386219e+00 * x + 5.88017537e-02 * y - 2.07223498e-02 * xx + 2.06636726e-05 * xy - 3.10795521e-05 * yy

    houdu = (houdu - 2.6076) / 0.4792901

    kongxilv = (kongxilv - 95.88) / 0.798759455

    yasuohuitan = (yasuohuitan - 86.6072) / 1.218528894

    zhuyi = -0.650110206 * houdu - 0.612391423 * kongxilv + 0.449814923 * yasuohuitan

    zhuer = 0.190957569 * houdu + 0.441310513 * kongxilv + 0.87680114 * yasuohuitan

    guolvxiaolv = 50.157818 + 2.54363681 * zhuyi - 1.93778788 * zhuer - 0.61286059 * zhuyi ** 2 + 1.13540646 * zhuyi * zhuer

    return -guolvxiaolv


def con1(X):
    return X[0]


def con2(X):
    return 100 - X[0]


def con3(X):
    return X[1]


def con4(X):
    return 2000 - X[1]


mycons = ({'type': 'ineq', 'fun': lambda x: con1(x)},
          {'type': 'ineq', 'fun': lambda x: con2(x)},
          {'type': 'ineq', 'fun': lambda x: con3(x)},
          {'type': 'ineq', 'fun': lambda x: con4(x)}
          )

x0 = [30, 1000]

bound = []
bound.append((20, 40))
bound.append((800, 1200))
bound = tuple(bound)

xcall = []
myobj = lambda x: obj(x)

res = minimize(myobj, x0, bounds=bound, options={'disp': True, 'maxiter': 200}, callback=xcall.append)

for i in range(len(xcall)):
    if (i % 10 == 0):
        np.savetxt("中间结果" + str(i) + ".csv", xcall[i])

print(res.fun, '\n', res.success, '\n', res.x, res.message)  # 输出最优值、求解状态、最优解
