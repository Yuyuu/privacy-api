# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from resource.index_resource import IndexResource
from injection_configuration import create_injector


class PrivacyApplication(object):
    def __init__(self):
        self.injector = create_injector()

    @staticmethod
    def routes():
        return [
            Route('/', IndexResource)
        ]


class Route(object):
    def __init__(self, uri, resource):
        self.uri = uri
        self.resource = resource
