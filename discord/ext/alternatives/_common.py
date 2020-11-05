import sys

from typing import Optional, NoReturn

def py_allow(major: int, minor: int, micro: int) -> Optional[NoReturn]:
    if sys.version_info < (major, minor, micro):
        raise RuntimeError('the version of Python installed is not compatible with this experiment.')
