# Example of the Shapiro-Wilk Normality Test
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
from scipy.stats import shapiro
from geneview.gwas import qqplot

# print('stat=%.3f, p=%.3f' % (stat, p))
# if p > 0.05:
# 	print('Probably Gaussian')
# else:
# 	print('Probably not Gaussian

data=pd.read_csv("data3求平均.csv",header=None)
data=data.values
print(shapiro(data[:,2]))

# ax = qqplot(data[:,0],ax=1)
fig = plt.figure()
res = stats.probplot(data[:,2], plot=plt)
plt.show()

