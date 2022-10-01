import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_excel('../C题数据填充.xlsx', sheet_name=0)
data = data.values
plt.rcParams['font.sans-serif']=['FangSong']
pre = np.zeros([25])
lat = np.zeros([25])
chaceng = np.zeros([25])

ans = np.zeros([25, 7])

for i in range(25):
    pre[i] = data[2 * i, 2]
    lat[i] = data[2 * i + 1, 2]
    chaceng[i] = data[2 * i + 1, 8]

ans[:, 0] = lat - pre

for i in range(25):
    pre[i] = data[2 * i, 3]
    lat[i] = data[2 * i + 1, 3]
    chaceng[i] = data[2 * i + 1, 8]
ans[:, 1] = lat - pre

for i in range(25):
    pre[i] = data[2 * i, 4]
    lat[i] = data[2 * i + 1, 4]
    chaceng[i] = data[2 * i + 1, 8]

ans[:, 2] = lat - pre

for i in range(25):
    pre[i] = data[2 * i, 5]
    lat[i] = data[2 * i + 1, 5]
    chaceng[i] = data[2 * i + 1, 8]
ans[:, 3] = lat - pre

for i in range(25):
    pre[i] = data[2 * i, 6]
    lat[i] = data[2 * i + 1, 6]
    chaceng[i] = data[2 * i + 1, 8]
ans[:, 4] = lat - pre

for i in range(25):
    pre[i] = data[2 * i, 7]
    lat[i] = data[2 * i + 1, 7]
    chaceng[i] = data[2 * i + 1, 8]
ans[:, 5] = lat - pre

ans[:, 6] = chaceng

res = pd.DataFrame(ans, columns=['厚度',
                                 '孔隙率',
                                 '压缩回弹性',
                                 '过滤阻力',
                                 '过滤效率',
                                 '透气性',
                                 '插层率'])

corr=res.corr(method='spearman')

sns.heatmap(corr,annot=True,vmax=1,vmin=0,xticklabels=True,yticklabels=True,
            square=True,cmap="Blues")

plt.show()