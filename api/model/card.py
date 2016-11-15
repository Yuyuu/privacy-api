# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from uuid import uuid4


class Card(object):
    def __init__(self, yellow, pink, green, red, blue, black, uuid=None):
        self.uuid = uuid or uuid4()
        self.yellow = yellow
        self.pink = pink
        self.green = green
        self.red = red
        self.blue = blue
        self.black = black


class Question(object):
    def __init__(self, title):
        self.title = title

    def serialize(self):
        return {'title': self.title}
