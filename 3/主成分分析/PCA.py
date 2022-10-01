import numpy as np
import pandas as pd
from numpy.linalg import eig
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

data = pd.read_csv("data3求平均.csv", header=None)
data = data.values
x = data[:, 0:3]

for i in range(25):
    x[i, 0] = (x[i, 0] - 2.6076) / 0.4792901
    x[i, 1] = (x[i, 1] - 95.88) / 0.798759455
    x[i, 2] = (x[i, 2] - 86.6072) / 1.218528894

x_pca = np.zeros([25, 2])

for i in range(25):
    x_pca[i, 0] = -0.650110206 * x[i, 0] - 0.612391423 * x[i, 1] + 0.449814923 * x[i, 2]
    x_pca[i, 1] = 0.190957569 * x[i, 0] + 0.441310513 * x[i, 1] + 0.87680114 * x[i, 2]

print(x_pca)

# pca=PCA(n_components=2)
# pca.fit(x)
# x_pca=pca.transform(x)
# print(x_pca)