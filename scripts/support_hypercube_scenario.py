#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2017 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/mystic/blob/master/LICENSE

from mystic.support import hypercube_scenario

__doc__ = hypercube_scenario.__doc__

if __name__ == '__main__':

    import sys

    hypercube_scenario(sys.argv[1:])


# EOF
