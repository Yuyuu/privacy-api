# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from flask_restful import Resource
from injector import inject

from api.infrastructure.bus import QueryBus
from api.query.get_random_card_query import GetRandomCardQuery


class GetRandomCard(Resource):
    @inject(query_bus=QueryBus)
    def __init__(self, query_bus):
        self.query_bus = query_bus

    def get(self):
        result = self.query_bus.send_and_wait_response(GetRandomCardQuery())
        if result.is_error():
            return None, 500
        return result.response, 200
