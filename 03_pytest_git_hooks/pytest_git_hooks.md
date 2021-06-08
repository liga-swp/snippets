# Writing tests and run them frequently

**What:**

- How to write and run tests with [`pytest`](https://docs.pytest.org/en/latest/)
- Have `git` automatically run tests at certain stages with [`git` hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

**Why:**
**No one is writing perfect code, ["Untested Code is Broken Code"](https://plone.org/events/conferences/2007-naples/speakers/sessions/untested-code-is-broken-code)**

- Tests help you to ensure your code is working as expected and help you to find/fix bugs
- Before committing, make sure the tests pass

**Tools:** Popular testing frameworks for `Python`:

- [`unittest`](https://docs.python.org/3/library/unittest.html)
- [`pytest`](https://docs.pytest.org/en/latest/)

There are also so called-linters like [flake8](https://flake8.pycqa.org/en/latest/) that perform for static analysis that can spot e.g. syntax errors, or undefined variables. For more info, see our [Python Linter](https://github.com/f-dangel/swp-snippets/blob/master/06_python_linter/python_linter.md) snippet.

You can install scripts that are executed at certain stages in `git`:

- Before committing
- Before pushing
- ...

These scripts are referred to as [`git` hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) and live in your repository's `.git/hooks/` directory (check it out, there are sample scripts). You can use these scripts for more than just running tests, however, this snippet focusses on the latter use case.

---

**Example:** We will use `pytest` to run the test. First, install it:
```bash
pip install pytest
```

Consider the following function somewhere in your project:

```python
def fib(n):
    """Returns the first n fibonacci numbers, starting with 1, 1, 2, …."""
    if n < 0:
        raise ValueError("Expected a positive number, got: {}".format(n))
    numbers = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        numbers.append(a)
    return numbers
```

We prepared two rudimentary tests for a custom implementation of addition in [tests.py](tests.py):
```python
"""Example tests."""

def test_fib_simple_cases():
    assert fib(0) == []
    assert fib(1) == [1]
    assert fib(2) == [1, 1]
    assert fib(5) == [1, 1, 2, 3, 5]


def test_fib_negative():
    with pytest.raises(ValueError):
        assert fib(-1)


@pytest.mark.parametrize("n", [
    10,
    20,
    100,
    1000,
])
def test_fib_arbitrary_length(n):
    result = fib(n)

    assert result[:2] == [1, 1]

    for a, b, c in zip(result, result[1:], result[2:]):
        assert a + b == c
```
**Side note**: The second test duplicates almost every line of the first one. This can be resolved by using [ parameterized tests ](https://docs.pytest.org/en/stable/parametrize.html) (also [here](https://www.youtube.com/watch?v=2EGgtlf7BN0)), which will not be addressed in this snippet.

`pytest` recognizes the functions performing the test since they were named as such (there are other ways to make `pytest` aware of tests, check out the documentation).

We can now run pytest (setting the verbose flag `-v` for a more comprehensible output)
```bash
pytest -v tests.py
```
```bash
======================= test session starts =======================
(platform info)
collected 6 items

tests.py::test_fib_simple_cases PASSED                      [ 16%]
tests.py::test_fib_negative PASSED                          [ 33%]
tests.py::test_fib_arbitrary_length[10] PASSED              [ 50%]
tests.py::test_fib_arbitrary_length[20] PASSED              [ 66%]
tests.py::test_fib_arbitrary_length[100] PASSED             [ 83%]
tests.py::test_fib_arbitrary_length[1000] PASSED            [100%]

======================== 6 passed in 0.01s ========================
```

### Automation

Great, the tests are passing. But it would be better if they were triggered automatically at a certain point in the development cycle. There are two main methods for this:

- git hooks
- continuous integration (CI) services

**git hooks**

We will install a `git` pre-commit hook that runs the test and only allows the changes to be commited if the tests are passing. [`pre-commit`](pre-commit) requires paths relative to the project directory.
For the script to be triggered before a call to `git commit`, copy it into the hooks directory:
```bash
# make executable
chmod u+x pre-commit
cp pre-commit ../../.git/hooks
```

If the tests fail, the commit will be rejected.

**Continuous Integration**

These are online services that get notified and run a user-specified build/test script whenever you push a commit to GitHub. You get an email notification if the script fails. Popular choices are:

- [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions) (well integrated into github)
- [Travis CI](https://travis-ci.org/)
- [Drone CI](https://www.drone.io/) (self-hosted)


---

**Links:**

- [Real Python: Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/?utm_source=realpython&utm_medium=rss)
- [13 Tips for Writing Useful Unit Tests](https://medium.com/better-programming/13-tips-for-writing-useful-unit-tests-ca20706b5368)
- [Unit Testing and Why You Should Be Doing It](https://medium.com/better-programming/unit-testing-and-why-you-should-be-doing-it-ab61407c53ce)
- [`pytest` documentation](https://docs.pytest.org/en/latest/)
- [`git` hooks documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
