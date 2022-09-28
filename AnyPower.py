import math

number = int(input())
is_power = False
for i in range(2, math.ceil(math.sqrt(number)) + 1):
    numb = number
    while (numb != 1):
        numb /= i
        if numb < i:
            break
        elif numb == i:
            is_power = True
    if is_power:
        break
print("YES" if is_power else "NO")
