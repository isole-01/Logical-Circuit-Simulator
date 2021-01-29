
from adder.full_adder import FullAdder
from gate.or_gate import Or
from gate.and_gate import And
from gate.not_gate import Not
from gate.xor_gate import Xor
from multiplexer.mux4x2 import Mux4x2
from CPU.Components.ALU.shiftleft import ShiftLeft
from CPU.Components.ALU.shiftright import ShiftRight
from multiplexer.mux2x1 import Mux2x1


class Alu:

    def __init__(self, x, y, cin, selector, name="ArithmaticLogicalUnit"):
        self.x = x
        self.y = y
        self.cin = cin
        self.cout = None
        self.selector = selector
        self.name = name
        self.output = None
        self.build()


    def build(self):
        fulladder = FullAdder((self.x, self.y), self.cin, "Adder")
        andxy = And((self.x, self.y), "And")
        orxy = Or((self.x, self.y), "Or")
        xorxy = Xor((self.x, self.y), "Xor")
        notx = Not(self.x, "notx")
        noty = Not(self.y, "noty")
        select = Mux4x2((fulladder, andxy, orxy, xorxy), self.selector, "Decider")

        self.output = select
        self.cout = fulladder.cout

    def set_cin(self, val):
        self.cin = val
        self.build()

    def get_output(self):
        pass



class AluLogic:

    def __init__(self, x, y, cin, selector, shift, name="Alu"):
        self.x = x
        self.y = y
        self.cin = cin
        self.output = None
        self.aluoutput = None
        self.selector = selector
        self.shift = shift
        self.name = name
        # 32-bit alu
        self.bit = 32
        self.shiftleft = None
        self.shiftright = None
        self.shift_to = None
        self.build()

    def build(self):
        self.aluoutput = [Alu(self.x[i], Xor((self.y[i], self.cin), f"Xor cin and b{i}"), None, self.selector[2:4], f"alu{i}")
                          for i in range(self.bit)]
        self.aluoutput[self.bit - 1].set_cin(self.cin)
        for i in range(self.bit - 2 , -1 , -1) :
            self.aluoutput[i].set_cin(self.aluoutput[i+1].cout)
        self.shiftleft = ShiftLeft(self.x, self.shift, 32, "shift_left")
        self.shiftright = ShiftRight(self.x, self.shift, 32, "shift_right")
        self.shift_to = [Mux2x1((self.shiftright[i], self.shiftleft[i]), self.selector[1:2], "Shift_to_where")
                         for i in range(32)]
        self.output = [Mux2x1((self.aluoutput[i].output, self.shift_to[i].output), self.selector[0:1], "Operation")
                       for i in range(32)]



    def get_output(self):
        return [output.get_output() for output in self.output]










