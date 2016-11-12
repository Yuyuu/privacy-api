# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from api.infrastructure.handlers import CommandHandler
from api.infrastructure.repository import RepositoryLocator
from api.model.card import Card, Question
from validators import CommandValidator, ValidateBeforeWith


class CreateCardCommand(object):
    def __init__(self, yellow, pink, green, red, blue, black):
        self.yellow = yellow
        self.pink = pink
        self.green = green
        self.red = red
        self.blue = blue
        self.black = black


class CreateCardCommandValidator(CommandValidator):
    def validate(self, command):
        violations = []
        if not command.yellow:
            violations.append('MISSING_YELLOW_QUESTION')
        if not command.pink:
            violations.append('MISSING_PINK_QUESTION')
        if not command.green:
            violations.append('MISSING_GREEN_QUESTION')
        if not command.red:
            violations.append('MISSING_RED_QUESTION')
        if not command.blue:
            violations.append('MISSING_BLUE_QUESTION')
        if not command.black:
            violations.append('MISSING_BLACK_QUESTION')
        return violations


class CreateCardCommandHandler(CommandHandler):
    @property
    def message_type(self):
        return CreateCardCommand

    @ValidateBeforeWith(CreateCardCommandValidator())
    def execute(self, command):
        card = Card(
            yellow=Question(command.yellow),
            pink=Question(command.pink),
            green=Question(command.green),
            red=Question(command.red),
            blue=Question(command.blue),
            black=Question(command.black),
        )
        RepositoryLocator.cards().add(card)
        return card.uuid
