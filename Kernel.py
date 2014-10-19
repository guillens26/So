# -*- coding: utf-8 -*-

from Memory import *
from SchedulerLong import *
from PCB import *

'''Para probar: '''
from Program import *
from Disk import *
from CPU import *
from SchedulerShort import *
from PcbTable import *

class Kernel():
    def __init__(self, disk, schedulerShort, schedulerLong, memoryManager, pcbTable):
        self.pcbTable = pcbTable
        self.memoryManager = memoryManager
        self.disk = disk
        self.schedulerShort = schedulerShort
        self.schedulerLong = SchedulerLong

    def calculatePID(self):
        return self.pcbTable.size() + 1

    def run(self, pName):
        program = self.disk.read(pName)
        dirBase = self.memoryManager.load(program)
        pid = self.calculatePID()
        priority = program.priority
        pcb = PCB(pid, dirBase, priority)
        self.pcbTable.addPCB(pcb)
        schedulerLong.addPCB(pcb, self)


#Prueba
#              number last cpu    
i1 = Instruction(1, False, True)
i2 = Instruction(2, False, True)
i3 = Instruction(3, False, False) # es de I/O
i4 = Instruction(4, False, True)
i5 = Instruction(5, False, True)
i6 = Instruction(6, True, True)
i7 = Instruction(7, True, True)
i8 = Instruction(8, True, True)

p1 = Program("p1",1)
p1.addInstruction(i1)
p1.addInstruction(i6)

p2 = Program("p2",5)
p2.addInstruction(i2)
p2.addInstruction(i3)
p2.addInstruction(i7)

p3 = Program("p3",8)
p3.addInstruction(i4)
p3.addInstruction(i5)
p3.addInstruction(i8)

disk = Disk()
disk.write(p1)
disk.write(p2)
disk.write(p3)

pcbTable = PcbTable()

memory = Continued(32)
memoryManager = MemoryManager(memory)

irqManager = IrqManager()
clock = Clock(2)

readyQueueFifo = ReadyQueueFifo()
readyQueuePriority = ReadyQueuePriority()

#schedulerShort = Fifo(readyQueueFifo)
schedulerShort = Priority(readyQueuePriority)
#schedulerShort = RoundRobin(readyQueueFifo, 3)  # se usa con todo fifo


cpu = CPU(memoryManager, irqManager, clock, pcbTable, schedulerShort)

#schedulerLong = SchedulerLong(readyQueueFifo, cpu, clock)
schedulerLong = SchedulerLong(readyQueuePriority, cpu, clock)

kernel = Kernel(disk, schedulerShort, schedulerLong, memoryManager, pcbTable)

kernel.run("p1")
kernel.run("p2")
kernel.run("p3")




