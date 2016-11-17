# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from api.infrastructure.handlers import QueryHandler
from api.infrastructure.repository import RepositoryLocator


class GetRandomCardQuery(object):
    def __init__(self):
        pass


class GetRandomCardQueryHandler(QueryHandler):
    @property
    def message_type(self):
        return GetRandomCardQuery

    def execute(self, query):
        card = RepositoryLocator.cards().get_random()
        return card.serialize()
