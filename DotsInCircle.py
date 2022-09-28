x, y, r = map(int, input().split(','))
my_continue = True
inside = True
while (my_continue):
    a, b = map(int, input().split(','))
    if (a == 0 and b == 0):
        break
    if ((x - a) ** 2 + (y - b) ** 2 > r ** 2):
        inside *= False
print("YES" if inside else "NO")
