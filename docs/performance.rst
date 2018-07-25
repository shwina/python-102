Improving the performance of Python programs
============================================

Timing code and identifying bottlenecks
---------------------------------------

Of course,
the first step toward improving performance
is to figure out where to focus your efforts.
This means identifying the section of code in your program
that is taking the most time,
i.e., the "bottleneck".

Sometimes,
the bottleneck is very obvious
(e.g., the training step in a machine learning application),
and sometimes it may not be clear.
In the latter case,
you need to be able to measure the time taken by various parts of your program.

The ``time`` function
^^^^^^^^^^^^^^^^^^^^^

The `time <https://docs.python.org/3/library/time.html#time.time>`_
function can be used to time a section of code as follows:

.. code-block:: python

   import time
   import numpy as np

   t1 = time.time()
   a = np.random.rand(5000, 5000)
   t2 = time.time()
   print("Generating random array took {} seconds".format(t2-t1))

::

   Generating random array took 0.44880104064941406 seconds


``%timeit`` and ``%%timeit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``%timeit%`` and ``%%timeit`` are
`magic statements <https://ipython.readthedocs.io/en/stable/interactive/magics.html>`_
that can be used in IPython
or in Jupyter Notebook
for timing a single line of code or a block of code
conveniently:

::
    
   In [1]: import numpy as np

   In [2]: %timeit np.random.rand(5000, 5000)
   410 ms ± 2.59 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

   In [3]: %%timeit
      ...: a = np.random.rand(5000, 5000)
      ...: b = np.random.rand(5000, 5000)
      ...: c = a * b
      ...:
   897 ms ± 10.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Profilers
^^^^^^^^^

``time`` and ``timeit`` should help with most of your measurement needs,
but if you need to profile a very long program with lots of functions,
you may benefit from using
a  `profiler <https://docs.python.org/3/library/profile.html>`_.

There is also a
`line_profiler <https://github.com/rkern/line_profiler>`_
that can help you automatically profile
each line in a script,
and a `memory_profiler <https://github.com/pythonprofilers/memory_profiler>`_
to measure memory consumption.

Install optimized versions of libraries
---------------------------------------

This is the easiest way to get "free" performance improvements.
If your computer supports it,
install optimized version of Python libraries,
for example, those provided by
the `Intel Distribution for Python <https://software.intel.com/en-us/distribution-for-python>`_.

Another option is `PyPy <https://pypy.org/compat.html>`_.

Choose the right algorithm
--------------------------

This is one of the most effective ways to
improve the performance of a program.

When choosing a function from a library
or writing your own,
ensure that  you understand how it will perform
for the type and size of data you have,
and what options there may be to boost its performance.
Always benchmark to compare with other functions and libraries.

For example,
if you are doing linear algebra,
you may benefit from the use of
`sparse <https://en.wikipedia.org/wiki/Sparse_matrix>`_ matrices and algorithms
if you are dealing with very large matrices with relatively few non-zeros.

As another example, many kinds of algorithms are iterative
and require an initial "guess" for the solution.
Typically, the closer this initial guess is to the actual solution,
the faster the algorithm performs.

Choose the appropriate data format
----------------------------------

Familiarize yourself with
the various data formats available for the type of data you are dealing with,
and the performance considerations for each.
For example,
`this page <https://pandas.pydata.org/pandas-docs/stable/io.html>`_
provides a good overview of various data formats for
tabular data supported by the Pandas library.
Performance for each is reported
`here <https://pandas.pydata.org/pandas-docs/stable/io.html#performance-considerations>`_.

Don't reinvent the wheel
------------------------

Resist any temptation
to write your own implementation for a
common task or a well-known algorithm.
Rely instead on other well-tested and well-used implementations.

For instance, it's easy to write a few lines of Python to
read data from a ``.csv`` file into a Pandas DataFrame:
   
