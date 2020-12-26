from gate.and_gate import And
from gate.or_gate import Or
from gate.not_gate import Not


def generate_control(opcode):
    Op5, Op4, Op3, Op2, Op1, Op0 = int(opcode[0]), \
                                   int(opcode[1]), int(opcode[2]), int(opcode[3]), \
                                   int(opcode[4]), int(opcode[5])

    r_format = And((Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0)), "r_format")
    lw = And((Op5, Not(Op4), Not(Op3), Not(Op2), Op1, Op0))
    sw = And((Op5, Not(Op4), Op3, Not(Op2), Op1, Op0))
    beq = And((Not(Op5), Not(Op4), Not(Op3), Op2, Not(Op1), Not(Op0)))

    reg_dst = r_format
    alu_src = Or((lw, sw))
    mem_to_reg = lw
    reg_write = Or((r_format, lw))
    mem_read = lw
    mem_write = sw
    branch = beq
    alu_op1 = r_format
    alu_op0 = beq

    return {reg_dst, alu_src, mem_to_reg, reg_write, mem_read, mem_write, branch, alu_op1, alu_op0}

