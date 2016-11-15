# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from abc import ABCMeta, abstractmethod

from google.appengine.ext import ndb


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
    def __init__(self):
        pass

    def get_cards(self):
        return CardRepository()


class QuestionEntityModel(ndb.Model):
    title = ndb.StringProperty(required=True, indexed=False)


class CardEntityModel(ndb.Model):
    yellow = ndb.StructuredProperty(QuestionEntityModel, required=True, indexed=False)
    pink = ndb.StructuredProperty(QuestionEntityModel, required=True, indexed=False)
    green = ndb.StructuredProperty(QuestionEntityModel, required=True, indexed=False)
    red = ndb.StructuredProperty(QuestionEntityModel, required=True, indexed=False)
    blue = ndb.StructuredProperty(QuestionEntityModel, required=True, indexed=False)
    black = ndb.StructuredProperty(QuestionEntityModel, required=True, indexed=False)


class CardRepository(object):
    def __init__(self):
        pass

    def add(self, card):
        entity = self._get_datastore_model(card)
        entity.put()

    @staticmethod
    def _get_datastore_model(card):
        return CardEntityModel(
            id=str(card.uuid),
            yellow=QuestionEntityModel(title=card.yellow.title), pink=QuestionEntityModel(title=card.pink.title),
            green=QuestionEntityModel(title=card.green.title), red=QuestionEntityModel(title=card.red.title),
            blue=QuestionEntityModel(title=card.blue.title), black=QuestionEntityModel(title=card.black.title)
        )
