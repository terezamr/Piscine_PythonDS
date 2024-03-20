import statistics
import numpy as np
# *args accepts positional arguments
# **kwargs accepts keywords (or named) arguments

# for arg in kwargs          - iterates over the keys
# for arg in kwargs.values   - iterates over the values

def mean(*args) -> float:
    result = sum(args)/len(args)
    return result

def median(l_args) -> float:

    n = len(l_args) // 2
    if len(l_args) % 2 == 0: # even
        result = (l_args[n - 1] + l_args[n]) / 2
    else:
        result = l_args[n]
    return result

def quartiles(l_args):

    n = len(l_args) // 2
    data1 = list(l_args)[:n + 1]
    m1 = median(data1)

    data2 = list(l_args)[n:]
    m2 = median(data2)

    return [float(m1), float(m2)]

def std(l_args):
    # saafsa
    print('ola')


def ft_statistics(*args: any, **kwargs: any) -> None:

    l_args = list(args)
    l_args.sort()

    for opt in kwargs.values():
        if not args:
            print("ERROR")
        elif opt == 'mean':
            r = mean(*args)
            print("mean:", r)
        elif opt == 'median':
            r = median(l_args)
            print("median:", r)
        elif opt == 'quartile':
            r = quartiles(l_args)
            print("quartile:", r)
        elif opt == 'std':
            a = np.array(l_args)
            print("std:", np.std(a))
        elif opt == 'var':
            a = np.array(l_args)
            print("var:", np.var(a))
