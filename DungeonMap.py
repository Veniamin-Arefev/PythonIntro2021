def foo(elem):
    global diction
    global ends
    inner = dict()
    for i in diction.keys():
        inner[i] = 0
    new = [ends[0]]
    while 1:
        for i in new:
            if i == ends[1]:
                return True
            for j in diction[i].keys():
                if inner[j]:
                    continue
                elif j == ends[1]:
                    return True
                inner[j] = 1
                new.append(j)
            new.remove(i)
        if not new:
            return False


diction = dict()
ends = []
while pair := input():
    if pair.find(' ') < 1:
        ends.append(pair)
        if len(ends) > 1: break
        continue
    pair = pair.split(' ')
    if not pair[0] in diction.keys(): diction[pair[0]] = dict()
    if not pair[1] in diction.keys(): diction[pair[1]] = dict()
    diction[pair[1]][pair[0]] = 1
    diction[pair[0]][pair[1]] = 1

print('YES' if foo(ends[0]) else 'NO')
