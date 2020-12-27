from gate.and_gate import And
from gate.or_gate import Or
from gate.not_gate import Not
from gate.zero_gate import Zero
from gate.one_gate import One


def generate_control(opcode):
    Op5, Op4, Op3, Op2, Op1, Op0 = int_to_logic(opcode[0]), \
                                   int_to_logic(opcode[1]), int_to_logic(opcode[2]), int_to_logic(opcode[3]), \
                                   int_to_logic(opcode[4]), int_to_logic(opcode[5])

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

    return {"reg_dst": reg_dst, "alu_src": alu_src, "mem_to_reg": mem_to_reg,
            "reg_write": reg_write, "mem_read": mem_read, "mem_write": mem_write
        , "branch": branch, "alu_op1": alu_op1, "alu_op0": alu_op0}


def alu_control(f0, f1, f2, f3, aluop0, aluop1):
    op3 = And((Not(aluop0), aluop0))
    op2 = Or((aluop0, And((aluop1, f1))))
    op1 = Or((Not(f2), Not(aluop1)))
    op0 = And((aluop1, Or(f3, f0)))
    return {
        op0: op0, op1: op1, op2: op2, op3: op3
    }


def int_to_logic(a):
    if a == 0 or a == '0':
        return Zero()
    return One()
