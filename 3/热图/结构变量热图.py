import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr

plt.rcParams['font.sans-serif'] = ['FangSong']

z = pd.read_csv("data3求平均.csv", header=None)
z = z.values

data = z[:, 0:3]

res = pd.DataFrame(data, columns=['厚度', '孔隙率', '压缩回弹性'])

corr = res.corr(method='pearson')

sns.heatmap(corr,
            annot=True,
            vmax=1,
            vmin=0,
            xticklabels=True,
            yticklabels=True,
            square=True,
            cmap="YlGnBu")

plt.show()
print(spearmanr(res['厚度'], res['孔隙率']))
print(spearmanr(res['厚度'], res['压缩回弹性']))
print(spearmanr(res['孔隙率'], res['压缩回弹性']))

print(pearsonr(res['厚度'], res['孔隙率']))
print(pearsonr(res['厚度'], res['压缩回弹性']))
print(pearsonr(res['孔隙率'], res['压缩回弹性']))
