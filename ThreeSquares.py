import math

my_list = set(eval(input()))
count = 0

my_set = {3}
cur_max = max(my_list)
for i in range(1, int(math.sqrt(cur_max)) + 1):
    for j in range(i, int(math.sqrt(cur_max - i * i) + 1)):
        for k in range(j, int(math.sqrt(cur_max - i * i - j * j)) + 1):
            my_set.add(i * i + j * j + k * k)
print(len(my_set & my_list))
# print(my_list)
