from __future__ import absolute_import

try:
    from . import search_FRB
    from .search_FRB import search_FRB
    from . import utils
    from FRB.io import file_wrapper
except:
    print("Warning: At least one utility could not be imported!")

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('FRB').version
except DistributionNotFound:
    __version__ = '0.0.0 - please install via pip/setup.py'
