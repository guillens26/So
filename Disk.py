# -*- coding: utf-8 -*-

from Exceptions import *

class Disk:
    def __init__(self):
        self.programs = []

    def write(self,prog):
        self.programs.append(prog)

    def read(self,progName):
        program = (self.existProgram(progName))
        if (program == None):
             raise ExceptionProgramNotExists("El programa no existe en disco")
        else:
            return program

    def existProgram(self,progName):
        program = None
        for i in self.programs:
            if(i.name == progName):
                program = i
        return program
