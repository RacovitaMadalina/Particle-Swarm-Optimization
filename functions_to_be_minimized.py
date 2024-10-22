import math
import numpy as np

from constants import *


def quadric_function(x):
    return x[0] ** 2 - 2 * x[0] + 3


def de_jong(x):
    return sum(x * x)


def six_hump_camel_back(x):
    return (4 - 2.1 * (x[0] ** 2) + (x[0] ** 4) / 3) * x[0] ** 2 + x[0] * x[1] + (-4 + 4 * (x[1] ** 2)) * (x[1] ** 2)


def rosenbrock(x):
    rosenbrock_value = 0
    for i in range(len(x) - 1):
        rosenbrock_value += (100 * ((x[i + 1] - x[i] ** 2) ** 2) + (1 - x[i]) ** 2)
    return rosenbrock_value


def rastrigin(x):
    return 10 * len(x) + sum(x * x) - 10 * sum(np.cos(2 * math.pi * x))
    #rastrigin_value = 10 * len(x)
    #for i in range(len(x)):
    #    rastrigin_value += (x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i]))
    #assert abs(val2 - rastrigin_value) < 1e-5
    #return rastrigin_value


def griewangk(x):
    s = sum(x * x) / 4000
    product = 1
    for i in range(len(x)):
        product = product * math.cos(x[i] / math.sqrt(i + 1))
    return s + product + 1