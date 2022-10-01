import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

def obj(X):
    # if (con2(X) < 0 or con3(X) < 0):
    #     return 0
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

    return -0.5 * xiaolv + 0.5 * zuli



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



def con2(X):
    x = X[0]
    y = X[1]
    return -(-0.8648 + 0.05428 * x + 0.001844 * y - 3)


def con3(X):
    x = X[0]
    y = X[1]
    return 43.96 + 1.149 * x + 0.05897 * y - 0.02063 * x ** 2 + 2e-5 * x * y - 85 - 3.114e-5 * y ** 2

x0 = np.linspace(start=15, stop=45, num=30)
x1 = np.linspace(start=600, stop=1300, num=30)
x0=x0.reshape([-1,1])

X=np.zeros([2,30])
X[0,:]=x0.flatten()
X[1,:]=x1.flatten()

Z=obj(X)
Z=Z.reshape([-1,1])
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(x0,x1,Z,alpha=0.8, cstride=1, rstride = 1, cmap='copper')

plt.show()