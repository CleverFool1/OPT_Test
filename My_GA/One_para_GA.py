import math
import random


# 得到所需二进制的位数
def get_bit(start, end, decimal):
    '''
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :return: 所需二进制的位数
    '''
    # 求所需要的二进制数的位数
    need = (end - start) * pow(10, decimal + 1)
    # 对2取对数，向上取整得到位数
    bit = int(math.log(need, 2)) + 1
    return bit


# 编码函数
def encode(start, end, decimal, bit, num):
    '''
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :param bit: 所需二进制的位数
    :param num: 需要转化的十进制数
    :return: 22位二进制数
    '''
    # # 求所需要的二进制数的位数
    # need = (end - start) * pow(10,decimal + 1)
    # # 对2取对数，向上取整得到位数
    # bit = int(math.log(need,2)) + 1
    # print(int(bit)+1)
    # 将数转化为二进制
    binary = bin(int((num + 1) * pow(10, decimal + 1)))
    # 除去前面的0b
    binary = str(binary)[2:]
    # 将其补为22位
    while len(binary) < 22:
        binary = "0" + binary
    return binary


# 解码函数
def decode(start, end, decimal, num):
    '''
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :param num: 需要解码的二进制数
    :return: 原十进制数
    '''
    num = "0b" + num
    num = int(num, 2)
    num = num / pow(10, decimal + 1) - 1
    # print(num)
    return num


# 适应度函数
def fitness(start, end, decimal, num):
    '''
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :param num: 需要求适应度函数值的二进制数
    :return: 适应度函数值
    '''
    # 首先解码
    x = decode(start, end, decimal, num)
    # 计算适应度函数值
    f = x * math.sin(10 * math.pi * x) + 2.0
    return f


# 选择函数
def select(start, end, decimal, population):
    """
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :param num: 需要求适应度函数值的二进制数
    :param population: 种群，规模为M
    :return: 返回选择后的种群
    """
    # 按照population顺序存放其适应度
    all_fitness = []
    for i in population:
        all_fitness.append(fitness(start, end, decimal, i))
        # print(fitness(start,end,decimal,i))
    # 适应度函数的总和
    sum_fitness = sum(all_fitness)
    # 以第一个个体为0号，计算每个个体轮盘开始的位置，position的位置和population是对应的
    all_position = []
    for i in range(0, len(all_fitness)):
        all_position.append(sum(all_fitness[:i + 1]) / sum_fitness)
    # print(all_position)
    # 轮盘赌进行选择
    # 经过选择后的新种群
    next_population = []
    for i in range(0, len(population)):
        # 生成0-1之间的随机小数
        ret = random.random()
        for j in range(len(all_position)):
            # 根据轮盘赌规则进行选择
            if all_position[j] > ret:
                # print(ret)
                # print(all_position[j])
                next_population.append(population[j])
                break
    return next_population


# 判断是否超出范围的函数
def whether_out(start, end, decimal, num):
    if start <= decode(start, end, decimal, num) <= end:
        return True
    else:
        return False


# 交叉函数
def cross(M, Pc, bit, start, end, decimal, next_population1):
    '''
    :param M: 种群规模
    :param Pc: 交叉概率
    :param bit: 二进制的位数
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :param next_population1: 选择后的种群
    :return: 交叉后的种群
    '''
    num = M * Pc
    # 计数器，判断是否交换次数达到num次
    count = 0
    i = 0
    # # 交叉后的种群
    # next_population2 = []
    # 由于选择后的种群本来就是随机的，所以让相邻两组做交叉，从第一组开始直到达到交叉概率停止
    while (i < M):
        # while(count < num):
        # 随机产生交叉点
        position = random.randrange(0, bit - 1)
        # print(position)
        # print(position)
        # 将两个个体从交叉点断开
        tmp11 = next_population1[i][:position]
        tmp12 = next_population1[i][position:]
        tmp21 = next_population1[i + 1][:position]
        tmp22 = next_population1[i + 1][position:]
        # 重新组合成新的个体
        # print(next_population1[i])
        next_population1[i] = tmp11 + tmp22
        # print(next_population1[i])
        next_population1[i + 1] = tmp21 + tmp12
        # 判断交叉后的个体是否超出范围，如果每超出则count+1，否则i不加，count不加
        if (whether_out(start, end, decimal, next_population1[i]) and whether_out(start, end, decimal,
                                                                                  next_population1[i + 1])):
            i += 2
            count += 1
        else:
            continue
        if count > num:
            break
        # print(count)
    return next_population1


