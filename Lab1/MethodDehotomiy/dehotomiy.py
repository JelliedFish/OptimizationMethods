import math

from Lab1.Functions.functions import f1, f2, f3, f4, f5


def minimization(f, a, b):
    e = 0.0001
    delta = e / 4
    n = int(math.log(((b - a) / e), math.e) / math.log(2, math.e))
    fmin = 0

    for i in range(n):
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta

        fx1 = f(x1)
        fx2 = f(x2)
        if fx1 < fx2:
            b = x2
            fmin = fx1
        else:
            a = x1
            fmin = fx2

    print(fmin)


minimization(f1, -0.5, 0.5)
minimization(f2, 6, 9.9)
minimization(f3, 0, 2*math.pi)
minimization(f4, 0, 1)
minimization(f5, 0.5, 2.5)
