# -*- coding: utf-8 -*-

class ExceptionProgramNotExists(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return repr(self.valor)

class ExceptionQueueFull(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return repr(self.valor)

class ExeptionNotImplemented(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return repr(self.valor)