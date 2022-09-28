import sys

linearized_classes = {}
classes = {}


def merge(lists):
    merged = []
    i = 0
    while True:
        item = lists[i][0]
        if any(j.index(item) != 0 for j in lists if lists[i][0] in j and lists[i] != j):
            i += 1
        else:
            merged.append(item)
            lists = list(filter(lambda x: len(x) > 0, map(lambda x: x[1:] if item in x else x, lists)))
            # lists = [i[1:] for i in lists if item in i and len(i) > 1]
            if len(lists) == 0:
                if all(merged.count(i) == 1 for i in merged):
                    return merged
                else:
                    raise ValueError
            i = 0
        if i == len(lists):
            raise ValueError


def linearize(my_class, dependencies):
    if len(dependencies) == 0:
        linearized_classes[my_class] = [my_class]
        pass
    else:
        for i in dependencies:
            if i not in linearized_classes:
                linearized_classes[i] = None
                linearize(i, classes[i][0])
        linearized_classes[my_class] = \
            [my_class, *merge([linearized_classes[i] for i in dependencies] + [[*dependencies]])]
        pass


user_input = [i.split() for i in sys.stdin.read().split("\n")]
user_input = list(filter(lambda x: len(x) > 0, user_input))

for i in user_input[:-1]:
    if len(i) == 1:
        classes[i[0]] = [[], []]
    elif len(i) == 2:
        if i[1][0].isupper():
            classes[i[0]] = [[*i[1]], []]
        else:  # i[1][0].islower()
            classes[i[0]] = [[], [*i[1]]]
    else:  # len(i) == 3
        classes[i[0]] = [[*i[1]], [*i[2]]]

if len(user_input[-1]) == 2:
    classes["PepelaC"] = (None, [])  # own details
    specific_details = {*user_input[-1][1]}
else:
    classes["PepelaC"] = (None, [user_input[-1][1]])  # own details
    specific_details = {*user_input[-1][2]}

# print(classes)

try:
    for i, j in classes.items():
        if i != "PepelaC":
            linearize(i, j[0])

    linearize("PepelaC", user_input[-1][0])
    total_details = {*sum([classes[i][1] for i in linearized_classes["PepelaC"]], [])}
    # print("specific_details ", specific_details)
    # print("total_details", total_details)
    if not total_details.issuperset(specific_details):
        raise ValueError
    print("Correct")
except Exception as e:
    print("Incorrect")

# print(linearized_classes)
