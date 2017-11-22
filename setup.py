from distutils.core import setup
from linearizator import Metadata

metadata = Metadata()

long_description = """
Linearizator is compatible with **Python 2** and **Python 3**.

************************************
What can I do with Linearizator?
************************************

- Solve equation of line using 2 points
- Use solved equation to linearize values


Installation
============

You can install or upgrade linearizator with:

- ``$ pip install linearizator --upgrade``

Or you can install from source with:

- ``$ git clone https://github.com/RDCH106/linearizator.git --recursive``

- ``$ cd linearizator``

- ``$ python setup.py install``


Quick example
=============

``---------------------------------``

.. code-block:: python

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
   """

setup(
    name = 'linearizator',
    packages = ['linearizator'],
    version = metadata.get_version(),
    license = 'LGPL v3',
    description = 'Small library to solve linearization problems',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/RDCH106/linearizator',
    download_url = 'https://github.com/RDCH106/linearizator/archive/v'+metadata.get_version()+'.tar.gz',
    keywords = ['math', 'linearization'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)