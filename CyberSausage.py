from fractions import Fraction


class Sausage:
    name = ""
    count = 0

    sausage_length = 12
    sausage_height = 3

    def __init__(self, name="pork!", count=1):
        self.name = str(name)
        self.count = Fraction(count)

    def __str__(self):
        a = ["/------------\\", *(["|" + (self.name * 12)[:12] + "|"] * 3), "\------------/"]
        index = 1 + (self.sausage_length * abs(self)).__floor__() + self.count.__floor__() * 2
        a_new = list(map(lambda x: (x * (self.count.__ceil__() if self.count != 0 else 1))[:index], a))
        if self.count.denominator != 1 or self.count == 0:
            a_new = list(map(lambda x: x + "|", a_new))
        return "\n".join(a_new)

    def __abs__(self):
        return self.count

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, other):
        return Sausage(self.name, self.count * other)

    def __rmul__(self, other):
        return Sausage(self.name, self.count * other)

    def __truediv__(self, other):
        return Sausage(self.name, self.count / other)

    def __add__(self, other):
        return Sausage(self.name, self.count + other.count)

    def __sub__(self, other):
        return Sausage(self.name, self.count - other.count if self.count - other.count > 0 else 0)


import sys

exec(sys.stdin.read())
