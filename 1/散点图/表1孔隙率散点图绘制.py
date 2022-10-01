import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_excel("C题数据.xlsx",sheet_name=0)
data=data.values
plt.rcParams['font.sans-serif']=['FangSong']

# print(data)


pre=np.zeros([25])
lat=np.zeros([25])

for i in range(25):
    pre[i]=data[2 * i, 3]
    lat[i]=data[2 * i + 1, 3]

# print(prehoudu)
# print(lathoudu)

myx=np.arange(25)

plt.title("孔隙率",fontsize=20)

ax=plt.plot(myx, pre, c='red', marker='.')
bx=plt.plot(myx, lat, c='blue', marker='.')
plt.show()

res=np.zeros([2,25])
res[0,:]=pre[:]
res[1,:]=lat[:]
print(res)
np.savetxt("孔隙率数据.csv",res,delimiter=',')