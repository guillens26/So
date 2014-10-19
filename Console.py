# -*- coding: utf-8 -*-

class Console:
    def __init__(self):
        self.instructions = []

    def output(self):
        print ('Ejecutando:')
        for i in self.instructions:
            print("Instrucción NRO", i.number)
        print ("Fin de ejecución:")