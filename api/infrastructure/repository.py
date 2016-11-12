# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from abc import ABCMeta, abstractmethod

from google.cloud import datastore


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


class DatastoreRepositoryLocator(RepositoryLocator):
    def __init__(self, client):
        self.client = client

    def get_cards(self):
        return CardRepository(self.client.key('Card'))


class CardRepository(object):
    def __init__(self, key):
        self.key = key

    def add(self, card):
        completed_key = self.key.completed_key(str(card.uuid))
        entity = datastore.Entity(key=completed_key)
        entity.update(card.serialize())
