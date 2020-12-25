from gate.zero_gate import Zero
from multiplexer.mux_mxn import Mux_mxn
import math


class ShiftRight:

    def __init__(self, x, y, length, name="ShiftLeft"):
        self.x = x
        self.y = y
        self.length = length
        self.name = name
        self.output = None

    def build(self):
        size = int(math.log(self.length, 2))
        self.output = []
        zero_gate = Zero()
        for i in range(self.length):
            inputs = []
            for j in range(self.length):
                if i - j >= 0:
                    inputs.append(self.x[i - j])
                else:
                    inputs.append(zero_gate)

            self.output.append(Mux_mxn(inputs, self.y, size))
        return self.output

    def get_output(self):
        return [self.output[i].get_output() for i in range(self.length)]
