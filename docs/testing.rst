Testing your code
=================

.. note::

   This section is based heavily on Ned Batchelder's
   excellent article and PyCon 2014 talk
   `Getting Started Testing <https://nedbatchelder.com/text/test0.html>`_.

How can you write
modular, extensible, and reusable code?

After making changes to a program,
how do you ensure that
it will still give the same answers as before?

How can we make finding and fixing bugs
an easy, fun and rewarding experience? 

These seemingly unrelated questions all
have the same answer,
and it is
**automated testing**.

An example: ``flip_string``
---------------------------

Here is a function called ``flip_string`` that flips (reverses) a string.
There are bug(s) in this function that we need to find and fix.
Test the function for
various inputs and compare the results obtained with expected output.

.. literalinclude:: ../code/flip_string.py
   :caption: flip_string.py

* What test cases did you come up with? Why did you choose those test cases?
* How did you organize and execute your tests?
* Can the results of your tests help you figure out what problem(s)
  there might be with the code?

Testing interactively
^^^^^^^^^^^^^^^^^^^^^

This is the most common type of testing,
and something you have probably done before.
To test a function or a line of code,
you simply fire up an interactive Python interpreter,
import the function,
and test away:

.. code-block:: python

   >>> from flip_string import flip_string
   >>> flip_string('mario')
   'oiram'
   >>> flip_string('luigi')
   'igiul'

While this kind of testing is better than not doing any testing at all,
it leaves much to be desired.
First,
it needs to be done
each time ``flip_string`` is changed.
It also requires that we manually inspect the output from each test to
decide if the code "passes" or "fails" that test.
Further,
we need to remember all the test cases we came up with today
if we want to test again tomorrow.

Writing a test script
^^^^^^^^^^^^^^^^^^^^^

A *much* better way to write tests is to put them in a script:

.. literalinclude:: ../code/test_flip_string-v1.py
   :caption: test_flip_string.py

Now, running and re-running our tests is very easy - we just run the script:

.. code-block:: bash

   $ python test_flip_string.py
   mario flipped is: oiram
   luigi flipped is: igiul

It's also easy to add new tests,
and there's no need to remember
all the test cases we come up with.

Testing using assertions
^^^^^^^^^^^^^^^^^^^^^^^^

One problem with the method above is that
we *still* need to manually inspect the results of our tests.

Assertions can help with this.

The ``assert`` statement in Python is very simple:
Given a condition, like ``1 == 2``,
it checks to see if the condition is true or false.
If it is true, then ``assert`` does nothing,
and if it false, it raises an ``AssertionError``:

.. code-block:: python

   >>> assert 1 == 1
   >>> assert 1 < 2
   >>> assert 1 > 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AssertionError

We can re-write our script ``test_flip_string.py``
using assertions as follows:

.. literalinclude:: ../code/test_flip_string-v2.py
   :caption: test_flip_string.py

And we still run our tests the same way:

.. code-block:: bash

   $ python test_flip_string.py

This time, there's no need to inspect the test results.
If we get an ``AssertionError``, then we had a test fail,
and if not, all our tests passed.

However, there's no way to know if *more* than one test failed.
The script stops executing after the first ``AssertionError`` is encountered.

Let's add another test to our test script and re-run it:

.. literalinclude:: ../code/test_flip_string-v3.py
   :caption: test_flip_string.py

.. code-block:: bash

   $ python test_flip_string.py

   Traceback (most recent call last):
     File "test_flip_string.py", line 5, in <module>
       assert flip_string('samus') == 'sumas'
   AssertionError

This time we get a failed test,
because - as we said - our code has bugs in it.
Before adding more tests to investigate further,
we'll discuss one more method for running tests.

Using a test runner
^^^^^^^^^^^^^^^^^^^

A test runner takes a bunch of tests,
executes them all,
and then reports which of them passed
and which of them failed.

A very popular test runner for Python is
`pytest <https://docs.pytest.org/en/latest/>`_.

To run our tests using pytest,
we need to re-write them as follows
(essentially, wrap each test in a function):

.. code-block:: python
   :caption: test_flip_string.py

    from flip_string import flip_string

    def test_flip_mario():
        assert flip_string('mario') == 'oiram'

    def test_flip_luigi():
        assert flip_string('luigi') = 'igiul'

    def test_flip_samus():
        assert flip_string('samus') == 'sumas'

To run our tests,
we simply type ``pytest`` on the command line.
When we do this, pytest will
look for all files containing tests,
run all the tests in those files,
and report what it found:

.. code-block:: bash

   $ pytest

   collected 3 items

   test_flip_string.py ..F                                               [100%]

   =================================== FAILURES ===================================
   _______________________________ test_flip_samus ________________________________

       def test_flip_samus():
   >       assert flip_string('samus') == 'sumas'
   E       AssertionError: assert 's' == 'sumas'
   E         - s
   E         + sumas

   test_flip_string.py:10: AssertionError
   ====================== 1 failed, 2 passed in 0.07 seconds ======================

As you can see above,
pytest prints a lot of useful information in its report.
First,
it prints a summary of passed v/s failed tests:

::

    test_flip_string.py ..F                                               [100%]

A dot (``.``) indicates a passed test,
while a ``F`` indicates a failed test.


For each failed test,
it provides further information,
including the
expected value as well as the obtained value
in the failed assertion:

::

    =================================== FAILURES ===================================
    _______________________________ test_flip_samus ________________________________
    
        def test_flip_samus():
    >       assert flip_string('samus') == 'sumas'
    E       AssertionError: assert 's' == 'sumas'
    E         - s
    E         + sumas
    
    test_flip_string.py:10: AssertionError


