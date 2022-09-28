import itertools


def chainslice(begin, end, *seq):
    yield from itertools.islice(itertools.chain(*seq), begin, end)


import sys

exec(sys.stdin.read())
