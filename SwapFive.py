k = int(input())
p = 0
while True:
    if (n := k * (10 ** (p + 1) - 1)) % (10 * k - 1) == 0:
        print(n // (10 * k - 1))
        break
    else:
        p += 1
