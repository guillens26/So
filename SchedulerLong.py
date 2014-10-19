# -*- coding: utf-8 -*-

from PCB import *
from ReadyQueue import *

class SchedulerLong():
    def __init__(self, readyQueue, cpu, clock):
        self.cpu = cpu
        self.readyQueue = readyQueue
        self.clock = clock
        self.first = True

    def addPCB(self, pcb, kernel):
        if(self.first):
            self.cpu.setPCB(pcb)
            self.clock.register(self.cpu.fetchInstruction)
            self.clock.start()
            pcb.state = Running()
            self.first = False
        else:
            self.readyQueue.add(pcb)
            pcb.state = Ready()






'''
    def addPCB(self, pcb, kernel):
        if(self.readyQueue.isEmpty()):
            self.cpu.setPCB(pcb, 2)
            self.clock.register(self.cpu.fetchInstruction)
            self.clock.start()
            pcb.state = Running()
        else:
            self.readyQueue.add(pcb) 
            pcb.state = Ready()

'''
