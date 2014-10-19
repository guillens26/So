# -*- coding: utf-8 -*-

class PCB:
    def __init__(self, pid, dirBase, priority):
        self.pc = 0
        self.state = New()
        self.pid = pid
        self.dirBase = dirBase
        self.priority = priority

    def printState(self):
        self.state.printState()

class PCBState:

    def printState(self):
        raise ExeptionNotImplemented("El método printState no está implementado en PCBState")

class New(PCBState):

    def printState(self):
        print("State New")

class Ready(PCBState):

    def printState(self):
        print("State Ready")

class Running(PCBState):

    def printState(self):
        print("State Running")

class Waiting(PCBState):

    def printState(self):
        print("State Waiting")

class Terminated(PCBState):

    def printState(self):
        print("State Terminated")