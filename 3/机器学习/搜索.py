import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import KFold, train_test_split, RepeatedKFold
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor

kf = KFold(n_splits=5, shuffle=True, random_state=1)

x = pd.read_csv("data3_接受距离.csv", header=None)
x = x.values

y = pd.read_csv("data3_热风速度.csv", header=None)
y = y.values

myx = np.zeros([100, 2])
myx[:, 0] = x.flatten()
myx[:, 1] = y.flatten()

z = pd.read_csv("data3求平均.csv", header=None)
z = z.values
myz = z[:, 4]

# x_train, x_test, y_train, y_test = train_test_split(myx, myz, random_state=1, train_size=0.7)

# GBDT  XGBoost  随机森林



x_train=myx
y_train=myz


x_test=np.zeros([100*2000,2])
p=0
for i in range(100):
    for j in range(2000):
        x_test[p,0]=i
        x_test[p,1]=j
        p+=1


oof_xgb = np.zeros(len(x_train))
predictions_xgb = np.zeros(len(x_test))

xgb_rmse = []
xgb_score = []
xgb_mae = []

model1 = XGBRegressor(random_state=1)

for fold_, (trn_idx, val_idx) in enumerate(kf.split(x_train, y_train)):
    # print("fold n°{}".format(fold_ + 1))
    kx_train, ky_train = x_train[trn_idx], y_train[trn_idx]
    kx_val, ky_val = x_train[val_idx], y_train[val_idx]

    model1.fit(kx_train, ky_train)

    oof_xgb[val_idx] = model1.predict(x_train[val_idx])

    ky_val_predict = model1.predict(kx_val)
    xgb_rmse.append(mean_squared_error(ky_val, ky_val_predict))
    xgb_score.append(model1.score(kx_train, ky_train))
    xgb_mae.append(mean_absolute_error(ky_val, ky_val_predict))
    predictions_xgb += model1.predict(x_test) / 5

print("XGBoost")
# print(mean_squared_error(y_test,predictions_xgb))
# print(mean_absolute_error(y_test,predictions_xgb))
print(np.mean(xgb_rmse))
print(np.mean(xgb_score))
print(np.mean(xgb_mae))



kf = KFold(n_splits=5, shuffle=True, random_state=1)
oof_gbdt = np.zeros(len(x_train))
predictions_gbdt = np.zeros(len(x_test))

gbdt_rmse = []
gbdt_score = []
gbdt_mae = []

model2 = GradientBoostingRegressor(random_state=1)
for fold_, (trn_idx, val_idx) in enumerate(kf.split(x_train, y_train)):
    # print("fold n°{}".format(fold_ + 1))
    kx_train, ky_train = x_train[trn_idx], y_train[trn_idx]
    kx_val, ky_val = x_train[val_idx], y_train[val_idx]

    model2.fit(kx_train, ky_train)

    oof_gbdt[val_idx] = model2.predict(x_train[val_idx])

    ky_val_predict = model2.predict(kx_val)
    gbdt_rmse.append(mean_squared_error(ky_val, ky_val_predict))
    gbdt_score.append(model2.score(kx_train, ky_train))
    gbdt_mae.append(mean_absolute_error(ky_val, ky_val_predict))
    predictions_gbdt += model2.predict(x_test) / 5
print("GBDT")
# print(mean_squared_error(y_test,predictions_gbdt))
# print(mean_absolute_error(y_test,predictions_gbdt))
print(np.mean(gbdt_rmse))
print(np.mean(gbdt_score))
print(np.mean(gbdt_mae))

train_stack = np.vstack([oof_gbdt,oof_xgb]).transpose()#训练集2列特征
test_stack = np.vstack([predictions_gbdt, predictions_xgb]).transpose()#测试集2列特征


folds_stack = RepeatedKFold(n_splits=5, n_repeats=2, random_state=2018)

oof_stack = np.zeros(train_stack.shape[0])#存放训练集中验证集的预测结果
predictions = np.zeros(test_stack.shape[0])#存放测试集的预测结果

model=RandomForestRegressor(random_state=1)

rf_rmse = []
rf_score = []
rf_mae = []

for fold_,(trn_idx,val_idx) in enumerate(folds_stack.split(train_stack,y_train)):
    # print("fold n°{}".format(fold_ + 1))
    kx_train, ky_train = x_train[trn_idx], y_train[trn_idx]
    kx_val, ky_val = x_train[val_idx], y_train[val_idx]

    model.fit(kx_train, ky_train)

    oof_stack[val_idx] = model.predict(kx_val)#对验证集有一个预测，用于后面计算模型的偏差
    predictions+=model.predict(test_stack)/10
    rf_rmse.append(mean_squared_error(ky_val, ky_val_predict))
    rf_score.append(model.score(kx_train, ky_train))
    rf_mae.append(mean_absolute_error(ky_val, ky_val_predict))

print("STACKING")
# print(mean_squared_error(y_test,predictions))
# print(mean_absolute_error(y_test,predictions))
print(np.mean(rf_rmse))
print(np.mean(rf_score))
print(np.mean(rf_mae))

np.savetxt("自变量.csv",x_test,delimiter=',')
np.savetxt("xgb预测结果.csv",predictions_xgb,delimiter=',')
np.savetxt("gbdt预测结果.csv",predictions_gbdt,delimiter=',')
np.savetxt("stacking结果.csv",predictions,delimiter=',')









#最后的搜索当做测试集放进去，训练集用所有数据

