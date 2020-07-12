# Logical Circuit Simulator in Python

This library help to simulate Sequential Logical Circuit. 

## How to make your Circuit
#### Important Warning: 
you should first determine flipflop, multiplexer, latch,... inputs then set or reset it.
consider this example:
```python
from flipflop.d import D_FlipFlop
from signals.signal import Signal
from gate.not_gate import Not

###### CORRECT WAY ##########
clock = Signal(cycle=1)             # Clock for pulse
d1 = D_FlipFlop(clock, None, "d1")  # make our D flipflop
not1 = Not(d1, "not")               # make not Gate with d1 output
d1.set_input(not1)                  # set not for flipflop input
d1.set()

###### INCORRECT WAY ##########
clock = Signal(cycle=1)             # Clock for pulse
d1 = D_FlipFlop(clock, None, "d1")  # make our D flipflop
not1 = Not(d1, "not")               # make not Gate with d1 output
d1.set()
d1.set_input(not1)                  # set not for flipflop input
```

### Sample combinational Circuit
not(x1 and x2) or x3
```python
from gate.and_gate import And
from gate.or_gate import Or
from gate.not_gate import Not

x1, x2, x3 = 0, 1, 0
and1 = And((x1, x2), "x1 & x2")
not1 = Not(and1, "not")
or1 = Or((not1, x3), "or x3")

print(or1.logic())
```

shorter way
```python
from gate.and_gate import And
from gate.or_gate import Or
from gate.not_gate import Not

x1, x2, x3 = 0, 1, 0
circuit = Or((x3, Not(And((x1,x2)))))
print(circuit.logic())
```
### D Flipflop
Its a sample code of flipflop that its input connected to output by a not gate.
```python
from flipflop.d import D_FlipFlop
from signals.signal import Signal
from gate.not_gate import Not

clock = Signal(cycle=1)             # Clock for pulse
d1 = D_FlipFlop(clock, None, "d1")  # make our D flipflop
not1 = Not(d1, "not")               # make not Gate with d1 output
d1.set_input(not1)                  # set not for flipflop input
d1.set()

# now run the cricuit
for _ in range(20):
    clock.pulse()                   # PULSING 
    d1.logic()                      # run the Circuit in this cycle
    print(d1)                       # showing result
```

### Johnson Counter n-bit
```python
from flipflop.d import D_FlipFlop
from signals.signal import Signal
from gate.not_gate import Not

n = 50
clock = Signal(cycle=1)
bits = [D_FlipFlop(clock, None, f"d{i}") for i in range(n)]
for i in range(1, n):
    bits[i].set_input(bits[i - 1])
    bits[i].reset()

bits[0].set_input(Not(bits[-1], "not"))
bits[0].reset()

for _ in range(100):
    clock.pulse()
    bits[-1].logic()
    print("".join([str(b.q()) for b in bits]))
```