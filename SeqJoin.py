def joinseq(*seq):
    first_letters = dict()

    seq = list(map(iter, seq))
    for ind, it in enumerate(seq):
        first_letters[ind] = next(it)
    while True:
        my_min = min(first_letters.items(), key=lambda x: x[1], default=None)
        if my_min is None:
            break
        yield my_min[1]
        first_letters.pop(my_min[0])
        if (new_elem := next(seq[my_min[0]], None)) is not None:
            first_letters[my_min[0]] = new_elem


import sys

exec(sys.stdin.read())
