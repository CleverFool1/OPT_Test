
import numpy as np

POP_SIZE=10
DNA_SIZE=10
length=3

pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE * length))  # matrix (POP_SIZE, DNA_SIZE)

pop2 = np.random.randint(2, size=(5, 5))
X_BOUND = [-3, 3]
Y_BOUND = [-3, 3]




def translateDNA2(pop, length):  # pop表示种群矩阵，一行表示一个二进制编码表示的DNA，矩阵的行数为种群数目
    X = []
    print(pop)
    for i in range(length):
        x_pop1 = pop[:, i:DNA_SIZE * length:length]
        print(x_pop1)
        print('-----------------------')
        x = x_pop1.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (Y_BOUND[1] - Y_BOUND[0]) + \
            Y_BOUND[0]
        X.append(x)

    return X



X=translateDNA2(pop, length)
print('-----------------------')
print(X)
print('-----------------------')
print(X[1])


