"""Module for testing some python-mode features."""
# import os

from utils import set_breakpoint


def main(*args, **kwargs):
    """See? We got nice syntax highting."""
    print 'Hello world'
    set_breakpoint(42, 42, data={'key': 'value', })


def fold_this():
    """We can fold and unfold code blocks by pressing ``f``."""
    print 'Fold it.'


def fold_all():
    """We can fold and unfold everything by pressing ``F``."""
    print 'Fold all.'


def create_ropeproject():
    """We would create a ropeproject by executing ``:RopeOpenProject``."""
    print 'Now add your venv to ``.ropeproject/config.py``!'


def life_syntax_checking():
    """Pylint checks our code on each save."""
    # Try to uncomment this and save.
    # Try to uncomment the os import and save.
    # abc = 5  # Try to uncomment this line and save.

    # Now fix all reported issues!
    # You can move down into the Quickfix window witch ``<C-j>``
    # You can navigate up and down in that window with ``j`` and ``k``

    # When you press enter, you will get back into this window at the correct
    # line


def code_completion():
    """Code completion makes life easy."""
    life_syntax_checking
    # Try to call one of our methods here.
    # i.e.: Type ``li`` and then press ``<C-SPACE>``
    # You can navigate between then found choices by holding ``CTRL`` and using
    # ``j`` and ``k``

    # Try to import something from utils
    # i.e. Type ``from utils import`` and then press ``<C-SPACE>``


def open_utils_py():
    """We can use Ctlp to open files in our project."""
    print 'Open ``utils.py`` in a new vertical split via ``<C-p>ut<C-v>``'
    print 'Now open ``utils.py`` in a new tab via ``<C-p>ut<C-t>``.'


if __name__ == '__main__':
    main()
