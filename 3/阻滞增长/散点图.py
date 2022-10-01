import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

x = pd.read_csv("data3_接受距离.csv", header=None)
x = x.values

y = pd.read_csv("data3_热风速度.csv", header=None)
y = y.values

myx = np.zeros([2, 25])
myx[0] = x.flatten()
myx[1] = y.flatten()

z = pd.read_csv("data3求平均.csv", header=None)
z = z.values
myz = z[:, 4]
myz = myz.flatten()

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.view_init(20, 20)
ax.set_zlabel('过滤效率（%）',fontsize=13)

plt.xlabel('接收距离(cm)',fontsize=13)
plt.ylabel('热风速度(r/min)',fontsize=13)
ax.scatter(myx[0],myx[1],myz,marker='.')
plt.show()