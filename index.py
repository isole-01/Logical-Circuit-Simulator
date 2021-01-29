from CPU.Components.control_unit import generate_control

a=generate_control("000000")
for gate in a:
    print(gate)
    print(a[gate].logic())
