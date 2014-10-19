# -*- coding: utf-8 -*-

from Exceptions import *
import Queue

class ReadyQueueFifo():
    def __init__(self):
        self.queue = Queue.Queue()

    def isFull(self):
        return self.queue.full()
    
    def isEmpty(self):
        return (self.queue.qsize() == 0)

    def add(self,elem):
        if(not self.isFull()):
            self.queue.put(elem)
        else:
            raise ExceptionQueueFull("La cola esta llena")

    def remove(self,elem):
        self.queue.remove(elem)

    def size(self):
        return self.queue.qsize()

    def first(self):
        return self.queue.get_nowait()

class ReadyQueuePriority():
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return (self.size() == 0)

    def add(self,elem):
        self.queue.append(elem)

    def remove(self,elem):
        self.queue.remove(elem)

    def first(self):
        return self.queue[0]

    def get(self,nCell):
        return self.queue[nCell]