#cy_utils.pyx
from cy_include cimport c_max

def max3(double a, double b, double c):
  return c_max(c_max(a, b), c)