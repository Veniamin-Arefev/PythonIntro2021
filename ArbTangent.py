import decimal
from decimal import Decimal


def pi():
    out = Decimal(0)
    fack, fac3k, fac6k = 1, 1, 1
    for k in range(0, decimal.getcontext().prec // 10):
        for i in range(k, k + 1):
            fack *= (i if i > 0 else 1)
        for i in range(3 * (k - 1) + 1, 3 * k + 1):
            fac3k *= (i if i > 0 else 1)
        for i in range(6 * (k - 1) + 1, 6 * k + 1):
            fac6k *= (i if i > 0 else 1)
        out += (Decimal(-1) ** k * fac6k * (13591409 + 545140134 * k)) / (fac3k * fack ** 3 * 640320 ** (3 * k))
    out = out * Decimal(10005).sqrt() / 4270934400
    return out ** (-1)


def my_sin(x):
    decimal.getcontext().prec += 5
    k, prev, out, num, fact, sign = 1, 0, x, x, 1, 1
    while out != prev:
        prev = out
        k += 2
        fact *= k * (k - 1)
        num *= x ** 2
        sign *= -1
        out += num / fact * sign
    decimal.getcontext().prec -= 5
    return +out


def my_cos(x):
    decimal.getcontext().prec += 5
    k, prev, out, num, fact, sign = 0, 0, 1, 1, 1, 1
    while out != prev:
        prev = out
        k += 2
        fact *= k * (k - 1)
        num *= x ** 2
        sign *= -1
        out += num / fact * sign
    decimal.getcontext().prec -= 5
    return +out


degree = Decimal(input())
decimal.getcontext().prec = int(input())

decimal.getcontext().prec += 5
angle = Decimal(degree) * pi() / 200
tang = my_sin(angle) / my_cos(angle)

decimal.getcontext().prec -= 5
print(str(+tang))
