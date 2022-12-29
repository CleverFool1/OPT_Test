# -*- coding: utf-8 -*-
# @Time : 29/12/22 上午 09:46
# @Author : 张斌飞
# @Email : ZhangBinFei1995@outlook.com
# @File : My_Multiparameter_Ga.py
# @Project : pythonProject1


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm

DNA_SIZE = 24  # 基因长度
POP_SIZE = 30  # 种群数量
CROSSOVER_RATE = 0.7  # 交叉概率
MUTATION_RATE = 0.005  # 变异概率
N_GENERATIONS = 200  # 迭代次数

X_BOUND = [-3, 3]  # 参数取值范围
Y_BOUND = [-3, 3]
length = 3  # 参数数目，即需要求解的未知数个数
Parameter_BOUND = [[-1, 1],
                   [-1, 1],
                   [-1, 1]]


# Parameter_BOUND = [[-2.048, 2.048],
#                    [-2.048, 2.048]
#                    ]


# 定义函数
def F(X):
    x = X[0]
    y = X[1]
    z=X[2]
    # return 3 * (1 - x) ** 2 * np.exp(-(x ** 2) - (y + 1) ** 2) - 10 * (x / 5 - x ** 3 - y ** 5) * np.exp(
    #     -x ** 2 - y ** 2) - 1 / 3 ** np.exp(-(x + 1) ** 2 - y ** 2)
    # return np.sin(x) + 1 + np.cos(x)
    return 100.0 * (y - x ** 2.0) ** 2.0 + (1 - x) ** 2.0+4*z


# 计算函数适应度值
def get_fitness(pop):
    X = translateDNA(pop, length, Parameter_BOUND)
    pred = F(X)
    # return (pred - np.min(
    #     pred)) + 1e-9  # 减去最小的适应度是为了防止适应度出现负数，通过这一步fitness的范围为[0, np.max(pred)-np.min(pred)],最后在加上一个很小的数防止出现为0的适应度
    return -(pred - np.max(pred))+ 1e-9     # 求函数最小值时的适应度函数


# 初始种群

def translateDNA(pop, length, Parameter_BOUND):  # pop表示种群矩阵，一行表示一个二进制编码表示的DNA，矩阵的行数为种群数目
    X = []
    for i in range(length):
        x_pop1 = pop[:, i:DNA_SIZE * length:length]  # 每隔几列取一个基因组成新的一个参数基因值
        x = x_pop1.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (Parameter_BOUND[i][1] - \
                                                                                     Parameter_BOUND[i][0]) + \
            Parameter_BOUND[i][0]
        X.append(x)

    return X


def crossover_and_mutation(pop, CROSSOVER_RATE, length):
    new_pop = []
    for father in pop:  # 遍历种群中的每一个个体，将该个体作为父亲
        child = father  # 孩子先得到父亲的全部基因（这里我把一串二进制串的那些0，1称为基因）
        if np.random.rand() < CROSSOVER_RATE:  # 产生子代时不是必然发生交叉，而是以一定的概率发生交叉
            mother = pop[np.random.randint(POP_SIZE)]  # 再种群中选择另一个个体，并将该个体作为母亲
            mother2 = pop[np.random.randint(POP_SIZE)]  # 再种群中选择另一个个体，并将该个体作为母亲
            cross_points = np.random.randint(low=0, high=DNA_SIZE)  # 随机产生交叉的点
            child[cross_points:DNA_SIZE] = mother[cross_points:DNA_SIZE]  # 孩子得到位于交叉点后的母亲的基因
            child[cross_points + DNA_SIZE:DNA_SIZE * length] = mother2[cross_points + DNA_SIZE:DNA_SIZE * length]
        mutation(child, MUTATION_RATE, length)  # 每个后代有一定的机率发生变异
        new_pop.append(child)

    return new_pop


def mutation(child, MUTATION_RATE, length):
    if np.random.rand() < MUTATION_RATE:  # 以MUTATION_RATE的概率进行变异
        mutate_point = np.random.randint(0, DNA_SIZE * length)  # 随机产生一个实数，代表要变异基因的位置
        mutate_point2 = np.random.randint(0, DNA_SIZE * length)  # 随机产生一个实数，代表要变异基因的位置
        child[mutate_point] = child[mutate_point] ^ 1  # 将变异点的二进制为反转
        child[mutate_point2] = child[mutate_point2] ^ 1  # 将变异点的二进制为反转


