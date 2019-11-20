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

TODO: Missing content

- Test function
- How to run `pytest`
- How to execute the tests when committing

---

**Links:**
- [13 Tips for Writing Useful Unit Tests](https://medium.com/better-programming/13-tips-for-writing-useful-unit-tests-ca20706b5368)
- [`pytest` documentation](https://docs.pytest.org/en/latest/)
- [`git` hooks documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
