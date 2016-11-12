# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import logging
import sys

from flask_injector import FlaskInjector
from google.cloud import datastore

from configuration import logging_configuration, meta_configuration
from privacy_application import PrivacyApplication
from server import Server

logger = logging.getLogger(__name__)


def create_log_handler():
    formatter = logging.Formatter(logging_configuration['pattern'])
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging_configuration['level'])
    return handler


def get_client():
    return datastore.Client(meta_configuration['projectId'])


log_handler = create_log_handler()
root_logger = logging.getLogger()
root_logger.setLevel(log_handler.level)
root_logger.addHandler(log_handler)

application = PrivacyApplication(get_client())
server = Server(application)
server.flask.logger.addHandler(log_handler)

FlaskInjector(app=server.flask, injector=application.injector)
