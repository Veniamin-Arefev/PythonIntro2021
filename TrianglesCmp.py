import math


class Triangle:
    sides = []

    def __init__(self, a, b, c):
        self.sides = [*map(float, [a, b, c])]

    def __bool__(self):
        a = sorted(self.sides, reverse=True)
        return all(i > 0 for i in a) & (a[0] < a[1] + a[2])

    def __abs__(self):
        if (self):
            p = sum(self.sides) / 2
            return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
        else:
            return 0

    def __str__(self):
        return f"{self.sides[0]}:{self.sides[1]}:{self.sides[2]}"

    def __eq__(self, other):
        return all(i == j for i, j in zip(sorted(self.sides), sorted(other.sides)))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)


import sys

exec(sys.stdin.read())
