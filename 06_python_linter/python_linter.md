# Python Linter

**What:** Linters are tools that perform code analysis in order to find
possible bugs or stylistic issues.

**Why:**

- due to its highly dynamic nature, in python many programming errors, such as
  typos, missing imports, type errors, and even syntax errors, can often go
  undetected until runtime
- many errors can even be missed altogether, if the corresponding module,
  function, or code branch is never executed, or works by accident
- linters help prevent certain classes of statically detectable errors that even
  tests sometimes do not uncover
- linters help in enforcing a common coding style across a code base


**Tools:** Some of the most prevalent linters are:


- [flake8](https://github.com/PyCQA/flake8) I recommend starting off with
  *flake8*. It combines three basic tools for static code analysis in its belly
  and presents the results in a unified report:

  - [pyflakes](https://pypi.org/project/pyflakes/): static analysis (syntax
    errors, unused variables, undefined names, etc)
  - [mccabe](https://pypi.org/project/mccabe/): complexity analysis, reports
    highly complex functions (which often indicate error proneness)
  - [pycodestyle](https://pypi.org/project/pycodestyle/): style checks

- [pylint](https://www.pylint.org/) is another commonly used tool. However,
  it is much more strict in what it considers bad style by default, which can
  be quite overwhelming (i.e. it has a larger false positive rate)

---

**Example:**

Consider the following module that contains a naive implementation of the
``sinc`` function:

```python
def sinc(t):
    """Return the sinus cardinalis of t."""
    if t = 0:
        return 1
    else:
        return sin(x) / t


# Yay works:
print(sinc(0))
```

Did you spot the mistakes?

Maybe you did, good job! But in large code bases, errors like these quickly
become harder to recognize.

Running ``flake8`` on the sample reports the syntax error in a heartbeat:

```bash
$ flake8 sample.py
sample.py:3:10: E999 SyntaxError: invalid syntax
```

And after fixing the issue, running flake8 again reveals possible runtime errors:

```bash
sample.py:6:16: F821 undefined name 'sin'
sample.py:6:20: F821 undefined name 'x'
```

**Customization:**

You may not always agree with flake8's default settings on coding style, in which
case it is possible to let flake8 ignore certain error codes or exclude specified
folders. This can be done on the command line or within a config files.


**Hooks**

For every serious code base, it is a must have to run static analysis on every
commit through continuous integration tools (such as GitHub Actions, or Travis
CI).

Additionally, we recommend always running flake8 before you commit. You have
already learned to achieve this by using a git precommit hook.

It is even better and much quicker to directly integrate flake8 with your
editor. Many IDEs have equivalent checks builtin, or provide them through
plugins.

I also recommend running flake8 as part of your automatic testing whenever
commits are pushed to github. This will be part of a later snippet about
*continuous integration*.


---

**Links:** References and links to used materials and further reading

- [Python Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/)
