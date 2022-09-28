class Dots:
    start, stop = 0, 0

    def __init__(self, a, b):
        self.start, self.stop = a, b

    def __getitem__(self, item):
        # print("   " + item.__repr__())
        if type(item) == int:
            step = (self.stop - self.start) / (item - 1)
            return iter(i * step + self.start for i in range(item))
        elif type(item) == slice:
            if item.step is None:
                step = (self.stop - self.start) / (item.stop - 1)
                return self.start + item.start * step
            else:
                step = (self.stop - self.start) / (item.step - 1)
                return iter(self.start + i * step for i in range(0 if item.start is None else item.start,
                                                                 item.step if item.stop is None else item.stop))
        else:
            return None


import sys

exec(sys.stdin.read())
