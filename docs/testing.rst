Testing your code
=================

.. note::

   This section is based heavily on Ned Batchelder's
   excellent article and PyCon 2014 talk
   `Getting Started Testing <https://nedbatchelder.com/text/test0.html>`_.

   | *Tests are the dental floss of development: everyone knows they should do it more,*
   | *but they don’t, and they feel guilty about it.*
   | - Ned Batchelder

   | *Code without tests should be approached with a 10-foot pole.*
   | - me

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

Testing by example: ``flip_string``
-----------------------------------

Here is a function called ``flip_string`` that flips (reverses) a string.
There are bug(s) in this function that we need to find and fix.
Test the function for
various inputs and compare the results obtained with expected output.

.. literalinclude:: ../code/flip_string.py
   :caption: flip_string.py

* What tests did you come up with? Why did you choose those tests?
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
we need to remember all the tests came up with today
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
all the tests we come up with.

Testing with assertions
^^^^^^^^^^^^^^^^^^^^^^^

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

Useful tests
^^^^^^^^^^^^

Now that we know how to write and run tests,
what kind of tests should we write?
Testing ``flip_string`` for arbitrary words like ``'mario'`` and ``'luigi'``
might not tell us much about where the problem might be.

Instead, we should choose tests that exercise specific functionality
of the code we are testing,
or represent different conditions that the code may be exposed to.

Here are some examples of more useful tests:

* Flipping a string with a single character (no work needs to be done)
* Flipping a string with two characters (minmum amount of work needs to be done)
* Flipping a string that reads the same forwards and backwards

.. literalinclude:: ../code/test_flip_string-v5.py
   :caption: test_flip_string.py

:: 

   collected 3 items

   test_flip_string-v5.py ..F                                               [100%]

   =================================== FAILURES ===================================
   _____________________________ test_flip_palindrome _____________________________

       def test_flip_palindrome():
   >       assert flip_string('aba') == 'aba'
   E       AssertionError: assert 'a' == 'aba'
   E         - a
   E         + aba

   test_flip_string.py:10: AssertionError
   ====================== 2 failed, 1 passed in 0.08 seconds ======================

Fixing the code
^^^^^^^^^^^^^^^

From the test results above, we see that ``flip_string`` failed
for the input ``'aba'``.
Now, can you trace the execution of the code
in the function ``flip_string`` for this input
and figure out why it returned ``a``?

After fixing the code,
re-run the tests to make sure you didn't break anything else
in the process of fixing this bug -- this is one of the reasons tests are so valuable!

Types of testing
----------------

Software testing is a vast topic
and there are
`many levels and types <https://en.wikipedia.org/wiki/Software_testing>`_
of software testing.

For scientific and research software,
the focus of testing efforts is primarily:

1. **Unit tests**: Unit tests aim to test small, independent sections of code
   (a function or parts of a function),
   so that when a test fails,
   the failure can easily be associated with that section of code.
   This is the kind of testing that we have been doing so far.

2. **Regression tests**: Regression tests aim to check whether
   changes to the program result in it producing
   different results from before.
   Regression tests can test larger sections of code
   than unit tests.
   As an example, if you are writing a machine learning application,
   you may want to run your model on small data
   in an automated way
   each time your software undergoes changes,
   and make sure that the same (or a better) result is produced.

Test-driven development
-----------------------

`Test-driven development (TDD) <https://en.wikipedia.org/wiki/Test-driven_development>`_
is the practice of writing tests for a function or method
*before* actually writing any code for that function or method.
The TDD process is to:

1. Write a test for a function or method
2. Write just enough code that the function or method passes that test
3. Ensure that all tests written so far pass
4. Repeat the above steps until you are satisfied with the code

Proponents of TDD suggest that this results in better code.
Whether or not TDD sounds appealing to you,
writing tests should be *part* of your development process,
and never an afterthought.
In the process of writing tests,
you often come up with new corner cases for your code,
and realize better ways to organize it.
The result is usually code that is
more modular,
more reusable
and of course, more testable,
than if you didn't do any testing.

Growing a useful test suite
---------------------------

More tests are always better than less,
and your code should have as many tests as you are willing to write.
That being said,
some tests are more useful than others.
Designing a useful suite of tests is a challenge in itself,
and it helps to keep the following in mind when growing tests:

1. **Tests should run quickly**: testing is meant to be done as often as possible.
   Your entire test suite should complete in no more than a few seconds,
   otherwise you won't run your tests often enough for them to be useful.
   Always test your functions or algorithms on very small and simple data;
   even if in practice they will be dealing with more complex and large datasets.

2. **Tests should be focused**: each test should exercise a small part of your code.
   When a test fails, it should be easy for you
   to figure out which part of your program you need to focus debugging efforts on.
   This can be difficult if your code isn't modular,
   i.e., if different parts of your code depend heavily on each other.
   This is one of the reasons TDD is said to produce more modular code.
   
3. **Tests should cover all possible code paths**: if your function has multiple code paths
   (e.g., an if-else statement), write tests that execute both the "if" part
   and the "else" part.
   Otherwise, you might have bugs in your code and still have all tests pass.

4. **Test data should include difficult and edge cases**: it's easy to
   write code that only handles cases with well-defined inputs and outputs.
   In practice however, your code may have to deal with
   input data for which it isn't clear what the behaviour should be.
   For example, what should ``flip_string('')`` return?
   Make sure you write tests for such cases,
   so that you force your code to handle them.
