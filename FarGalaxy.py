from collections import OrderedDict

start = OrderedDict()
while a := input():
    if a[0] == '.':
        break
    start[tuple(map(float, a.split()[:-1]))] = a.split()[-1]

pairs = [(i, j) for i in start for j in start if i < j]
my_max = max(pairs, key=lambda x: sum([(x[0][i] - x[1][i]) ** 2 for i in range(3)]))
print(*sorted([start[my_max[0]], start[my_max[1]]]))
