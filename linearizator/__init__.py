# -*- coding: utf-8 -*-

from . import linearizator

class Metadata:
    def __init__(self):
        self.__version__ = '0.1.01'
        self.__author__ = 'Rubén de Celis Hernández'

    def get_version(self):
        return self.__version__
    def get_author(self):
        return self.__author__