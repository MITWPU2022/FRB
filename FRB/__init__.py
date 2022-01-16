from __future__ import absolute_import

try:
    from . import search_FRB
    from .search_FRB import search_FRB
    from . import utils
    # from . import fil2h5
    # from . import h52fil
    # from . import h5diag
    # from . import bl_scrunch
    # from . import calcload
    # from . import rawhdr
    # from . import stax
    # from . import stix
    # from . import match_fils
    from FRB.io import file_wrapper
except:
    print("Warning: At least one utility could not be imported!")

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('FRB').version
except DistributionNotFound:
    __version__ = '0.0.0 - please install via pip/setup.py'
