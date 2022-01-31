# Vectorization

**What:** Replace python loops by numpy operations on vectors.

This allows moving loops from python to C/Fortran and making use of numerical
routines that were carefully optimized over the course of many decades - down
to using specialized instructions available in the CPU, and performing
operations in cache-friendly order.

**Why:**

- (much) faster program execution
- more eco friendly
- often more concise and readable programs
- therefore less error-prone (typically fewer bugs!)
- more closely resembles mathematical notation

**Tools:**

- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)

---

**Example:**

*Naive* python code:

```python
import math

xs = range(10_000_000)
ys = range(10_000_000)
result = 0
for x, y in zip(xs, ys):
    result += math.sqrt(x**2 + y**2)
result /= len(xs)
```

Vectorized:

```python
import numpy as np

xs = np.arange(10_000_000)
ys = np.arange(10_000_000)
result = np.sqrt(xs**2 + ys**2).mean()
print(f"{result=}")
```

Run time (see [source](./vectorization.py)):

```
python loop: 5.227s
vectorized: 0.097s
```

The speedup can often be even more significant.

Note: You have to use the numpy functions instead of the builtin ones to fully
make use of the speedup, so don't use `sum(xs)`, but rather `np.sum(x)` or
`x.sum()`.


**Useful things to know about**

- multi-dimensional arrays: `np.zeros((3, 5, 7))` is a 3×5×7 dimensional array
- numpy supports the `x[start:stop:step]` python slicing syntax, with support
  for multi-dimensional indexing:
  - `x[::2]` extracts every second element in the first dimension
  - `x[::2, ::2]` does the same in the first two dimensions
  - `x[..., ::2, :]` does the same in the second to last dimension

- boolean masks:
  - `x < 3` is a boolean array with the same shape as `x`
  - boolean masks can be used to index arrays, e.g.: `x[(x < 3) | (x > 5)]`

- adding dimensions:
  - `x[None, :]` is a 1×N array (same as `x.reshape(1, -1)`)
  - `x[:, None]` is a N×1 array (same as `x.reshape(-1, 1)`)

- broadcasting: `np.arange(5)[:, None] * np.arange(3)[None, :]` is a 5×3 array
- numpy defines many mathematical functions that act elementwise (sin, cos,
  exp, …)

- array dimensions can be reduced using e.g. `np.sum()`,
  `np.prod()` `np.all()`, `np.any()`. Optionally, all these functions accept an
  `axis` argument that can be used to perform the reduction only over specified
  dimensions.


**pandas**

Pandas is a wrapper over numpy arrays for working with tabular data. A pandas
DataFrame can have:

- row and column names (or more generically indexes)
- multi-level indexes
- different data types for each column

pandas also provides many useful functions that often come up in the context
of data analysis, such as:

- grouping by specified column values (`DataFrame.groupby()`)
- joining tables (`pandas.join()`, `pandas.merge()`, …)
- converting columns into indexes and vice versa (`DataFrame.stack()`,
  `DataFrame.unstack()`).

Example (simple algorithm):

```python
match_data = pd.DataFrame(...)    # fetch from OpenLigaDB

matches = match_data[
  ((match_data.HomeTeam == 'Stuttgart') &
  (match_data.AwayTeam == 'Nürnberg') |
]

home = matches.HomeGoals > matches.AwayGoals
away = matches.HomeGoals < matches.AwayGoals
draw = ~home & ~away

num_home = home.sum()
num_away = away.sum()
num_draw = draw.sum()
```

---

**Links:** References and links to used materials and further reading

- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
- [Numba](https://numba.pydata.org/)
