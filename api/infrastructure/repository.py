# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from abc import ABCMeta, abstractmethod

from api.model.factories import CardFactory


class RepositoryLocator(object):
    __metaclass__ = ABCMeta
    
    instance = None

    @staticmethod
    def initialize(repository_locator):
        RepositoryLocator.instance = repository_locator

    @staticmethod
    def cards():
        return RepositoryLocator.instance.get_cards()

    @abstractmethod
    def get_cards(self):
        pass


class MongoRepositoryLocator(RepositoryLocator):
    def __init__(self, db):
        self.db = db

    def get_cards(self):
        return CardRepository(self.db['card'])


class CardRepository(object):
    def __init__(self, collection):
        self.collection = collection

    def add(self, card):
        self.collection.insert(card.serialize())
