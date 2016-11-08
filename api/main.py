# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import sys
import logging
from flask_injector import FlaskInjector
from server import Server
from privacy_application import PrivacyApplication


def create_log_handler():
    from configuration import logging_configuration

    formatter = logging.Formatter(logging_configuration['pattern'])
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging_configuration['level'])
    return handler


log_handler = create_log_handler()
root_logger = logging.getLogger()
root_logger.setLevel(log_handler.level)
root_logger.addHandler(log_handler)

application = PrivacyApplication()
server = Server(application)
server.flask.logger.addHandler(log_handler)

FlaskInjector(app=server.flask, injector=application.injector)