def select(pop, fitness):  # nature selection wrt pop's fitness  自然选择WRT pop的适应性
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,
                           p=(fitness) / (fitness.sum()))  # 适应度越高，被选择的机会越高，而适应度低的，被选择的机会就低。
    return pop[idx]


def print_info(pop):
    fitness = get_fitness(pop)
    max_fitness_index = np.argmax(fitness)
    print("max_fitness:", fitness[max_fitness_index])
    X = translateDNA(pop, length, Parameter_BOUND)
    print("最优的基因型：", pop[max_fitness_index])
    # x = X[0][max_fitness_index]
    # y = X[1][max_fitness_index]
    # z=X[2][max_fitness_index]
    X=np.array(X)
    # print(X[...,max_fitness_index])
    print("(x, y,z):", X[...,max_fitness_index])
    # print("(x, y):", (x[max_fitness_index], y[max_fitness_index]))

    print('此时的函数值为：', F( X[...,max_fitness_index]))


def plot_2d(N_GENERATIONS, Max_fitness, Average_fitness):
    plt.ion()
    plt.plot(range(N_GENERATIONS), Max_fitness, label='Max_fitness', color='red', linewidth=1.0, linestyle='--')
    plt.plot(range(N_GENERATIONS), Average_fitness, label="Average_fitness")

    # df = pd.DataFrame(columns=['A', 'B'])
    # fig = df.plot(figsize=(10, 6))  # 创建图表对象，并复制给fig
    plt.title('GA')
    plt.xlabel('N_GENERATIONS ')
    plt.ylabel('fitness ')
    plt.legend(loc="upper right")  # 标签显示（一般称为图例）
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    plt.ion()

    pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE * length))  # 生成初始种群  matrix (POP_SIZE, DNA_SIZE*length)

    Average_fitness = []
    Max_fitness = []
    Function_value = []
    for i in range(N_GENERATIONS):  # 迭代N代
        X = translateDNA(pop, length, Parameter_BOUND)
        pop = np.array(crossover_and_mutation(pop, CROSSOVER_RATE, length))   # 变异与交叉
        # F_values = F(translateDNA(pop)[0], translateDNA(pop)[1])#x, y --> Z matrix
        fitness = get_fitness(pop)
        pop = select(pop, fitness)  # 选择生成新的种群

        Average_fitness.append(np.mean(fitness))  # 每一代的平均是适应度
        Max_fitness.append(np.amin(fitness))  # 每一代的最大适应度值

        # 计算每一代的最优函数值
        max_fitness_index = np.argmax(fitness)
        X = translateDNA(pop, length, Parameter_BOUND)
        x = X[0][max_fitness_index]
        y = X[1][max_fitness_index]
        z= X[2][max_fitness_index]
        Function_value.append(F([x, y,z]))

    print_info(pop)
    plot_2d(N_GENERATIONS, Max_fitness, Average_fitness)

    plt.ion()
    plt.plot(range(N_GENERATIONS), Function_value)
    plt.ioff()
    plt.show()

    # # df = pd.DataFrame(np.random.rand(10, 2), columns=['A', 'B'])
    # # fig = df.plot(figsize=(10, 6))  # 创建图表对象，并复制给fig
    #
    # plt.plot( range(N_GENERATIONS),Max_fitness,label = 'Max_fitness',color = 'red',linewidth=1.0,linestyle='--')
    # plt.plot(range(N_GENERATIONS), Average_fitness ,label = "Average_fitness")
    #
    # # df = pd.DataFrame(columns=['A', 'B'])
    # # fig = df.plot(figsize=(10, 6))  # 创建图表对象，并复制给fig
    # plt.title('GA')
    # plt.xlabel('N_GENERATIONS ')
    # plt.ylabel('fitness ')
    # plt.legend(loc="upper right")  # 标签显示（一般称为图例）
    # plt.show()
