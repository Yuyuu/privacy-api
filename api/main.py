# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import logging
import sys

import pymongo
from flask_injector import FlaskInjector

from configuration import logging_configuration, db_configuration
from privacy_application import PrivacyApplication
from server import Server

logger = logging.getLogger(__name__)


def create_log_handler():
    formatter = logging.Formatter(logging_configuration['pattern'])
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging_configuration['level'])
    return handler


def get_database():
    host = db_configuration.get('host', 'localhost')
    port = db_configuration.get('port', 27017)
    try:
        return pymongo.MongoClient(host, port)['privacy']
    except (pymongo.errors.ConnectionFailure, pymongo.errors.AutoReconnect):
        logger.exception('mongo database could not be started on mongodb://{0}:{1}/'.format(host, port))
        sys.exit(0)


log_handler = create_log_handler()
root_logger = logging.getLogger()
root_logger.setLevel(log_handler.level)
root_logger.addHandler(log_handler)

application = PrivacyApplication(get_database())
server = Server(application)
server.flask.logger.addHandler(log_handler)

FlaskInjector(app=server.flask, injector=application.injector)
