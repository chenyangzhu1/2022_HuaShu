import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['FangSong']

data=pd.read_excel("../C题数据填充.xlsx",sheet_name=2)

data=data.values

# print(data)

x=data[:,0]
y=data[:,1]
z=data[:,4]
x=x.flatten()
y=y.flatten()
z=np.reshape(z,[75,1])
z=z.flatten()
fig = plt.figure()
ax = fig.gca(projection='3d')
pic=ax.plot_trisurf(x,y,z)
plt.xlabel('接收距离(cm)')
plt.ylabel('热风速度(r/min)')
plt.show()