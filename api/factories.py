# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from api.model.card import Card, Question


class CardFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create_card(card_entity):
        card = Card(
            uuid=card_entity.key.id(), yellow=Question(card_entity.yellow.title), pink=Question(card_entity.pink.title),
            green=Question(card_entity.green.title), red=Question(card_entity.red.title),
            blue=Question(card_entity.blue.title), black=Question(card_entity.black.title)
        )
        return card
