import math

from Lab1.Functions.functions import f1, f2, f3, f4, f5


def fibonachi(n):
    if n in (1, 2):
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


def minimization(f, a, b):
    n = 20

    def findDot(a, b, n, k, is_first):
        if is_first:
            return a + (fibonachi(n - k - 1) * (b - a)) / fibonachi(n - k + 1)
        else:
            return a + (fibonachi(n - k) * (b - a)) / fibonachi(n - k + 1)

    x1 = findDot(a, b, n, 1, True)
    x2 = findDot(a, b, n, 1, False)

    for k in range(2, n + 1):

        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = findDot(a, b, n, k, False)
        else:
            b = x2
            x2 = x1
            x1 = findDot(a, b, n, k, True)
        if k == n - 2:
            break
    print(f((x1 + x2) / 2))


minimization(f1, -0.5, 0.5)
minimization(f2, 6, 9.9)
minimization(f3, 0, 2 * math.pi)
minimization(f4, 0, 1)
minimization(f5, 0.5, 2.5)
