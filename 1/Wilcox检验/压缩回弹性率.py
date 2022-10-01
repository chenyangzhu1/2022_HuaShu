import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
data=pd.read_excel("../C题数据填充.xlsx",sheet_name=0)
data=data.values
plt.rcParams['font.sans-serif']=['FangSong']

# print(data)


pre=np.zeros([25])
lat=np.zeros([25])

for i in range(25):
    pre[i]=data[2 * i, 4]
    lat[i]=data[2 * i + 1, 4]

# print(prehoudu)
# print(lathoudu)

# myx=np.arange(25)
#
# plt.title("厚度",fontsize=20)
#
# ax=plt.plot(myx, pre, c='red', marker='.')
# bx=plt.plot(myx, lat, c='blue', marker='.')
# plt.show()

stat, p = ss.ranksums(pre, lat)
print(ss.ranksums(pre, lat))

# RanksumsResult(statistic=-3.560422975533368, pvalue=0.0003702579082898629)