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
        command = self.command()
        result = self.command_bus.send_and_wait_response(command)
        if result.is_error():
            return {'errors': result.error.messages}, result.error.status_code
        return {'id': str(result.response)}, 201

    @staticmethod
    def command():
        return CreateCardCommand(
            yellow=request.json['yellow'],
            pink=request.json['pink'],
            green=request.json['green'],
            red=request.json['red'],
            blue=request.json['blue'],
            black=request.json['black']
        )
