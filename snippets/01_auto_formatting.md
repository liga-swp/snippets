# Auto-formatting and PEP8

**What:** Format your code according to the official style guide lines ([PEP8](https://www.python.org/dev/peps/pep-0008/)).

**Why:** 

- Common coding standard and improved code readability

- Easy to automate, no need to spend mental resources while coding

- Auto-formatting modifies how your code looks without affecting its behavior


**Tools:** Three very prominent Python auto-formatting tools are

- [`autopep8`](https://github.com/hhatto/autopep8)
- [`black`](https://github.com/psf/black)
- [`yapf`](https://github.com/google/yapf)

Check out [this](https://www.kevinpeters.net/auto-formatters-for-python) blog post for more details.
Chances are quite high that your editor supports one of the above formatters via a plugin.

---

**Example:** Let's try one of the above auto-formatters. We will use `autopep8` and install it by:
```bash
pip install autopep8
```

Let us consider an arbitrary piece of Python code, for instance the following function that returns the sum of its 5 inputs (script [`poor_format.py`](./poor_format.py)):
```python
def sum_five_arguments(argument1, argument2, argument3 , keyword_argument1=123, keyword_argument2 = 5):
    """Returns a sum of all arguments."""
    sum_of_args=argument1+argument2+argument3+keyword_argument1 + keyword_argument2
    return sum_of_all_args
```
Beside lacking elegance, this code suffers from poor readability caused by formatting issues:

- Very long lines
- Inconsistent conventions for spaces between arguments/operators

The optical quality of this code can easily be improved by running `autopep8`:
```bash
autopep8 --inplace --aggressive --aggressive poor_format.py
```

This will trigger the code-formatter (with a certain aggressive level specified by flags) to apply changes to the poorly formatted script and save it. The result should look like that:

```python
def sum_five_arguments(
        argument1,
        argument2,
        argument3,
        keyword_argument1=123,
        keyword_argument2=5):
    """Returns a sum of all arguments."""
    sum_of_args = argument1 + argument2 + argument3 + \
        keyword_argument1 + keyword_argument2
    return sum_of_args
```
Congratulations! The formatting issues were consistently resolved.

Different auto-formatters can yield different outputs, but they are highly customizable. 

---

**Links:**

- [ Kevin Peters: Auto formatters for Python ]( https://www.kevinpeters.net/auto-formatters-for-python )

- [ PEP 8 -- Style Guide for Python Code ]( https://www.python.org/dev/peps/pep-0008/ )
