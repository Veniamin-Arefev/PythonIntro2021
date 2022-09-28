import itertools
from random import randint

def randomes(seq):
    seq = [*seq]
    while True:
        for ind, item in enumerate(seq):
            if type(item) == tuple:
                start, end = item
            else:
                first, second = itertools.tee(item)
                seq[ind] = first
                start, end = second
            yield randint(start, end)


import sys

exec(sys.stdin.read())
