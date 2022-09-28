input()
my_map = []
while True:
    a = input()
    if a[0] == '-':
        break
    my_map.append([i for i in a])

rect_count = 0
for row_index, row in enumerate(my_map):
    for item_index, item in enumerate(row):
        if item == "#":
            if (item_index == 0 or my_map[row_index][item_index - 1] != '#') \
                    and (row_index == 0 or my_map[row_index - 1][item_index] != '#'):
                rect_count += 1
print(rect_count)
