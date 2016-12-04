# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from flask_restful import Resource


class CheckAppStarted(Resource):
    def __init__(self):
        pass

    def get(self):
        return 'OK', 200
