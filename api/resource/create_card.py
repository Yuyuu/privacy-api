# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from flask import request
from flask_restful import Resource
from injector import inject

from api.command.create_card_command import CreateCardCommand
from api.infrastructure.bus import CommandBus


class CreateCard(Resource):
    @inject(command_bus=CommandBus)
    def __init__(self, command_bus):
        self.command_bus = command_bus

    def post(self):
        command = self._command()
        result = self.command_bus.send_and_wait_response(command)
        if result.is_error():
            return {'errors': result.error.messages}, result.error.status_code
        return {'id': str(result.response)}, 201

    @staticmethod
    def _command():
        return CreateCardCommand(
            yellow=CreateCard._from_request(u'yellow'),
            pink=CreateCard._from_request(u'pink'),
            green=CreateCard._from_request(u'green'),
            red=CreateCard._from_request(u'red'),
            blue=CreateCard._from_request(u'blue'),
            black=CreateCard._from_request(u'black')
        )

    @staticmethod
    def _from_request(key):
        return request.json.get(key, u'')
