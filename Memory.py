# -*- coding: utf-8 -*-

class Memory:
    def __init__(self, tam):
        self.cells = []
        for i in range(tam):
            self.cells.append(None)
                
    def get(self,nCell):
        raise ExeptionNotImplemented("El método get no está implementado en Memory")
    
    def put(self,nCell,inst):  
        raise ExeptionNotImplemented("El método put no está implementado en Memory")

    def size(self):
        raise ExeptionNotImplemented("El método size no está implementado en Memory")

    def remove(self,nCell):
        raise ExeptionNotImplemented("El método remove no está implementado en Memory")

class Continued(Memory):
    def __init__(self,tam): 
        Memory.__init__(self,tam)

    def get(self,nCell):
        return self.cells[nCell]
    
    def put(self,nCell,inst):  
        self.cells[nCell] = inst

    def size(self):
        return len(self.cells)

    def remove(self,nCell):
        self.cells.remove(self.get(nCell))

class Paginated(Memory):
    def __init__(self):
        pass

    def get(self,nCell):
        pass
    
    def put(self,nCell,inst):  
        pass

    def size(self):
        pass

    def remove(self):
        pass

class MemoryManager:
    def __init__(self,memory):
        self.memory = memory
        self.nextDirWritable = 0        
        
    def load(self, program):
        dirBase = self.nextDirWritable
        for i in program.listInst:
            if(self.nextDirWritable >= (self.memory.size() - 1)):
                self.nextDirWritable = 0
            self.memory.put(self.nextDirWritable, i)
            self.nextDirWritable = self.nextDirWritable + 1
        return dirBase

    def remove(self,pcb):
        while(pcb.dirBase + pcb.pc != pcb.dirBase):
            self.memory.remove(pcb.dirBase + pcb.pc)
            pcb.pc = pcb.pc - 1

    def get(self,dirMem):
        return self.memory.get(dirMem)