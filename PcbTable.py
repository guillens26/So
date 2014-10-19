# -*- coding: utf-8 -*-

class PcbTable():
    def __init__(self):
        self.listPCB = []

    def addPCB(self, pcb):
        self.listPCB.append(pcb)

    def removePCB(self, pcb):
        self.listPCB.remove(pcb)

    def size(self):
        return len(self.listPCB)