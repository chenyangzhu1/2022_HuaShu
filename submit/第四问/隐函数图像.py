import matplotlib.pyplot as plt
import numpy as np

# 作点
x = np.linspace(-70, 120, 1000)
y = np.linspace(-300, 2500, 1000)

# 构造网格
x, y = np.meshgrid(x, y)
z = x
# 上式等号右边即为要绘制的方程，方程的右边等于0
# 绘制等高线,8表示等高线数量加1
plt.contour(x, y, z, 0)

z = x - 100
plt.contour(x, y, z, 0)

z = y - 2000
plt.contour(x, y, z, 0)

z = y
plt.contour(x, y, z, 0)

z = -0.8648 + 0.05428 * x + 0.001844 * y
plt.contour(x, y, z, 0)

z = -0.8648 + 0.05428 * x + 0.001844 * y - 3
plt.contour(x, y, z, 0)

z = 43.96 + 1.149 * x + 0.05897 * y - 0.02063 * x ** 2 + 2e-5 * x * y - 85 - 3.114e-5 * y ** 2
plt.contour(x, y, z, 0)
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('接收距离(cm)',fontsize=13)
plt.ylabel('热风速度(r/min)',fontsize=13)
# z = 43.96 + 1.149 * x + 0.05897 * y - 0.02063 * x ** 2 + 2e-5 * x * y -100- 3.114e-5 * y ** 2
# plt.contour(x, y, z, 0)

plt.show()
