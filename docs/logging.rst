Improved messaging using logging
================================

What is *Logging*?
------------------

It can be useful  to print out either a message or the  value of some variable,
etc.,  while  your  code is  running.  This  is  quite  common and  is  usually
accomplished with a simple call to the ``print`` function.

.. code-block:: python

    x = 1.234
    print("The value of x is {0:0.4f}.".format(x))

::

    The value of x is 1.2340.

Doing this is a  good idea to keep track of milestones in  your code. That way,
both when you  are developing your code  but also when other  users are running
the code, they can be notified of an event, progress, or value.

Printing a message is also useful for  notifying the user when something is not
going as expected. These are all different *levels* of messaging.

*Logging* is  simply engaging in this  behavior of printing out  messages, with
the added  feature that you include  meta data (e.g., a  timestamp, the message
category) with the message, as well as a filter where only messages with a high
enough level of criticality is actually allowed to be printed.


Logging Basics
--------------

The general  idea is  that there are  multiple levels of  messages that  can be
Tprinted. ypically these include:

1. DEBUG    - used for diagnostic purposes.
2. INFO     - used for basic information (most common).
3. WARNING  - used for indicating non-normal behavior.
4. CRITICAL - used for indicating a problem (but program can continue).
5. ERROR    - used for exception messages (the program cannot continue).

During the initialization portion of your  code, you would configure a *logger*
object with a  format, where to print messages (e.g.,  console, file, or both),
and what level to use by default.  Usually, you would set the default log level
to ``INFO`` and the debugging messages  used for diagnostics would not actually
be printed. Then, allow the user to  override this with a command line argument
(e.g., ``--debug``).


Example Setup
-------------

Python has a `logging <https://docs.python.org/3/library/logging.html>`_ module
as part of the  standard library. It is very comprehensive  and allows the user
to heavily customize many parts of the behavior.

.. code-block:: python

    import logging

    log = logging.getLogger("ProjectName")

    file_handler = logging.FileHandler("path/for/output.log")
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(levelname)s %(asctime)s %(name)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(console_handler)
    log.setLevel(logging.INFO)

Then, somewhere in the code:

.. code-block:: python

    log.debug("report on some variable")
    log.info("notification of milestone")
    log.warn("non-standard behavior")
    log.critical("there is an issue")
    log.error("halting execution")

.. code-block:: none

    INFO 2018-07-24 09:41:56,683 ProjectName - notification of milestone
    WARNING 2018-07-24 09:41:56,835 ProjectName - non-standard behavior
    CRITICAL 2018-07-24 09:41:57,103 ProjectName - there is an issue
    ERROR 2018-07-24 09:41:57,103 ProjectName - halting execution

Notice that the debug  message was not printed. This is because  we set the log
level to  ``INFO``. Only  messages with  a level  equal to  or higher  then the
assigned level will make it passed the filter.


Using Color
-----------

Finally, another common feature  of logging is to add color  as an indicator of
the message type. Obviously, this only  applies to messages that are printed to
the console.  If you've ever started  up a *Jupyter* notebook  server you might
have noticed the logging messages it puts out a similar format as used here and
the meta data is a bold color. The color codes are generally as follows:

- DEBUG (blue)
- INFO (green)
- WARNING (orange or yellow)
- CRITICAL (purple)
- ERROR (red)

