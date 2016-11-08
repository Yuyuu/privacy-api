# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import uuid

import os
from flask import Flask
from flask_restful import Api


class Server(object):
    def __init__(self, application):
        flask = Flask(__name__)
        flask.config.from_object(ServerConfiguration)
        self._application = application
        self._web_server = Api(flask)
        self.add_routes(self._application.routes())

    def start(self, port):
        self.flask.run(port=port)

    def add_routes(self, routes):
        for route in routes:
            self._web_server.add_resource(route.resource, route.uri)

    def __call__(self, environ, start_response):
        return self.flask.wsgi_app(environ, start_response)

    @property
    def flask(self):
        return self._web_server.app


class ServerConfiguration(object):
    DEBUG = os.environ.get('env', 'dev') == 'dev'
    SECRET_KEY = uuid.uuid4()
