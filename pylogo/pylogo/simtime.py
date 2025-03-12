import numpy as np

class SimTime:
    def __init__(self, start=0, steps=10, end=100):
        self.start = start
        self.steps = steps
        self.end = end
        self.arr = np.arange(start, end, steps)

    def __str__(self):
        return f"SimTime(start={self.start}, steps={self.steps}, end={self.end})"

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__init__(*args, **kwargs)
        return obj.arr
