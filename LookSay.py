import itertools


def LookSay():
    out_number, cur_number = itertools.tee([1])
    while True:
        yield from out_number
        cur_number = itertools.chain.from_iterable(
            itertools.starmap(lambda x, y: (len([*y]), int(x)), itertools.groupby(cur_number)))
        out_number, cur_number = itertools.tee(cur_number)
    pass


import sys

exec(sys.stdin.read())
