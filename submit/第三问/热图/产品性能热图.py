import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
z = pd.read_csv("data3求平均.csv", header=None)
z = z.values

data = z[:, 3:6]

res = pd.DataFrame(data, columns=['过滤阻力',
                                  '过滤效率',
                                  '透气性'])

corr = res.corr(method='pearson')

sns.heatmap(corr, annot=True, vmax=1, vmin=-1, xticklabels=True, yticklabels=True,
            square=True, cmap="YlGnBu")

plt.show()

print(spearmanr(res['过滤阻力'], res['过滤效率']))
print(spearmanr(res['过滤阻力'], res['透气性']))
print(spearmanr(res['过滤效率'], res['透气性']))

print(pearsonr(res['过滤阻力'], res['过滤效率']))
print(pearsonr(res['过滤阻力'], res['透气性']))
print(pearsonr(res['过滤效率'], res['透气性']))
