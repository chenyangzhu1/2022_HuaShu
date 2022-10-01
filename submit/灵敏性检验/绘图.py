import numpy as np
import matplotlib.pyplot as plt

idx = np.arange(7)
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
x = [19.95985194, 19.00200115, 18.40262979, 17.97813515, 17.65885453, 17.41081979, 17.2133381]
y = [1204.92291937, 1181.2702941, 1163.70828487, 1149.62005709, 1137.9109177, 1128.02142078, 1119.5626856]

yasuohutian = [84.95898395960776, 84.95727669899995, 84.95621388695557, 84.95548038409541, 84.9549487994646,
               84.9545538693083, 84.95425455717614]

houdu = [2.4403636614567277, 2.3448993442794244, 2.280077534768153, 2.2311295995782787, 2.1922645202058475,
         2.1606112839199136, 2.1343323837101127]

xiaolv = [89.25550111102237, 91.27634439236763, 92.16800706499085, 92.63662030428213, 92.89930179264972,
          93.04710069515019, 93.12647330234147]

zuli = [28.288753086341885, 28.574232580282118, 28.781124270730697, 28.947318551202194, 29.086811318755736,
        29.20612655519384, 29.309534818389196]

idx = idx.flatten()
plt.plot(idx + 1, x, marker='.')
plt.xlabel('组合序号', fontsize=13)
plt.ylabel('接收距离(cm)', fontsize=13)
plt.show()

plt.plot(idx + 1, y, marker='.')
plt.xlabel('组合序号', fontsize=13)
plt.ylabel('热风速度(r/min)', fontsize=13)
plt.show()

plt.plot(idx + 1, houdu, marker='.')
plt.xlabel('组合序号', fontsize=13)
plt.ylabel('厚度mm', fontsize=13)
plt.show()

plt.plot(idx + 1, yasuohutian, marker='.')
plt.xlabel('组合序号', fontsize=13)
plt.ylabel('压缩回弹性率（%）', fontsize=13)
plt.ylim(50,100)
plt.show()

plt.plot(idx + 1, xiaolv, marker='.')
plt.xlabel('组合序号', fontsize=13)
plt.ylabel('过滤效率（%）', fontsize=13)
plt.show()

plt.plot(idx + 1, zuli, marker='.')
plt.xlabel('组合序号', fontsize=13)
plt.ylabel('过滤阻力Pa', fontsize=13)
plt.show()