.. code-block:: python
   :caption: my_csv.py

   def read_csv(fname):
       with open(fname) as f:
           col_names = f.readline().rstrip().split(',')
           df = pandas.DataFrame(columns=col_names)
               for line in f:
                   record = pandas.DataFrame([line.rstrip().split(',')], columns=col_names)
                   df = df.append(record, ignore_index=True)
       return df

But such code performs poorly.
Compare the performance with Pandas' ``read_csv`` function:

.. code-block:: python

   In [1]: from my_csv import read_csv

   In [2]: %time data = read_csv('feet.csv')
   CPU times: user 2min 3s, sys: 1.39 s, total: 2min 4s
   Wall time: 2min 5s

.. code-block:: python
   
   In [1]: from pandas import read_csv

   In [2]: %time data = read_csv('feet.csv')
   CPU times: user 28.5 ms, sys: 10.8 ms, total: 39.3 ms
   Wall time: 54.2 ms

It also isn't nearly as versatile,
and doesn't account for the dozens of edge cases than Pandas does.

Benchmark, benchmark, benchmark!
--------------------------------

If there are two ways of doing the same thing,
*benchmark* to see which is faster for different problem sizes.

For example, let's say we want to compute
the average ``hindfooth_length`` for
all species in ``plot_id`` 13 in the following dataset:

.. code-block:: python

    In [1]: data = pandas.read_csv('feet.csv')

    In [2]: data.head()
    Out[2]:
       plot_id species_id  hindfoot_length
    0        2         NL             32.0
    1        3         NL             33.0
    2        2         DM             37.0
    3        7         DM             36.0
    4        3         DM             35.0

One way to do this would be to group by the ``plot_id``,
compute the mean hindfoot length for each group,
and extract the result for the group with ``plot_id`` 13:

.. code-block:: python

    In [2]: data.groupby('plot_id')['hindfoot_length'].mean()[13]
    Out[2]: 27.570887035633056

Another way would be to filter the data first,
keeping only records with ``plot_id`` 13,
and then computing the mean of the ``hindfoot_length`` column:

.. code-block:: python

    In [3]: data[data['plot_id'] == 13]['hindfoot_length'].mean()
    Out[3]: 27.570887035633056

Both methods give identical results,
but the difference in performance is significant:

.. code-block:: python

    In [4]: %timeit data.groupby('plot_id')['hindfoot_length'].mean()[13]
    1.34 ms ± 24.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

    In [5]: %timeit data[data['plot_id'] == 13]['hindfoot_length'].mean()
    750 µs ± 506 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)

Why do you think the first method is slower?

Avoid explicit loops
--------------------

Very often, you need to operate on multiple elements of a collection
such as a
NumPy array or
Pandas DataFrame.

In such cases, it is almost always a bad idea to write
an explicit ``for`` loop over the elements.

For instance,
looping over the rows (a.k.a, *indices* or *records*)
of a Pandas DataFrame is considered poor practice,
and is very slow.
Consider replacing values in a column of a dataframe:

.. code-block:: python

   In [5]: %%timeit
      ...: for i in range(len(data['species_id'])):
      ...:     if data.loc[i, 'species_id'] == 'NL':
      ...:         data.loc[i, 'species_id'] = 'NZ'
      ...:
   308 ms ± 4.49 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

A better way to do this is
simply to use the ``replace()`` method:

.. code-block:: python

    In [2]: %time data['species_id'].replace('NL', 'NZ', inplace=True)
    CPU times: user 3.1 ms, sys: 652 µs, total: 3.75 ms
    Wall time: 3.34 ms

In addition to being faster,
this also leads to more readable code.

Of course, loops are unavoidable in many situations;
but look for alternatives before you write a ``for`` loop
over the elements of an array, DataFrame, or similar data structure.

Avoid repeatedly allocating, copying and rearranging data
---------------------------------------------------------

