# py_utils.py
from math import log


def logsum(x, y):
    return log(x + y)


def py_integ(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        ds = a + i * dx
        s += ds ** 2 - ds
    return s * dx
