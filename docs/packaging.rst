Writing a Python Package
========================

We want to write some code that
plots triangles:

.. image:: images/triangle.png
   :width: 50%

How to structure a Python project?
----------------------------------

How you choose organize the code for your project is an incredibly important decision.
Well structured code is:

* easier to navigate and make changes to
* easier to reuse
* easier to test
* more likely to be used by others

One way to organize your code
is to put all of it
in a single ``.py`` file (module),
including (optionally) executable "top-level" code.

.. code-block:: python
    :caption: main.py 

    import matplotlib.pyplot as plt

    def draw_triangle(coords, ax=None):
        if ax is None:
            ax = plt.gca()
        else:
            fig, ax = plt.subplots()
       patch = plt.Polygon(coords)
       ax.add_patch(patch)
       return ax

    if __name__ == "__main__":
        draw_triangle([
            (0.2, 0.2),
            (0.2, 0.6),
            (0.4, 0.4)])

Multiple modules that each
contain related data and functionality:

.. code-block:: python 
   :caption: shapes.py

   import matplotlib.pyplot as plt

   def draw_triangle(coords, ax=None):
       if ax is None:
           ax = plt.gca()
       else:
           fig, ax = plt.subplots()
       patch = plt.Polygon(coords)
       ax.add_patch(patch)
       return ax

.. code-block:: python 
   :caption: main.py
     
   import shapes
   shapes.draw_triangle([
       (0.2, 0.2),
       (0.2, 0.6),
       (0.4, 0.4)])

3. As a **package**.
   A Python package is a directory containing
   a file called ``__init__.py``.
   Any module in this directory can be imported
   using the "dot" notation:

   .. code-block:: bash
      
      geometry
      ├── __init__.py
      └── shapes.py 

   .. code-block:: python
  
      from geometry.shapes import draw_triangle
      draw_triangle(args)

Making your project installable
-------------------------------

To improve their reusability,
you typically want to be able to
``import`` your modules and packages
from anywhere,
i.e., from any directory on your computer.

One way to do this that is **not** recommended
is to use ``sys.path``:

.. code-block:: python

   import sys
   sys.path.append('/path/to/geometry')

   import shapes

``sys.path`` is a list of directories
that Python looks for modules and packages in
when you ``import`` them.

A better way is to make your package installable
using
`setuptools <https://setuptools.readthedocs.io/en/latest/>`_.
To do this, you will need to
include a ``setup.py`` with your project.
Your project should be organized as follows:

.. code-block:: bash

   geometry
   ├── geometry
   │   ├── __init__.py
   │   └── shapes.py
   └── setup.py

A minimal ``setup.py`` can include the following

.. code-block:: python 
   :caption: setup.py

   from setuptools import setup

   setup(name='geometry',
      version='0.1',
      author='Ashwin Srinath',
      packages=['geometry'])

You can install the package using ``pip``
with the following command
(run from the same directory as ``setup.py``):

.. code-block:: bash

   $ pip install -e . --user

This installs the package in *editable* mode,
creating a link to it in the user's ``site-packages`` directory,
which happens to be in ``sys.path``.
