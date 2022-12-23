# test.py
from py_utils import logsum as py_logsum
from cy_utils import logsum as cy_logsum
from cy_utils import cy_logsum2
import time

#
# # a rough estimation of running time of certain function.
# def run_time(x, y, rep, func, func_name):
#     total_time = 0.0
#     for i in range(5):
#         start_time = time.time()
#         for _ in range(rep):
#             res = func(x, y)
#         total_time += time.time() - start_time
#     stime = total_time / 5.0
#     print("%s: res = %.6f, time = %.2f" % (func_name, res, stime))
#
#
# def main(x, y, rep):
#     run_time(x, y, rep, py_logsum, "py_logsum")
#     run_time(x, y, rep, cy_logsum, "cy_logsum")
#     run_time(x, y, rep, cy_logsum2, "cy_logsum2")
#
#
# if __name__ == "__main__":
#     main(3.1, 5.2, 10000000)


# test.py
from py_utils import py_integ
from cy_utils import cy_integ, cy_integ2 , my_print
import time


# a rough estimation of running time of certain function.
def run_time(x, y, N, rep, func, func_name):
    total_time = 0.0
    for i in range(5):
        start_time = time.time()
        for _ in range(rep):
            res = func(x, y, N)
        total_time += time.time() - start_time
    stime = total_time / 5.0
    print("%s: res = %.6f, time = %.2f" % (func_name, res, stime))


def main(x, y, N, rep):
    run_time(x, y, N, rep, py_integ, "py_integ")
    run_time(x, y, N, rep, cy_integ, "cy_integ")
    run_time(x, y, N, rep, cy_integ2, "cy_integ2")


if __name__ == "__main__":
    main(3.1, 5.2, 100, 100000)
    my_print()
