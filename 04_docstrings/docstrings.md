# Docstrings

**What:** Write docstrings to document your code

**Why:** It is more convenient to read a short plaintext description than through
the entire implementation of your function, class, or module, to understand:

- what your API does
- how it's supposed to be used
- what the parameters are
- what a user should be careful about

Furthermore, docstrings integrate directly with python's builtin `help()`
function and can be used for auto generating online or PDF documentation.

**Tools:** docstrings are directly integrated into python syntax and need no
further tools for writing. There are several tools for working with documentation
provided by docstrings, e.g.:

- [pydoc](https://docs.python.org/3/library/pydoc.html) invokes python's `help()` function from the terminal
- [sphinx](https://www.sphinx-doc.org/) project documentation generator

---

**Example:**

Consider the following function:

```python
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

There are several details that can't be guessed from the name of the function and
parameter alone. Although, in this simple case, they can be inferred by reading
and understanding the implementation of the function, this poses additional
burden on the reader, and doesn't communicate the intention, which might be
different from the implementation (in case of bugs or corner cases).

The following is much clearer for the reader:

```python
def fib(n):
    """Returns the n'th fibonacci number (0 based), starting with 1, 1, 2, …."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

Docstrings are usually written inside three double or single quotes, but any
string literal at the beginning of a module, class, or function is regarded as
docstring. The three quote syntax has the advantage that it allows multi-line
strings.

It is conventional to start docstrings with a single line that shortly describes
the function, and then, if needed, follow up with more details after an empty
line, e.g.:

```python
def fib(n):
    """
    Returns the n'th fibonacci number (0 based), starting with 1, 1, 2, ….

    :param int n: 0-based index of n'th fibonacci number to be returned
    :returns: n'th fibonacci number

    Computation time is linear in ``n``.

    [important references, citation, etc]
    """
```

Note that we put the leading and trailing quotes on separate lines in the case of
multi-line docstrings.


**Accessing docstrings**

This documentation helps not only when reading the source code, but can also be
accessed in the interactive interpreter (or while debugging), using the builtin
`help()` function e.g.:

```python
help(fib)
```

The help can also be shown from the terminal using the `pydoc` command line
utility, e.g.:

```bash
pydoc math.sin
```

In general, `pydoc` can be used to show the help even for objects nested deep in
your package/class layout:

```bash
pydoc package.subpackage.submodule.class_.method
```

There are also tools such as *sphinx* that use docstrings to auto-generate
documentation for your project.

---

**Links:** References and links to used materials and further reading

- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [pydoc](https://docs.python.org/3/library/pydoc.html)
- [sphinx](https://www.sphinx-doc.org/)
- [realpython: documenting Python code](https://realpython.com/documenting-python-code/)
