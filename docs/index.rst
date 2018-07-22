.. python-102 documentation master file, created by
   sphinx-quickstart on Thu Jul 12 10:12:51 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python 102 for scientific computing and data analysis
=====================================================

This tutorial covers topics that are
essential for scientific computing and data analysis in Python,
but typically *not* covered in an introductory course or workshop.

These are topics you *need* to know if you are writing software
that meets any of the following criterial:

* You expect to be working on it for more than a couple of weeks.`
* You want it to produce results
  that can be trusted "beyond reasonable doubt" - e.g.,
  if you are publishing a research paper based on those results.
* You expect that it will be composed of more than a hundred
  or so lines of code.
* You expect that it will be used by one or more other people
* You are contributing to another project - e.g., an open-source
  software package.

What you will learn
-------------------

1. How to organize code in your project,
   and how to make it an installable *package*
   rather than a loose collection of files.
2. How to write tests for your code so that
   you can be sure it always produces the correct answer,
   even after you make changes to it.
3. How to document your code so that it is easy for
   you and others to use and navigate.
4. How to improve the performance of your code.


What you need to know
---------------------

This tutorial assumes you know the very basics
of programming with Python.
If you can write a loop and a function in Python,
and if you know how to run a ``.py`` script,
you should be able to follow this tutorial easily.

What you need to have
---------------------

If you plan to participate in the hands-on exercises,
you will need:

* 1 laptop
* .. with `Anaconda <https://www.anaconda.com/download/>`_ installed on it
* 1 or more friends.
  It is **highly** encouraged to work in groups,
  so if you haven't already,
  please introduce yourself to your neighbour(s).

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   packaging
   testing
   performance


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
