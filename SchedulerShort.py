# -*- coding: utf-8 -*-

class SchedulerShort():
    def __init__(self, readyQueue):
        self.readyQueue = readyQueue

    def choosePCB(self):
        raise ExeptionNotImplemented("El método choosePCB no está implementado en SchedulerShort")

    def asignQuantum(self):
        raise ExeptionNotImplemented("El método asignQuantum no está implementado en SchedulerShort")

    def isEmptyQueue(self):
        return self.readyQueue.isEmpty()


class Priority(SchedulerShort):
    def __init__(self, rq):
        SchedulerShort.__init__(self, rq)

    def choosePCB(self):
        process = self.readyQueue.first()
        mostPriority = process.priority
        count = 1
        while(self.readyQueue.size() > count):
            if(mostPriority < self.readyQueue.get(count).priority):
                process = self.readyQueue.get(count)
                mostPriority = process.priority
                count = count + 1
        self.readyQueue.remove(process)
        return process

    def asignQuantum(self):
        return False

class Fifo(SchedulerShort):
    def __init__(self, rq):
        SchedulerShort.__init__(self, rq)

    def choosePCB(self):
        return self.readyQueue.first()

    def asignQuantum(self):
        return False

class RoundRobin(SchedulerShort):
    def __init__(self, rq, quantum):
        SchedulerShort.__init__(self, rq)
        self.quantum = quantum

    def choosePCB(self):
        return self.readyQueue.first()
    
    def asignQuantum(self):
        return True