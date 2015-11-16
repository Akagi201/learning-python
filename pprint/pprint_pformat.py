#!/usr/bin/env python

"""Formatting with pformat

"""

import logging
from pprint import pformat
from pprint_data import data

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)-8s %(message)s',
                    )

logging.debug('Logging pformatted data')
logging.debug(pformat(data))
