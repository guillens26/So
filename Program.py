# -*- coding: utf-8 -*-

class Program:
    def __init__(self, name, priority):
        self.name = name
        self.listInst = []
        self.priority = priority

    def addInstruction(self,inst):
        self.listInst.append(inst)

class Instruction:
    def __init__(self, number, isLast, isCpu):
        self.number = number
        self.last = isLast
        self.cpu = isCpu

    def isCpu(self):
        return self.cpu
