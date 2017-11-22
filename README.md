# Linearizator

[![PyPI](https://img.shields.io/pypi/v/linearizator.svg)](https://pypi.python.org/pypi/linearizator)
[![PyPI](https://img.shields.io/pypi/pyversions/linearizator.svg)](https://pypi.python.org/pypi/linearizator)
[![PyPI](https://img.shields.io/pypi/l/linearizator.svg)](https://github.com/RDCH106/linearizator/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/442feb0ba62c44c7900e33e773cde6f8)](https://www.codacy.com/app/RDCH106/linearizator?utm_source=github.com&utm_medium=referral&utm_content=RDCH106/linearizator&utm_campaign=badger)
[![Build Status](https://travis-ci.org/RDCH106/linearizator.svg?branch=master)](https://travis-ci.org/RDCH106/linearizator)

Small library to solve linearization problems.

Linearizator is compatible with Python 2 and Python 3.

### What can I do with Linearizator?

- Solve equation of line using 2 points
- Use solved equation to linearize values

### Installation

You can install or upgrade linearizator with:

`$ pip install linearizator --upgrade`

Or you can install from source with:

```
$ git clone https://github.com/RDCH106/linearizator.git --recursive
$ cd linearizator
$ python setup.py install
```

### Quick example

```python
from linearizator import linearizator

# Initialize linearizator object
lin = linearizator.Linearizator(x1=6.4, y1=20, x2=16.8, y2=85, unknown="y")

# Linearize
lin.linearize()

# Show equation of line
print(lin.pretty_equation())

# Calculate the value of a point
print(lin.calculate(6.4))

# Generate inverse linearization
lin.inverse()

# Show equation of line
print(lin.pretty_equation())

# Calculate the value of a point
print(lin.calculate(20))

```
