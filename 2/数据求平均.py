import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']

data = pd.read_excel("C题数据填充.xlsx", sheet_name=2)

data = data.values

x = data[:, 0]
y = data[:, 1]
z = data[:, 2:8]

mx = np.zeros([25])
my = np.zeros([25])
mz = np.zeros([25, 6])

for i in range(25):
    mx[i] = x[3 * i]
    my[i] = y[3 * i]
    mz[i] = (z[3 * i] + z[3 * i + 1] + z[3 * i + 2])/3

np.savetxt("data3_接受距离.csv",mx,delimiter=',')
np.savetxt("data3_热风速度.csv",my,delimiter=',')
np.savetxt("data3求平均.csv",mz,delimiter=',')

