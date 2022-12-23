# 画出图像如下
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt

'''
以为加载不出来三维图片是  缺少组件
# import tkinter
# import matplotlib as mpl
# mpl.use("TkAgg")  # Use TKAgg to show figures
# mpl.rcParams['legend.fontsize'] = 10

'''

plt.ion()  # 打开交互模式


fig1 = plt.figure(figsize=(10, 6))
# ax = Axes3D(fig1)   # 错误的语句
ax = plt.axes(projection='3d')
x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)
Z = 0.5 - (np.sin(np.sqrt(X ** 2 + Y ** 2)) ** 2 - 0.5) / (1 + 0.001 * (x ** 2 + y ** 2) ** 2)
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlim([-1, 5])
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()

fig2 = plt.figure(figsize=(10, 6))
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()

fig3 = plt.figure(figsize=(10, 6))
# 创建3d绘图区域
ax = plt.axes(projection='3d')
# 从三个维度构建
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
# 调用 ax.plot3D创建三维线图
ax.plot3D(x, y, z, 'black')
ax.set_title('3D line plot')


plt.ioff()
plt.show()
