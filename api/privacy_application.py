# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from infrastructure.repository import RepositoryLocator, MongoRepositoryLocator
from injection_configuration import create_injector
from resource.create_card import CreateCard


class PrivacyApplication(object):
    def __init__(self, db):
        self.injector = create_injector()
        RepositoryLocator.initialize(MongoRepositoryLocator(db))

    @staticmethod
    def routes():
        return [
            Route('/cards', CreateCard)
        ]


class Route(object):
    def __init__(self, uri, resource):
        self.uri = uri
        self.resource = resource
