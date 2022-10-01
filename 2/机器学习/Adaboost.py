import pandas as pd
import numpy as np

from sklearn.ensemble import AdaBoostRegressor, AdaBoostClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, mean_squared_error
from sklearn.model_selection import train_test_split

x = pd.read_csv("data3_接受距离.csv", header=None)
x = x.values

y = pd.read_csv("data3_热风速度.csv", header=None)
y = y.values

myx=np.zeros([25,2])
myx[:,0]=x.flatten()
myx[:,1]=y.flatten()

z = pd.read_csv("data3求平均.csv", header=None)
z = z.values
myz=z[:,4]


x_train,x_test,y_train,y_test=train_test_split(myx,myz,random_state=1,train_size=0.7)

model=AdaBoostRegressor(random_state=1)


model.fit(x_train,y_train)

y_test_predict=model.predict(x_test)
# p_test=precision_score(y_test,y_test_predict)
# r_test=recall_score(y_test,y_test_predict)
# f1_test=f1_score(y_test,y_test_predict)

rmse=np.sqrt(mean_squared_error(y_test,y_test_predict))
score=model.score(x_train,y_train)
print(rmse)
print(score)

res=np.zeros([100,2000])
for i in range(1,100):
    for j in range(1,2000):
        res[i,j]=model.predict([[i,j]])