# 取反字符串指定位置的数
def reverse(string, position):
    string = list(string)
    if string[position] == '0':
        string[position] = "1"
    else:
        string[position] = "0"
    return ''.join(string)


# 变异函数
def variation(M, Pm, start, end, decimal, bit, next_population2):
    '''
    :param M: 种群规模
    :param Pm: 变异概率
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :param bit: 二进制的位数
    :param next_population2: 交叉后的种群
    :return: 变异后的种群
    '''

    # i = 0
    for i in range(M):
        ret = random.random()
        # 生成0-1的随机数，如果随机数
        if ret < Pm:
            # 随机产生变异点
            position = random.randrange(0, bit)
            next_population2[i] = reverse(next_population2[i], position)
            # if (whether_out())
            while (whether_out(start, end, decimal, next_population2[i]) == False):
                # 如果超出范围则重新随机产生变异点，直到满足范围
                position = random.randrange(0, bit)
                next_population2[i] = reverse(next_population2[i], position)
        else:
            continue
    return next_population2


# 寻找群体中的最优个体
def search(start, end, decimal, population):
    '''
    :param start: 区间左端点值
    :param end: 区间右端点值
    :param decimal: 有效位数
    :param population: 最终迭代后的群体
    :return: 最优个体
    '''
    # 记录函数值
    fit = []
    for i in population:
        fit.append(fitness(start, end, decimal, i))
    # 求出最大值所在的位置
    position = fit.index(max(fit))
    return decode(start, end, decimal, population[position])


# 测试函数
def test(M, T, Pc, Pm, start, end, decimal):
    bit = get_bit(start, end, decimal)
    # 全集，包括所有编码后的个体
    all = []
    for i in range(-1 * pow(10, 6), 2 * pow(10, 6) + 1):
        all.append(encode(start, end, decimal, bit, i / pow(10, 6)))
        i += 1
    # print(all)
    # 第一次随机选择种群，规模为T
    population = random.sample(all, M)
    # print(all)
    # print(population)
    # 进行选择操作
    next_population1 = select(start, end, decimal, population)
    # print(next_population1)
    # 进行交叉操作
    next_population2 = cross(M, Pc, bit, start, end, decimal, next_population1)
    # print(len(next_population2))
    # a = "1011101"
    # print(reverse(a,2))
    next_population3 = variation(M, Pm, start, end, decimal, bit, next_population2)
    # print(next_population2)
    # print(next_population3)
    sum = 0
    for i in range(len(next_population2)):
        if (next_population2[i] != next_population3[i]):
            sum += 1
    # print(sum)
    # print(len(next_population3))


# 主函数
def main(M, T, Pc, Pm, start, end, decimal):
    """
    :param M: 种群规模
    :param T: 遗传运算的终止进化代数
    :param Pc: 交叉概率
    :param Pm: 变异概率
    :return:
    """
    bit = get_bit(start, end, decimal)
    # 全集，包括所有编码后的个体
    all = []
    for i in range(-1 * pow(10, 6), 2 * pow(10, 6) + 1):
        all.append(encode(start, end, decimal, bit, i / pow(10, 6)))
        i += 1

    # 第一次随机选择种群，规模为T
    population = random.sample(all, M)
    for i in range(T):
        # 进行选择操作
        population = select(start, end, decimal, population)
        # 进行交叉操作
        population = cross(M, Pc, bit, start, end, decimal, population)
        # 进行变异操作
        population = variation(M, Pm, start, end, decimal, bit, population)

    # 最优个体
    final = search(start, end, decimal, population)
    print('%.5f' % final)


if __name__ == '__main__':
    # test()
    main(200, 200, 0.6, 0.005, -1, 2, 5)
