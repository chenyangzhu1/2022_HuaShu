import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
from sklearn import linear_model

data = pd.read_excel("../C题数据填充.xlsx", sheet_name=0)
data = data.values
plt.rcParams['font.sans-serif'] = ['FangSong']

myx = data[:, 8:11]

y = data[:, 6]

# for i in range(myx.shape[1]):
#     mean = np.mean(myx[:, i])
#     std = np.std(myx[:, i])
#     for j in range(myx.shape[0]):
#         myx[j] = (myx[j] - mean) / std
#
# mean = np.mean(y[:])
# std = np.std(y[:])
# for j in range(y.shape[0]):
#     y[j] = (y[j] - mean) / std

model = linear_model.LinearRegression()

model.fit(myx, y)

# 系数
print("coefficients:", model.coef_)
print("iter:",model.intercept_)

print(model.score(myx,y))
"""coefficients: [  2.78572231 -13.01017835   0.60671575]
0.8980059514021362"""

"""coefficients: [ 0.45174196 -2.10977362  0.09838704]
0.898005951402136"""