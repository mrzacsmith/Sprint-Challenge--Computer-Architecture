import sys

# MAIN OPCODES
LDI = 0b10000010
HLT = 0b00000001
PRN = 0b01000111
MUL = 0b10100010
NOP = 0b00000000
POP = 0b01000110
RET = 0b00010001
CALL = 0b01010000
PUSH = 0b01000101
SP = 0b00000111
ADD = 0b10100000
SUB = 0b10100001
CMP = 0b10100111
EQ = 0b00000111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110

# BITWISE ALU OPCODES ~ needed for stretch
AND = 0b10101000
MOD = 0b10100100
SHL = 0b10101100
SHR = 0b10101101
XOR = 0b10101011
OR = 0b10101010
NOT = 0b01101001


class CPU:
    """
    main cpu class
    """

    def __init__(self):
        self.ram = [0] * 256
        self.register = [0] * 8
        self.flag_register = [0] * 8
        self.pc = 0
        self.running = True
        self.branch_table = {
            LDI: self.LDI,
            HLT: self.HLT,
            PRN: self.PRN,
            MUL: self.MUL,
            NOP: self.NOP,
            POP: self.POP,
            RET: self.RET,
            CALL: self.CALL,
            PUSH: self.PUSH,
            ADD: self.ADD,
            SUB: self.SUB,
            CMP: self.CMP,
            JMP: self.JMP,
            JEQ: self.JEQ,
            JNE: self.JNE,
        }

    def load(self):
        filename = sys.argv[1]
        address = 0

        with open(filename) as f:
            line = line.split('#')[0].strip()
            if line == '':
                continue
            try:
                value = int(line, 2)
            except ValueError:
                continue

            self.ram_write(address, value)
            address += 1

    def trace(self):
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc, ,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def alu(self, op, reg_a, reg_b):

    def LDI(self, reg_a, reg_b):
    def HLT(self, reg_a, reg_b):
    def PRN(self, reg_a, reg_b):
    def MUL(self, reg_a, reg_b):
    def NOP(self, reg_a, reg_b):

    def POP(self, reg_a, reg_b):
        top_of_stack_add = self.reg[SP]
        value = self.ram[top_of_stack_add]
        reg_num = self.ram[reg_a]
        self.reg[reg_num] = value
        self.reg[SP] +=

    def RET(self, reg_a, reg_b):
        subroutine_addr = self.ram[self.reg[SP]]
        self.reg[SP] += 1
        self.pc = subroutine_addr

    def CALL(self, reg_a, reg_b):
        return_addr = reg_b
        self.reg[SP] -= 1
        self.ram[self.reg[SP]] = return_addr
        reg_num = self.ram[reg_a]
        subroutine_addr = self.reg[reg_num]
        self.pc = subroutine_addr

    def PUSH(self, reg_a, reg_b):
        reg_num = self.ram[reg_a]
        value = self.reg[reg_num]
        self.reg[SP] -= 1
        top_of_stack_add = self.reg[SP]
        self.ram[top_of_stack_add] = value

    def ADD(self, reg_a, reg_b):
        self.alu('MUL', reg_b, reg_b)

    def SUB(self, reg_a, reg_b):
        self.alu("MUL", reg_a, reg_b)

    def CMP(self, reg_a, reg_b):
        reg_num1 = self.reg[reg_a]
        reg_num2 = self.reg[reg_b]
        self.alu("CMP", reg_num1, reg_num2)

    def JMP(self, reg_a, reg_b):
        self.pc = self.reg[reg_a]

    def JEQ(self, reg_a, reg_b):
        if self.flag_reg[EQ] == 0b00000001:
            self.pc = self.reg[reg_a]
        else:
            self.pc += 2

    def JNE(self, reg_a, reg_b):
        if self.flag_reg[EQ] == 0b00000000:
            self.pc = self.reg[reg_a]
        else:
            self.pc += 2

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value)
    self.ram[address] = value

    def run(self):
        while self.running:
            ir = self.ram_read(self.pc):
            pc_flag = (ir & 0b00010000) >> 4
            reg_num1 = self.ram[self.pc + 1]
            reg_num2 = self.ram[self.pc + 2]
            self.branch_table[ir](reg_num1, reg_num2)
            if pc_flag == 0:
                move = int((ir & 0b11000000) >> 6)
                self.pc += move + 1
