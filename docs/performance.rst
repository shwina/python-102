Improving the performance of Python programs
============================================

Here are some general recommendations for improving
the performance of your code:

Identify bottlenecks
^^^^^^^^^^^^^^^^^^^^

This is often the most important step.

Choosing the right algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When choosing a function from a library
or writing your own,
ensure that  you understand how it will perform
for the type and size of data you have,
and what its limitations are.

For example,
if you are doing linear algebra
with very large matrices containing very few non-zero values,
you might find much better performance
using
`sparse <https://en.wikipedia.org/wiki/Sparse_matrix>`_ matrices
and algorithms compared to the dense matrix format.

Always benchmark to compare with other libraries/functions.

Accessing and operating on data efficiently
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In programming,
there are often many ways to achive the same result.
These methods may vary in the way data is accessed and operated on,
and sometimes this can lead to significant performance differences.

For example, let's say we want to compute the average
``hindfooth_length`` for all species in ``plot_id`` 13 in the following dataset:

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

Avoiding explicit loops
^^^^^^^^^^^^^^^^^^^^^^^

Very often, you need to operate on multiple elements of a collection
such as a
NumPy array or
Pandas DataFrame.

In such cases, it is almost always a bad idea to write
an explicit ``for`` loop over the elements.

For instance, looping over the rows (a.k.a, *indices* or *records*)
of a Pandas DataFrame is considered poor practice, and is very slow.
Consider replacing values in a column of a dataframe:

.. code-block:: python

    In [1]: %%time
       ...: for row in range(data.shape[0]):
       ...:     if data.loc[row, 'species_id'] == 'NL':
       ...:         data.loc[row, 'species_id'] = 'NZ'
       ...:
    CPU times: user 3.95 s, sys: 12.5 ms, total: 3.96 s
    Wall time: 3.97 s

Doing this with a ``for`` loop takes about 4 seconds on my computer.
Of course, a much better way to do this is
simply to use the ``replace()`` method:

.. code-block:: python

    In [2]: %time data['species_id'].replace('NL', 'NZ', inplace=True)
    CPU times: user 3.1 ms, sys: 652 µs, total: 3.75 ms
    Wall time: 3.34 ms

In addition to being faster,
this also leads to much more readable code.

Reading and writing data efficiently
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A typical bottleneck is when your code reads or writes data from disk
(i.e., from a file), especialy for large files or frequent reads/writes.
Some considerations for I/O are:

1. **Use the appropriate data format**: Familiarize yourself with
   the various data formats available for the type of data you are dealing with,
   and the performance considerations for each.
   For example,
   `this page <https://pandas.pydata.org/pandas-docs/stable/io.html>`_
   provides a good overview of various data formats for tabular data
   supported by the Pandas library.
   Performance for each is reported
   `here <https://pandas.pydata.org/pandas-docs/stable/io.html#performance-considerations>`_.

2. **Avoid writing your own readers and writers**: Resist any temptation
   to write your own code for reading and writing data from files,
   and instead rely on other well-tested and well-used implementations.

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

   But the performance of such code is extremely poor. Compare with the
   Pandas' ``read_csv`` function:

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

3. If you are using a high-performance computing cluster,
   it becomes important to consider whether data is read from and written to
   a shared *network file system* (NFS), which are very common in HPC settings.
   On such systems,
   it is much more efficient to perform large, less frequent reads/write operations as opposed
   to small, frequent ones.



Parallelization
^^^^^^^^^^^^^^^


