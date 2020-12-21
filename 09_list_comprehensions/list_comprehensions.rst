List comprehensions
===================

*List comprehensions* are a syntax feature of python with which many loops can
be rewritten in a more declarative functional style. Code that makes use of
list-comprehensions is often shorter, less indented, communicates its intent
more concisely, and is therefore more readable than its imperative
counterpart.

Whenever you see a for-loop like that in python code, you should be thinking
"Can I write this more succinctly using a list comprehension?"

For example, consider the following function that takes a list of numbers and
computes a list with their squares:

.. code-block:: python

    squares = []
    for n in numbers:
        squares.append(n ** 2)

The same can be written as follows with list comprehensions:

.. code-block:: python

    squares = [n ** 2 for n in numbers]

List comprehensions can also include ``if`` conditions that allow filtering
out certain items. For example consider the following code that filters all
even numbers from a list of arbitrary numbers:

.. code-block:: python

    even = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)

Again, the same can be written using a list comprehensions:

.. code-block:: python

    even = [n for n in numbers if n % 2 == 0]

This syntax also supports more complex constructs such as nested loops. For
example, the following flattens a document that is given as a list of lines,
where each line is in turn represented by a list of words:

.. code-block:: python

    flattened = []
    for line in text:
        for word in line:
            flattened.append(word)

This is equivalent to:

.. code-block:: python

    flattened = [
        word
        for line in text
        for word in line
    ]


Related constructs
==================

There are three closely related syntaxes in python that work the same way but
result in different data types.

- *dict* comprehensions: ``{k: v for ...}``
- *set* comprehensions: ``{x for ...}``
- *generator* expressions: ``(x for ...)``



See also
========

- https://realpython.com/list-comprehension-python/
- https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
- https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
