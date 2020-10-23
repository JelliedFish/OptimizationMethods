import math


def f1(x):
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1  # [-0.5;0.5]


def f2(x):
    return math.log(x - 2, 10) + math.log(10 - x, 10) ** 2 - x ** 0.2  # [6;9.9]


def f3(x):
    return -3 * x * math.sin(0.75 * x) + math.exp(x) - 2 * x  # [0;2pi]


def f4(x):
    return math.exp(3 * x) + 5 * math.exp(-2 * x)  # [0;1]


def f5(x):
    return 0.2 * math.log(x, 10) + (x - 2.3) ** 2  # [0.5;2.5]
