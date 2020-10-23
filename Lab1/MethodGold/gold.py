import math

from Lab1.Functions.functions import f1, f2, f3, f4, f5


def minimization(f, a, b):
    e = 0.0001
    fmin = 0
    k = (3 - math.sqrt(5)) / 2

    x1 = a + (b - a) * k
    x2 = b - (b - a) * k

    fx1 = f(x1)
    fx2 = f(x2)

    while b - a > e:

        if fx1 < fx2:
            # Выбираем интервал
            # Сохраняем функцию
            b = x2
            fmin = fx1
            #

            # Переобозначаем x1 и x2 на основании нового интервала
            # По свойству золотого сечения нам достаточно найти x1 , тк x2 -это прошлый x1
            x2 = x1
            x1 = a + (b - a) * k
            #

            # Находим оракула в точке x1
            # В точке x2 он уже известен
            fx2 = fx1
            fx1 = f(x1)
            #

        else:
            # Выбираем интервал
            # Сохраняем функцию
            a = x1
            fmin = fx2
            #

            # Переобозначаем x1 и x2 на основании нового интервала
            # По свойству золотого сечения нам достаточно найти x1 , тк x2 -это прошлый x1
            x1 = x2
            x2 = b - (b - a) * k
            #

            # Находим оракула в точке x1
            # В точке x2 он уже известен
            fx1 = fx2
            fx2 = f(x2)
            #

    print(fmin)


minimization(f1, -0.5, 0.5)
minimization(f2, 6, 9.9)
minimization(f3, 0, 2 * math.pi)
minimization(f4, 0, 1)
minimization(f5, 0.5, 2.5)
