def divdigit(x):
    cop, count = x, 0
    while cop:
        if cop % 10 != 0 and x % (cop % 10) == 0:
            count += 1
        cop //= 10
    return count
