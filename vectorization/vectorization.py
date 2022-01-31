from contextlib import contextmanager
from timeit import default_timer

import math
import numpy as np


@contextmanager
def timed(text="Elapsed time"):
    start = default_timer()
    yield
    end = default_timer()
    print("{}: {:.3f}s".format(text, end - start))


with timed("python loop"):
    xs = range(10_000_000)
    ys = range(10_000_000)
    result = 0
    for x, y in zip(xs, ys):
        result += math.sqrt(x**2 + y**2)
    result /= len(xs)
    print(f"{result=}")


with timed("vectorized"):
    xs = np.arange(10_000_000)
    ys = np.arange(10_000_000)
    result = np.sqrt(xs**2 + ys**2).mean()
    print(f"{result=}")
