# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from api.infrastructure.handlers import QueryHandler


class DummyQuery(object):
    def __init__(self):
        self.message = 'The first query'


class DummyQueryHandler(QueryHandler):
    @property
    def message_type(self):
        return DummyQuery

    def execute(self, query):
        return query.message + ': this is so cool'
