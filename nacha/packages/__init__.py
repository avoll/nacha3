from __future__ import absolute_import
import sys

if sys.version_info[0] < 3:
    from .bryl import *
else:
    from .bryl3 import *

