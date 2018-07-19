Testing your code
=================

Here is a naïve function called ``strflip`` that flips a string.
There are bug(s) in this code.
To proceed, try testing the code
for various inputs and compare the results obtained with expected output.

.. code-block:: python
   :caption: strflip.py

    def strflip(s):
        """
        strflip: Flip a string

        Parameters
        ----------
        s : str
            String to reverse

        Returns
       -------
        flipped : str
            Copy of `s` with characters arranged in reverse order
        """
     
        flipped = ''

        # Starting from the last character in `s`,
        # add the character to `flipped`,
        # and proceed to the previous character in `s`.
        # Stop whenever we reach the first character.

        i = len(s)

        while True:
            i = i-1
            char = s[i]
            flipped = flipped + char

            # stop if we have reached the first character:
            if char == s[0]:
               break

        return flipped

* What did you find?
* What test cases did you come up with? Why did you choose those test cases?
* How did you organize and execute your tests?
* Can the results of your tests help you figure out what problem(s) there might be
  with the code?

Testing interactively
---------------------

.. code-block:: python
   
    >>> from strflip import strflip
    >>> strflip('mario')
    'oiram'
    >>> strflip('luigi')
    'igiul'

Testing using ``assert``
------------------------

.. code-block:: python

    >>> assert strflip('mario') == 'oiram'
    >>> assert strflip('luigi') == 'igiul'

Testing using ``pytest``
------------------------

.. code-block:: python
   :caption: test_strflip.py

    from strflip import strflip

    def test_flip_empty_string():
        assert strflip('') == ''

    def test_flip_one_char():
        assert strflip('a') = 'a'

    def test_flip_repeated_char():
        assert strflip('abca') == 'acba'

.. code-block:: bash
     
    $ pytest

    collected 3 items

    code/test_strflip.py ..F                                             [100%]

    ================================= FAILURES =================================
    _________________________ test_flip_repeated_char __________________________

    def test_flip_repeated_char():
    >       assert strflip('abca') == 'acba'
    E       AssertionError: assert 'a' == 'acba'
    E         - a
    E         + acba
     code/test_strflip.py:10: AssertionError
    ==================== 1 failed, 2 passed in 0.12 seconds ====================

* Good tests run quickly
* Test exhaustively
* Test for corner cases
* If you encounter a bug,
  write a test for it first
* Test before committing code
