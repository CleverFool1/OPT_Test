# cy_utils.pyx
from math import log

from libc.stdio cimport printf

def my_print():

    printf("hello world\n")


def logsum(x, y):
    return log(x + y)


def cy_logsum2(double x, double y):
    return log(x + y)



#cy_utils.pyx
def cy_integ(a, b, N):
      cdef int i
      cdef double s, dx, ds
      s = 0
      dx = (b - a) / N
      for i in range(N):
        ds = a + i * dx
        s += ds ** 2 - ds
      return s * dx

def cy_integ2(double a, double b, int N):
      cdef int i
      cdef double s, dx, ds
      s = 0
      dx = (b - a) / N
      for i in range(N):
        ds = a + i * dx
        s += ds ** 2 - ds
      return s * dx