import math

N, M = map(int, input().split(","))

len_num = len(str(N))
len2_num = len(str(N ** 2))
max_len = len_num * 2 + len2_num + 3 + 3
one_line_count = math.floor((M - max_len) / (max_len + 3)) + 1
line_rows = math.ceil(N / one_line_count)

form = "{:>" + str(len_num) + "} * {:<" + str(len_num) + "} = {:<" + str(len2_num) + "}"

print("=" * M)
for i in range(1, line_rows + 1):
    for second in range(1, N + 1):
        for first in range((i - 1) * one_line_count + 1,
                           m := (i * one_line_count + 1 if i * one_line_count < N else N + 1)):
            print(form.format(first, second, first * second), end=(" | " if first != m - 1 else "\n"))
    print("=" * M)
