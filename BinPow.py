def BinPow(a, n, f):
    return f(*(l := [BinPow(a, n // 2, f)] * 2)) if n % 2 == 0 else a if n == 1 else f(a, BinPow(a, n - 1, f))
