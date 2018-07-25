Documenting your code
=====================

Most people think of writing documentation as
an unpleasant, but necessary task,
done for the benefit of othe people
with no real benefit to themselves.
So they choose not to do it,
or they do it with little care.

But even if you are the only person who will ever use your code,
it's still a good idea to document it well.
Being able to document your own code gives you confidence that you understand it yourself,
and a sign of well-written code is that it can be easily documented.
Code you wrote a few weeks ago
may as well have been written by someone else,
and you will be glad that you documented it.

The good news is that writing documentation can be fun,
and you really don't need to write a lot of it.

Docstrings and comments
-----------------------

Documentation is *not* comments.

A *docstring* in Python is a string literal
that appears at the beginning of a module, function, class, or method.

.. code-block:: python

   """
   A docstring in Python that appears
   at the beginning of a module, function, class or method.
   """

The *docstring* of a module, function, class or method
becomes the ``__doc__`` attribute of that object,
and is printed if you type ``help(object)``:

.. code-block:: python

   In [1]: def fahr_to_celsius(F):
      ...:     """
      ...:     Convert temperature from Fahrenheit to Celsius.
      ...:     """
      ...:     return (F - 32) * (5/9)

   In [2]: help(fahr_to_celsius)

   Help on function fahr_to_celsius in module __main__:

   fahr_to_celsius(F)
    Convert temperature from Fahrenheit to Celsius. 

A *comment* in Python is any line that begins with a ``#``:

.. code-block:: python

   # a comment.

The purpose of a docstring is to document a module, function, class, or method.
The purpose of a comment is to explain a very difficult piece of code,
or to justify a choice that was made while writing it.

Docstrings should not be used in place of comments,
or vice versa. **Don't do the following**:

.. code-block:: python

   In [1]: def fahr_to_celsius(F):
      ...:     # Convert temperature from Fahrenheit to Celsius.
      ...:     return (F - 32) * (5/9)

Deleting code
^^^^^^^^^^^^^

Incidentally, many people use comments and string literals
as a way of "deleting" code - also known as *commenting out* code.
See `this article <https://nedbatchelder.com/text/deleting-code.html>`_ on a better way to delete code.

What to document?
-----------------

So what goes in a dosctring?

At minimum, the docstring for a function or method should consist of the following:

1. A **Summary** section that describes in a sentence or two
   what the function does.
2. A **Parameters** section that provides a
   description of the parameters to the function,
   their types,
   and default values (in the case of optional arguments).
3. A **Returns** section that similarly describes the return values.
4. Optionally,
   a **Notes** section that describes the implementation,
   and includes references.

Here is a simple example of this in action:

.. literalinclude:: ../code/flip_list-v1.py

NumPy's `documentation guidelines <https://numpydoc.readthedocs.io/en/latest/>`_ are a great
reference for more information about what and how to document your code.

Doctests
--------

In addition to the sections above,
your documentation can also contain runnable tests.
This is possible using the
`doctest <https://docs.python.org/3/library/doctest.html>`_ module.

.. literalinclude:: ../code/flip_list-v2.py
   :caption: flip_list.py

You can tell ``pytest`` to run doctests as well as other tests
using the ``--doctest-modules`` switch:

::

   $ pytest --doctest-modules flip_list.py

   collected 1 item

   flip_list.py .                                                            [100%]

   =========================== 1 passed in 0.03 seconds ===========================

Doctests are great because they double up
as documentation as well as tests.
But they shouldn't be the *only* kind of tests you write.

Documentation generation
------------------------

Finally, you can turn your documentation into a beautiful website (like this one!),
a PDF manual, and various other formats,
using a document generator such as
`Sphinx <http://www.sphinx-doc.org/en/master/>`_.
You can use services like
`readthedocs <http://readthedocs.org/>`_
to build and host your website for free.
