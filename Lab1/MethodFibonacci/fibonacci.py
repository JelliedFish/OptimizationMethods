import math

from Lab1.Functions.functions import f1, f2, f3, f4, f5


def F(n):
    return (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n)


def minimization(f, a, b):
    delta = 0.00001

    n = 1

    while F(n) <= (b - a) / delta:
        n += 1

    n -= 2

    x1 = a + (F(n - 2) / F(n)) * (b - a)
    x2 = a + (F(n - 1) / F(n)) * (b - a)
    f1 = f(x1)
    f2 = f(x2)

    for k in range(2, n - 2):

        if f1 <= f2:
            b = x2
            x2 = x1
            x1 = a + (F(n - k) / F(n - k + 1)) * (b - a)
            f1 = f(x1)

        else:
            a = x1
            x1 = x2
            x2 = a + (F(n - k) / F(n - k + 1)) * (b - a)
            f2 = f(x2)

    min = (x1 + x2) / 2
    minf = f(min)

    print(minf)


minimization(f1, -0.5, 0.5)
minimization(f2, 6, 9.9)
minimization(f3, 0, 2 * math.pi)
minimization(f4, 0, 1)
minimization(f5, 0.5, 2.5)
