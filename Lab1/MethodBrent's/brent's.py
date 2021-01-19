import math

from Lab1.Functions.functions import f1, f2, f3, f4, f5


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def parabolic_minimum(x1, x2, x3, y1, y2, y3):
    return x2 - 0.5 * ((x2 - x1) ** 2 * (y2 - y3) - (x2 - x3) ** 2 * (y2 - y1)) / (
            (x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1))


def are_values_different(a, b, c):
    if a == b or a == c or b == c:
        return False
    return True


def minimization(f, left, right):
    eps = 0.001
    coff = (3 - 5 ** 0.5) / 2
    x = w = v = (left + right) / 2
    fx = fw = fv = f(x)

    d = e = right - left

    i = 0

    while right - left > eps:

        i += 1

        g, e = e, d

        if are_values_different(x, w, v) and are_values_different(fx, fw, fv):

            u = parabolic_minimum(w, x, v, fw, fx, fv)
            if left + eps <= u <= right - eps and abs(u - x) < g / 2:
                d = abs(u - x)
        else:

            if x < (right + left) / 2:
                u = x + coff * (right - x)
                d = right - x
            else:
                u = x - coff * (x - left)
                d = x - left

        if abs(u - x) < eps:
            u = x + sign(u - x) * eps

        yu = f(u)

        if yu <= fx:

            if u >= x:
                left = x
            else:
                right = x
            v, w, x = w, x, u
            fv, fw, fx = fw, fx, yu
        else:

            if u >= x:
                right = x
            else:
                left = x

            if yu <= fw or w == x:
                v, w = w, u
                fv, fw = fw, yu
            else:
                v, u = fv, yu
    print(f(w))


minimization(f1, -0.5, 0.5)
#minimization(f2, 6, 9.9)
minimization(f3, 0, 2 * math.pi)
minimization(f4, 0, 1)
minimization(f5, 0.5, 2.5)
