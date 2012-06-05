"""Module for testing some python-mode features."""
import os

from utils import set_breakpoint
# from utils import does_not_exist


def main(*args, **kwargs):
    """See? We got nice syntax highting."""
    print 'Hello world'
    set_breakpoint(42, 42, data={'key': 'value', })

def fold_this():
    """We can fold code blocks by pressing ``f``."""
    print 'Fold it.'


def fold_all():
    """We can fold everything by pressing ``F``."""
    print 'Fold all.'


def create_ropeproject():
    """We would create a ropeproject by executing ``:RopeOpenProject``."""
    print 'Now add your venv to ``.ropeproject/config.py``!'


def life_syntax_checking():
    """Pylint checks our code on each save."""
    # Try to uncomment this and save.
    # Try to uncomment the os import and save.
    # Try to uncomment the does_not_exist imort and save.
    # abc = 5


def code_completion():
    """Code completion makes life easy."""
    # Try to call one of our methods here.
    # Try to import something from utils


def open_utils_py():
    """We can use Ctlp to open files in our project."""
    print 'Open ``utils.py`` in a new vertical split via ``<C-p>ut<C-v>``'
    print 'Now open ``utils.py`` in a new tab via ``<C-p>ut<C-t>``.'


if __name__ == '__main__':
    main()
