# -*- coding: utf-8 -*-

from PCB import *

class Interruption:
    def __init__(self, pcb):
        self.pcb = pcb

    def execute(self):
        raise ExeptionNotImplemented("El método execute no está implementado en Interruption")
        

class Kill(Interruption):
    def __init__(self, pcb):
        Interruption.__init__(self, pcb)
        
    def execute(self):
        self.pcb.state = Terminated() 
        print("Kill PCB Number: " , self.pcb.pid)

class Timeout(Interruption):
    def __init__(self, pcb):
        Interruption.__init__(self, pcb)

    def execute(self):
        self.pcb.state = Ready()
        print("Tiemeout PCB Number: " , self.pcb.pid)

class IO(Interruption):
    def __init__(self, pcb):
        Interruption.__init__(self, pcb)

    def execute(self):
        self.pcb.state = Waiting()
        print("Waiting I/O PCB Number: " , self.pcb.pid)


class IrqManager():
    def __init__(self):
        self.interruption = None

    def setInterruption(self, interruption):
        self.interruption = interruption

    def launch(self):
        self.interruption.execute()