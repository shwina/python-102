Improving the usability of Python programs
==========================================

Logging
-------

What is *Logging*?
^^^^^^^^^^^^^^^^^^

It can be useful  to print out either a message or the  value of some variable,
etc.,  while  your  code is  running.  This  is  quite  common and  is  usually
accomplished with a simple call to the ``print`` function.

.. code-block:: python

    x = 1.234
    print("The value of x is {0:0.4f}.".format(x))

.. code-block:: none

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
^^^^^^^^^^^^^^

The general  idea is  that there are  multiple levels of  messages that  can be
printed. Typically these include:

1. DEBUG    - used for diagnostic purposes.
2. INFO     - used for basic information (most common).
3. WARNING  - used for indicating non-normal behavior.
4. CRITICAL - used for indicating a problem (but program can continue).
5. ERROR    - used for exception messages (the program cannot continue).

During the initialization portion of your  code, you would configure a *logger*
object with a  format, where to print messages (e.g.,  console, file, or both),
and what level to use by default.  Usually, you would set the default log level
to ``INFO`` and the debugging messages  used for diagnostics would not actually
be printed. Then, allow the user to override this with a `command line argument
<#command-line-arguments>`_ (e.g., ``--debug``).


Example Setup
^^^^^^^^^^^^^

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


Logging with Color
^^^^^^^^^^^^^^^^^^

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


Command Line Arguments
----------------------

In addition to  packaging your code in  a way that other users  or projects can
import for use in their code, often it makes sense to also make elements of the
code  executable from  the  command line  as stand  alone  scripts. Python  has
everything you need to do this built right in.

As   with  logging,   there  are   several  python   packages  available   that
handle   command  line   argument   parsing  for   you,   including  a   robust
implementation   provided   right  in   the   standard   library  -   `argparse
<https://python.org/argparse>`_.

The *argparse*  module, as  well as  the others, rely  on a  universally except
convention for how  command line arguments should be structured.  Nearly all of
the  standard  utilities on  Unix/Linux  systems  use  this same  syntax.  This
convention covers both the command line argument syntax as well as the stucture
of *usage*  statements that your  script prints  out (e.g., when  supplying the
``--help`` option).  The *argparse* module actually  takes care of all  of this
for you.

Unix Convension
^^^^^^^^^^^^^^^

There is a fair bit of complexity to the convention surrounding the *usage* 
statetments, but the argument syntax is fairly simple.

*Positional arguments* are those that don't have names. These are usually file
paths in the context of analysis scripts.

...

Simple Example
^^^^^^^^^^^^^^

The easiest way to  provide a stand alone script as part of  your package is to
define  the  script within  a  ``.py``  file inside  of  a  function, and  then
from  within  the  ``setup.py``  file  *point*  to  that  function  within  the
"console_scripts"  section  of the  "entry_points"  argument  to the  ``setup``
function.

.. code-block:: python

    # do_science.py
    # script for doing cool science things

    import argparse

    parser = argparse.ArgumentParser(prog="do_science")
    parser.add_argument("input_file")  # positional argument
    parser.add_argument("-d", "--debug", action="store_true") # option

    def main(*argv: str) -> int:
        """Main entry point for `do_science`.

           Arguments:
           *argv: str
               Command line arguments (e.g., `sys.argv`).

           Returns:
           exit_status: int
               0 if success, non-zero otherwise.
        """

        opts = parser.parse_args(argv)
        # opt is a namespace
        # opt.input_file is name of file
        # opt.debug is True or False (default is False w/ "store_true")
        return 0

.. code-block:: python

    # setup.py

    # use "entry_points" to point to function and setuptools
    # will create executables on your behalf.
    setup(
    # ...
        # syntax: "{name}={package}.{module}:{function}"
        # "{name}" will be on your PATH in the same "/bin/"
        # alongside python/pip executables.
        entry_points = {"console_scripts": [
            "do_science=my_package.do_science:main"
        ]},
    # ...
    )

After the package is installed, ``pip install my_package ...``, you'll be able to
call the script:

.. code-block:: bash

    > do_science some/file.dat --debug


