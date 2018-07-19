Improving the performance of Python programs
============================================

Programming for performance
and parallel programming are vast topics
that could easily take
an entire workshop, or a semester-long course.
This section covers the essentials
and some useful tools.

Your code may take longer than you'd like for
many different reasons.
Here are some common ways
to speed up code:

Accessing and operating on data efficiently
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In programming,
there are often many ways to achive the same result.
Sometimes, different methods may vary significantly in performance.

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
As an example, consider replacing values in a dataframe:

.. code-block:: python

    In [1]: %%time
       ...: for row in range(data.shape[0]):
       ...:     if data.loc[row, 'species_id'] == 'NL':
       ...:         data.loc[row, 'species_id'] = 'NZ'
       ...:
    CPU times: user 3.95 s, sys: 12.5 ms, total: 3.96 s
    Wall time: 3.97 s

The ``for`` loop takes about 4 seconds on my computer.
Of course, a much better way to do this is
simply to use the ``replace()`` method:

.. code-block:: python

    In [2]: %time data['species_id'].replace('NL', 'NZ', inplace=True)
    CPU times: user 3.1 ms, sys: 652 µs, total: 3.75 ms
    Wall time: 3.34 ms

In addition to being faster,
this also leads to much more readable code.

