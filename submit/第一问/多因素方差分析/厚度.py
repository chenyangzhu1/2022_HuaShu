import numpy as np
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.read_excel("C题数据填充.xlsx")
data = data.values

for i in range(50):
    if data[i, 8] != 0:
        data[i, 8] = int(data[i, 8] / 10 + 1)
    data[i,9]=(int(data[i,9]-20))/5
    data[i, 10] = (int(data[i, 10]) - 800) / 100
    if(data[i,8]==6):
        data[i,8]=5

predata = np.zeros([50, 4])

predata[:, 0] = data[:, 2]
predata[:, 1] = data[:, 8]
predata[:, 2] = data[:, 9]
predata[:, 3] = data[:, 10]

predata = pd.DataFrame(predata, columns=['厚度', '插层率', '接收距离', '热风速度'])

model = ols("厚度 ~插层率+接收距离+热风速度+插层率:接收距离+插层率*热风速度+接收距离*热风速度+插层率*接收距离*热风速度", data=predata)
data = model.fit()
print(anova_lm(data))

# hsd=pairwise_tukeyhsd(predata['厚度'],predata['插层率'])
# print(hsd)
