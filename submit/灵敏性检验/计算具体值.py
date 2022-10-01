import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


#### 压缩回弹性
def yasuohuitan(X):
    popt = [4.39577299e+01, 1.15386219e+00, 5.88017537e-02, - 2.07223498e-02, 2.06636726e-05, - 3.10795521e-05]
    p00 = popt[0]
    p10 = popt[1]
    p01 = popt[2]
    p20 = popt[3]
    p11 = popt[4]
    p02 = popt[5]
    x = X[0]
    y = X[1]
    return p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2


#### 厚度
def houdu(X):
    popt = [0.05419093, 0.00184155, -0.86020508]
    return popt[0] * X[0] + popt[1] * X[1] + popt[2]


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

    return xiaolv * 82.98, zuli * 36.47


x = [ 17.97813515 ,1149.62005709]
print("压缩回弹，厚度，过滤效率，过滤阻力")
print(yasuohuitan(x))
print(houdu(x))
print(obj(x))
