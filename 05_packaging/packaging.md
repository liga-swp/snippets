# Packaging

**What:** Creating python packages by writing a `setup.py`.

**Why:** Reusability, Publishing, Declaring Dependencies

Publishing your library or application as a python package makes it searchable
and installable by other users via [pip](https://pip.pypa.io/), and declares
its dependencies, such that they can later be installed automatically.

**Tools:**

- [setuptools](https://setuptools.readthedocs.io/)
- [pip](https://pip.pypa.io/)
- [twine](https://twine.readthedocs.io/)
- ([flit](https://flit.readthedocs.io/))

---

**Project structure:**

Before writing any code, the first thing is to structure your project properly
into directories. We'll start off with the most basic layout, which looks like
this:

```
project_repo/
  .git
  README.rst
  setup.py
  soccer_predictor_2000/
    __init__.py
    algorithms/
      poisson_regression.py
      deep_neural_net.py
      …
    widgets/
      mainwindow.py
      settings_dialog.py
      …
    …
```

i.e. you will have a subfolder in your repository that contains your actual
python code, while the README, setup.py and other metadata reside in the
toplevel folder.

*An alternative convention is to put python code under a common `src` directory
which is nice once you have multiple toplevel modules or packages, and for
symmetry with `tests`, `docs` and perhaps other folders.*

**Example:**

The most prevalent way to declare python packages is by adding a `setup.py`
into the project's base directory. This file should at least list your python
modules, dependencies, as well as a name and version, but we'll provide a few
extra fields:

```python
from setuptools import setup

setup(
    name='SoccerForecast2000',          # package name
    author='Ronaldo MegaStar',          # original author
    author_email='ronaldo@fifa.com',
    maintainer='Kick It Like Beckham',  # current maintainer, if different
    # short one line description:
    description='Predict soccer game results using various regression algorithms',
    version='0.0.1',
    install_requires=[              # list of runtime dependencies
        'numpy>=1.9',               # with optional version specifiers
        'matplotlib',
        'PyQt5',
    ],
    py_modules=[
        'soccer_forecast_2000',     # toplevel module names, if any, without ".py"
    ],
    packages=[                      # package names, if any, plus subpackages
        'soccer',
        'soccer.widgets',
        'soccer.algorithms',
        'soccer.crawler',
    ],
)
```

Once you've set up this file, you can create and install your package as
follows:

```bash
python setup.py sdist       # create a *source package* in dist/ subfolder

pip install .               # install package defined in current directory
```

*You will often see `python setup.py install` as install instructions. Albeit
possible, you should in general use `pip install` instead! If you're
interested why, see e.g. [here](https://coldfix.de/2019/04/11/use-pip-for-install/).*

Next, we'll upload the package to [PyPI](https://pypi.org), which is a public
directory for community created python packages. The recommended tool for
uploading is [twine](https://twine.readthedocs.io/) which needs to be
installed separately.  We'll also install [wheel](https://pypi.org/project/wheel/),
which is a library that allows creating installer packages, so called *wheels*
(`*.whl` files):

```bash
pip install twine wheel
```

(You may need to add a --user flag if you're not in a virtualenv)

Now we come to the exciting part:

```bash
python setup.py sdist bdist_wheel     # create sdist and wheel

twine check dist/*                    # check created distributions
```

The second line is rather important to point out common issues with your
package files before publishing it on a public directory!

And finally, once you're done, you can publish your package as follows:

```bash
twine upload dist/<package-name>-<version>.tar.gz \
             dist/<package-name>-<version>-<platform>.whl
```

Of course, this only works after setting up a [PyPI](https://pypi.org) user
account.


---

**Links:** References and links to used materials and further reading

- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/), the official guide
