import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import matplotlib.pyplot as plt
from geneview.gwas import qqplot
data=pd.read_csv("data1纯数据.csv",header=None)
data = data.values
plt.rcParams['font.sans-serif'] = ['FangSong']
from scipy import stats
import seaborn as sns


def self_JBtest(y):
    # 样本规模n
    n = y.size
    y_ = y - y.mean()
    """
    M2:二阶中心钜
    skew 偏度 = 三阶中心矩 与 M2^1.5的比
    krut 峰值 = 四阶中心钜 与 M2^2 的比
    """
    M2 = np.mean(y_ ** 2)
    skew = np.mean(y_ ** 3) / M2 ** 1.5
    krut = np.mean(y_ ** 4) / M2 ** 2

    """
    计算JB统计量，以及建立假设检验
    """
    JB = n * (skew ** 2 / 6 + (krut - 3) ** 2 / 24)
    pvalue = 1 - stats.chi2.cdf(JB, df=2)
    # print("偏度：", stats.skew(y), skew)
    # print("峰值：", stats.kurtosis(y) + 3, krut)
    print("JB检验：", stats.jarque_bera(y))
    return np.array([JB, pvalue])


idx=5
print(self_JBtest(data[:, idx]))


plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False


fig = plt.figure()
res = stats.probplot(data[:, idx], plot=plt)
plt.show()

sns.histplot(data[:,idx],kde=True)
plt.show()


for i in range(50):
    data[i,idx]=math.log(data[i,idx])

print(self_JBtest(data[:, idx]))

sns.histplot(data[:,idx],kde=True)
plt.show()