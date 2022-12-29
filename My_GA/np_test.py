import numpy as np

a = np.arange(24)
print(a)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小  reshape 函数来调整数组大小。
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b)
print(b.ndim)

# 随机生产0-5之内的数
for i in range(6):
    print(i)

# 下面是一个创建空数组的实例：
# numpy.empty(shape, dtype = float, order = 'C')
# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype=int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

x = np.ones([2, 2], dtype=int)
print(x)

# 将列表转换为 ndarray:
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)
# 将元组转换为 ndarray:
x = (1, 2, 3)
a = np.asarray(x)
print(a)
# 将元组列表转换为 ndarray:
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)

# numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：numpy.arange(start, stop, step, dtype)
x = np.arange(10, 20, 2)
print(x)

# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的   np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

a = np.linspace(10, 20, 50)
print(a)

# numpy.logspace 函数用于创建一个于等比数列。格式如下：
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None) 对数 log 的底数。


a = np.logspace(0, 9, 10, base=3)
print(a)

# ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。
#
# ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。
a = np.arange(10)
b = a[2:7:2]  # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
print(a[s])

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # 第2列元素
print(a[1, ...])  # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素



# NumPy 高级索引
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)

# 可以借助切片 : 或 … 与索引数组组合。如下面例子：
a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b = a[1:3, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)


# 布尔索引
# 我们可以通过一个布尔数组来索引目标数组。
# 布尔索引通过布尔运算（如：比较运算符）来获取符合指定条件的元素的数组。
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素
print  ('大于 5 的元素是：')
print (x[x >  5])

# 以下实例使用了 ~（取补运算符）来过滤 NaN。
a = np.array([np.nan,  1,2,np.nan,3,4,5])
print (a[~np.isnan(a)])



# NumPy 广播(Broadcast)
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print (c)
print(a + b)


a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(a + bb)


for i in range(15):
    print(i)
for x in np.arange(6):
    print (x, end="\n" )


# 控制遍历顺序
# for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
# for x in np.nditer(a.T, order='C'):C order，即是行序优先；
for x in np.nditer(a):
    print (x, end=", " )
print ('\n')