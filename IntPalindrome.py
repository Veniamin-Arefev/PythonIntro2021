import math


def count_dig(numb):
    count = 0
    while numb:
        count += 1
        numb //= 10
    return count


number = int(input())
dig_count = count_dig(number)
is_pal = True
for i in range(1, math.ceil(dig_count / 2) + 1):
    if (number // 10 ** (dig_count - i) % 10 != number % 10 ** (i) // 10 ** (i - 1)):
        is_pal = False
        break
print("YES" if is_pal else "NO")
