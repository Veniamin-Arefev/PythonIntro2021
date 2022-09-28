intervals = eval('[' + input() + ']')
dots = []
for left, right in intervals:
    dots.append((left, '('))
    dots.append((right, ')'))
dots.sort()
sum_len = 0
start = None
brackets_count = 0
for dot, side in dots:
    if side == '()':
        continue
    if start is None and side == '(':
        start = dot
    brackets_count += 1 if side == '(' else -1  # j == ')'
    if (brackets_count == 0):
        sum_len += dot - start
        start = None
print(sum_len)
