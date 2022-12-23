# file: hello.pyx
from math import log


def say_hello_to(name):

    print( "Hello %s!" % name)


def logsum(x , y):

    print( log(x + y))
    return x+y

