import unittest
import Kernel from *
import ProgramInstruConsole from *

class KernelTestCase(unittest.TestCase):
    
    def runTest(self):
        self.kernel = Kernel()
        self.console = Console()
        self.i1 = Instruction(1)
        self.i2 = Instruction(2)
        self.program = Program("p1")
        self.program.inst.append(self.i1)
        self.program.inst.append(self.i2)
        self.kernel.run(self.program,self.console)
        self.assertEqual(self.program.inst[1],self.console.instructions[1])
        

    def instructionNumberTest(self):
        self.i1 = Instruction(1)
        self.assertEqual(self.i1.number,1)

    def addConsoleTest(self):
        self.kernel = Kernel()
        self.console = Console()
        self.i1 = Instruction(1)
        self.i2 = Instruction(2)
        self.program = Program("p1")
        self.program.inst.append(self.i1)
        self.program.inst.append(self.i2)
        self.kernel.run(self.program,self.console)
        self.assertEqual(self.program.inst,self.console.instructions)