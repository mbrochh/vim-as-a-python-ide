"""Another file in our package."""
from urlparse import urljoin


def print_twitter_url():
    """We can lookup the urljoin method via ``<Leader>g``."""
    print urljoin('http://www.twitter.com', 'mbrochh')


def try_to_import_from_demo_py():
    """Code completion makes importing easy!"""
    print 'Try to import that method which starts with ``open_``.'


def set_breakpoint(arg1, arg2, data=None):
    """
    We can set breakpoints via ``<Leader>b``.

    Make sure you have ipython and ipdb installed::

        pip install ipython
        pip install ipdb

    Then run your program from a new terminal window like so:

        python demo.py

    Use ``?`` to show all available commands and ``? <command>`` to show help
    for a certain command.

    """
    foo = 'bar'
    result = arg1 + arg2
    import ipdb; ipdb.set_trace() # BREAKPOINT
    print 'Try to set a breakpoint before this statement.'
    print 'Then run ``python demo.py``.'
    import ipdb; ipdb.set_trace() # BREAKPOINT
    print 'Good bye!'

    # Nice commands to try in ipdb:
    # ?
    # help a
    # a
    # l
    # next
    # inspect data
    # bt
    # u
    # s
    # c
    # exit