Repeatedly creating and destroying new data can be very expensive
especially if you are working with very large arrays or data frames.
So avoid, for instance, creating a new array each time inside a loop.
When operating on NumPy arrays,
memory is allocated for intermediate results.
Packages like `numexpr <https://github.com/pydata/numexpr>`_ aim to help with this.

Understand when data needs to be copied v/s when data can be operated "in-place".
It also helps to know *when* copies are made.
For example, do you think
the following code results in two copies of the same array?

.. code-block:: python

   import numpy as np

   a = np.random.rand(50, 50)
   b = a

`This article <https://nedbatchelder.com/text/names.html>`_
clears up a lot of confusion
about how names and values work in Python
and when copies are made v/s when they are not.

Access data from memory efficiently
-----------------------------------

Accessing data in the "wrong order":
it is always more efficient to access values that are
"closer together" in memory than values that are farther apart.
For example, looping over the elements along the rows of a 2-d NumPy array
is *much* more efficient than looping over the elements along its columns.
Similarly, looping over the columns of a DataFrame in Pandas will be faster
than looping over its rows.

* Redundant computations / computing "too much":
  if you only need to compute on a subset of your data,
  filter *before* doing the computation
  rather than after.


Interfacing with compiled code
------------------------------

You may have heard that Python is "slow"
compared to other languages like C, C++, or Fortran.
This is somewhat true in that Python programs
written in "pure Python", i.e., without the use
of any libraries except the standard libraries,
will be slow compared to their C/Fortran counterparts.
One of the reasons that C is so much faster than Python
is that it is a
`compiled language <https://en.wikipedia.org/wiki/Compiled_language>`_,
while Python is an
`interpreted language <https://en.wikipedia.org/wiki/Interpreted_language>`_.

However,
the core of libraries like NumPy
are actually written in C,
making them much faster than "pure Python".

It's also possible for you to write your own code
so that it interfaces with languages like C, C++ or Fortran.
Better still,
you often don't even need to write any code in those languages,
and instead can have other libraries "generate" them for you.

`Numba <https://numba.pydata.org/>`_ is a library that lets you compile
code written in Python using
a very convenient "decorator" syntax.

As an example,
consider numerically evaluating the derivative
of a function using finite differences.
A function that uses NumPy to do this might look like the following:

.. literalinclude:: ../code/derivatives.py
   :language: python
   :caption: derivatives.py

Below, we time the function for a grid of 10000000 points:

:: 

   In [1]: x = np.linspace(0, 1, 10000000)

   In [2]: dx = x[1] - x[0]

   In [3]: f = np.sin(2 * np.pi * x / 1000000)

   In [4]: y = np.zeros_like(f)

   In [5]: %timeit dfdx(f, dx, y)
   61.1 ms ± 2.62 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

Below is a function that is compiled using Numba to do the same task:

.. literalinclude:: ../code/derivatives_numba.py
   :language: python
   :caption: derivatives.py

We see much better performance for the same grid size:

::

   In [1]: %timeit dfdx(f, dx, y)
   14.6 ms ± 282 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

`Cython <http://cython.org/>`_ is another option for interfacing with compiled code.
It performs about the same as Numba but requires much more effort;
although it can do many things that Numba cannot,
such as generating C code, and
interface with C/C++ libraries.

Parallelization
---------------

Finally,
if your computer has multiple cores,
or if you have access to a bigger computer (e.g., a high-performance computing cluster),
parallelizing your code may be an option.

* Note that many libraries support parallelization without any effort on your part.
  Libraries like Numba and `Tensorflow <https://www.tensorflow.org/>`_
  can use all the cores on your CPU,
  and even your GPU for accelerating computations.

* `Dask <https://dask.pydata.org/en/latest/>`_ is a great library for
  parallelizing computations
  and operating on large datasets that don't fit in RAM.

* The `multiprocessing <https://docs.python.org/3/library/multiprocessing.html>`_ package
  is useful when you have several independent tasks that can all be done concurrently.
  `joblib <https://pythonhosted.org/joblib/>`_ is another popular library for this.

