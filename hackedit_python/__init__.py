"""
This package contains a set of plugins that add basic python support to
HackEdit.
"""
import os
import sys

__version__ = '1.0a2.dev1'


EXTLIBS_PATH = os.path.join(os.path.dirname(__file__), 'extlibs')
sys.path.insert(0, EXTLIBS_PATH)


try:
    # make sure our icons are imported
    from .forms import hackedit_python_rc
except ImportError:
    # not generated yet
    hackedit_python_rc = None
