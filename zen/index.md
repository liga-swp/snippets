# Zen of Python

**What:** Idiomatic principles guiding both the design and usage of python.

**Why:** It's good to have commonly shared design ideals.

**Tools:** No tools needed;)

---

**Example:**

The *Zen of Python* is a poem that captures quite well some of the principles
that have influenced (and continue to influence) the design of python and the
idioms of what *idiomatic* python code should look like. It can be shown anytime
in the python interpreter:

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Of course, some of these ideas are very subjective. After all, this is a piece of
poetry and not a strict rule book that must zealously be followed to the point.
Nevertheless it might give you some general ideas and input on how to structure
your code. Some of these ideas will also become clearer the more experience you
have with programming.

Also, for fun, you may want to look at the source code of the ``this.py`` module!

**Braces syntax**

If you are one of those who want the braces `{ ... }` syntax that is used e.g. in
C/C++/Java to enclose block scope, you may want to try this:

```python
>>> from __future__ import braces
```

**More easter eggs**

```python
>>> import antigravity
```

There is an april fools' [PEP 401](https://www.python.org/dev/peps/pep-0401/)
that (once activated) adds some syntax alternatives (which of course should not
be used in serious code).


---

**Links:** References and links to used materials and further reading

- [PEP 20 -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [PEP 401 -- BDFL Retirement](https://www.python.org/dev/peps/pep-0401/)
- [Python’s easter eggs and hidden jokes](https://hackernoon.com/pythons-easter-eggs-and-hidden-jokes-d7368c7fe2c2)
