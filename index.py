from Components.control_unit import generate_control
from runner.circuit_runner import CircuitRunner
from gate.not_gate import Not
from gate.one_gate import One
from gate.and_gate import And
from gate.zero_gate import Zero

a=generate_control("000000")
for gate in a:
    print(gate)
    print(a[gate].logic())
