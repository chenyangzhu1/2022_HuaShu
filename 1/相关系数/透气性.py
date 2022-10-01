import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
from scipy.stats import spearmanr, pearsonr
data = pd.read_excel("../C题数据填充.xlsx", sheet_name=0)
data = data.values
plt.rcParams['font.sans-serif'] = ['FangSong']

# print(data)


pre = np.zeros([25])
lat = np.zeros([25])
chaceng = np.zeros([25])
for i in range(25):
    pre[i] = data[2 * i, 7]
    lat[i] = data[2 * i + 1, 7]
    chaceng[i] = data[2 * i + 1, 8]

myx = lat - pre

# myx = pd.DataFrame(myx)
# chaceng = pd.DataFrame(chaceng)
res = spearmanr(myx,chaceng)
res2=pearsonr(myx,chaceng)
print(res2)
#