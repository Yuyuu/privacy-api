# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import logging

logging_configuration = {
    'level': logging.DEBUG,
    'pattern': '[%(asctime)s] [%(name)s] %(levelname)s | %(message)s'
}

db_configuration = {
    'host': 'localhost',
    'port': 27017
}
