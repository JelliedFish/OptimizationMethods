import math

from Lab1.Functions.functions import f1, f2, f3, f4, f5


def parabolic_minimum(x1, x2, x3, y1, y2, y3):
    return x2 - 0.5 * ((x2 - x1) ** 2 * (y2 - y3) - (x2 - x3) ** 2 * (y2 - y1)) / (
            (x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1))


def minimization(f, a, b):
    e = 0.001

    x1, x2, x3 = a, (a + b) / 2, b
    y1, y2, y3 = f(x1), f(x2), f(x3)

    while x3 - x1 >= e:

        u = parabolic_minimum(x1, x2, x3, y1, y2, y3)
        yu = f(u)

        if u < x2:
            if yu < y2:
                x3, y3 = x2, y2
                x2, y2 = u, yu

            else:

                x1, y1 = u, yu
        else:

            if yu < y2:
                x1, y1 = x2, y2
                x2, y2 = u, yu

            else:
                x3, y3 = u, yu
    print(f((x1 + x3) / 2))


minimization(f1, -0.5, 0.5)
minimization(f2, 6, 9.9)
minimization(f3, 0, 2 * math.pi)
minimization(f4, 0, 1)
minimization(f5, 0.5, 2.5)
