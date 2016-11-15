# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import random
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


class QuestionEntity(ndb.Model):
    title = ndb.StringProperty(required=True, indexed=False)


class CardEntity(ndb.Model):
    yellow = ndb.StructuredProperty(QuestionEntity, required=True, indexed=False)
    pink = ndb.StructuredProperty(QuestionEntity, required=True, indexed=False)
    green = ndb.StructuredProperty(QuestionEntity, required=True, indexed=False)
    red = ndb.StructuredProperty(QuestionEntity, required=True, indexed=False)
    blue = ndb.StructuredProperty(QuestionEntity, required=True, indexed=False)
    black = ndb.StructuredProperty(QuestionEntity, required=True, indexed=False)
    randomizer = ndb.FloatProperty()


class CardRepository(object):
    def __init__(self):
        pass

    def add(self, card):
        entity = self._get_datastore_model(card)
        entity.put()

    @staticmethod
    def _get_datastore_model(card):
        return CardEntity(
            id=str(card.uuid), randomizer=random.random(),
            yellow=QuestionEntity(title=card.yellow.title), pink=QuestionEntity(title=card.pink.title),
            green=QuestionEntity(title=card.green.title), red=QuestionEntity(title=card.red.title),
            blue=QuestionEntity(title=card.blue.title), black=QuestionEntity(title=card.black.title)
        )
