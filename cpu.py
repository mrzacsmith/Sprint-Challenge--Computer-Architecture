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
        self.program_counter = 0
        self.running = True
        self.branch_table = {
            NOP: self.NOP,
            HLT: self.HLT,
            PRN: self.PRN,
            LDI: self.LDI,
            MUL: self.MUL,
            ADD: self.ADD,
            SUB: self.SUB,
            PUSH: self.PUSH,
            POP: self.POP,
            CALL: self.CALL,
            RET: self.RET,
            CMP: self.CMP,
            JMP: self.JMP,
            JEQ: self.JEQ,
            JNE: self.JNE,
        }

    def load(self):

    def trace(self):

    def alu(self, op, reg_a, reg_b):

    def LDI(self, reg_a, reg_b):
    def HLT(self, reg_a, reg_b):
    def PRN(self, reg_a, reg_b):
    def MUL(self, reg_a, reg_b):
    def NOP(self, reg_a, reg_b):
    def POP(self, reg_a, reg_b):
    def RET(self, reg_a, reg_b):
    def CALL(self, reg_a, reg_b):
    def PUSH(self, reg_a, reg_b):
    def SP(self, reg_a, reg_b):
    def ADD(self, reg_a, reg_b):
    def SUB(self, reg_a, reg_b):
    def CMP(self, reg_a, reg_b):
    def EQ(self, reg_a, reg_b):
    def JMP(self, reg_a, reg_b):
    def JEQ(self, reg_a, reg_b):
    def JNE(self, reg_a, reg_b):

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value)
    self.ram[address] = value

    def run(self):
        while self.running:
