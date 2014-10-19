# -*- coding: utf-8 -*-

from Interruption import *
import sys

#Para probar:
from Memory import *
from Clock import *
from PCB import *
from PcbTable import *

class CPU():
    def __init__(self, aMemoryManager, aIrqManager, aClock, pcbTable, schedulerShort):
        self.pcb = None
        self.io = False
        self.quantum = None
        self.memoryManager = aMemoryManager
        self.irqManager = aIrqManager
        self.pcbTable = pcbTable
        self.schedulerShort  = schedulerShort
        self.clock = aClock
        self.clock.register(self.fetchInstruction)

    def setQuantum(self):
        if (self.schedulerShort.asignQuantum()):
            self.quantum = self.schedulerShort.quantum
        else:
            self.quantum = 2

    def setPCB(self, aPcb):
        self.pcb = aPcb
        self.setQuantum()

    def asingPCB(self, pcb):
        self.setPCB(pcb)
        self.clock.register(self.fetchInstruction)

    def chooseAndAsingPCB(self):
        newPCB = self.schedulerShort.choosePCB() 
        self.asingPCB(newPCB)
    
    def isLastInstruction(self, instruction):
        return instruction.last     
    
    def launch(self, irq):
        self.irqManager.setInterruption(irq)
        self.irqManager.launch()

    def fetchInstruction(self):
        self.quantum = self.quantum -1
        instruction = self.memoryManager.get(self.pcb.dirBase + self.pcb.pc)
        if(instruction.isCpu()):
            print("Se ejecuto la instruccion: ", instruction.number)
            if(self.isLastInstruction(instruction)):
                self.launch(Kill(self.pcb))
                #self.memoryManager.remove(self.pcb) #con este hace un resize y las dirbase no coinciden ver cuando se implementen bien las memorias
                self.pcbTable.removePCB(self.pcb)
                if(self.schedulerShort.isEmptyQueue()):
                    print("Termino el proceso de ejecucion del ciclo")
                    sys.exit(0)
                else:
                    self.chooseAndAsingPCB()
            else:
                self.pcb.pc = self.pcb.pc + 1
                if(self.quantum == 0):
                    self.launch(Timeout(self.pcb))
                    self.schedulerShort.readyQueue.add(self.pcb)
                    self.chooseAndAsingPCB()
        else:
            self.launch(IO(self.pcb))
            self.pcb.pc = self.pcb.pc + 1
            self.schedulerShort.readyQueue.add(self.pcb)
            self.chooseAndAsingPCB()
    

'''
memory = Continued(32)
memoryManager = MemoryManager(memory)
irqManager = IrqManager()
clock = Clock()
pcb = PCB(1,100,10)

cpu = CPU(memoryManager, irqManager, clock)
cpu.setPCB(pcb,3)




'''

