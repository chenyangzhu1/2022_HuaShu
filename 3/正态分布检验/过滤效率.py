# Example of the Shapiro-Wilk Normality Test
import math

import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
from scipy.stats import shapiro
from geneview.gwas import qqplot
import seaborn as sns
# print('stat=%.3f, p=%.3f' % (stat, p))
# if p > 0.05:
# 	print('Probably Gaussian')
# else:
# 	print('Probably not Gaussian

data=pd.read_csv("data3求平均.csv",header=None)





data=data.values
print(shapiro(data[:,4]))

sns.histplot(data[:,4],kde=True)
plt.show()


# ax = qqplot(data[:,0],ax=1)
fig = plt.figure()
res = stats.probplot(data[:,4], plot=plt)
plt.show()

for i in range(25):
    data[i,4]=math.sqrt(data[i,4])

print(shapiro(data[:,4]))

sns.histplot(data[:,4],kde=True)
plt.show()