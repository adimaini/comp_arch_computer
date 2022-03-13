import logging

from simulator.utils import binaryUtils


class ControlUnit:

    def __init__(self, memory, bus, registers):
        self.memory = memory
        self.bus = bus
        self.registers = registers

        self.opcode = 0
        self.r = 0
        self.x = 0
        self.i = 0
        self.address = 0
        self.cc = 0
        self.rx = 0
        self.ry = 0
        self.count = 0
        self.LR = 0
        self.AL = 0
        self.dev_id = 0
        self.trapCode = 0
        self.immed = 0
        self.command_dict = {
            'LDR': 1, 'STR': 2, 'LDA': 3, 'LDX': 41, 'STX': 42,
            'JZ': 10, 'JNE': 11, 'JCC': 12, 'JMA': 13, 'JSR': 14, 'RFS': 15, 'SOB': 16, 'JGE': 17,
            'MLT': 20, 'DVD': 21, 'TRR': 22, 'AND': 23, 'ORR': 24, 'NOT': 25, 'SRC': 31, 'RRC': 32,
            'AMR': 4, 'SMR': 5, 'AIR': 6, 'SIR': 7, 'MLT': 20, 'DVD': 21, 'TRR': 22, 'AND': 23, 'ORR': 24, 'NOT': 25,
            'SRC': 31, 'RRC': 32,
            'IN': 61, 'OUT': 62, 'CHK': 63
        }

    # decode a word: LDR,0,0,1,ADDRESS,0
    # decode a word: 0000010000000001
    def decodeAWord(self, word: str):
        if word.find(',') != -1:
            command = word.split(',')
            self.opcode = str(self.command_dict[command[0]])
            self.execute_function(command)
        else:
            self.opcode = oct(int(word[0:6], 2))[2:]
            # self.opcode = int(word[0:6], 2)
            self.execute_function(word)

    # notify the function
    def execute_function(self, command):
        number_func_dict = {
            '1': self.LDR, '2': self.STR, '3': self.LDA, '41': self.LDX, '42': self.STX,
            '10': self.JZ, '11': self.JNE, '12': self.JCC, '14': self.JSR, '15': self.RFS, '16': self.SOB,
            '17': self.JGE,
            '4': self.AMR, '5': self.SMR, '6': self.AIR, '7': self.SIR, '20': self.MLT, '21': self.DVD, '22': self.TRR,
            '23': self.AND, '24': self.ORR, '25': self.NOT, '31': self.SRC, '32': self.RRC,
            '61': self.IN, '62': self.OUT, '63': self.CHK
        }

        method = number_func_dict.get(self.opcode)
        if method:
            method(command)  # execute the function
        else:
            logging.error(f"Machine can't execute this opcode{self.opcode} instruction.")
            return

    def get_a_ir_str(self, opcode, r, x, i, address):
        opcode_bin = binaryUtils.to_binary_with_length(int(opcode, 8), 6)
        r_bin = binaryUtils.to_binary_with_length(r, 2)
        x_bin = binaryUtils.to_binary_with_length(x, 2)
        i_bin = binaryUtils.to_binary_with_length(i, 1)
        address_bin = binaryUtils.to_binary_with_length(address, 5)

        return f'{opcode_bin}{r_bin}{x_bin}{i_bin}{address_bin}'

    def get_computed_address(self):
        self.address = self.address + int(self.registers["ix"][self.x], 2)
        if self.i == 1:
            self.address = self.memory.get(self.address, False)

    def set_mar_bar(self):
        pass

    # instruction function
    # LDR,0,0,address,0/1
    # 0000010000000000
    def LDR(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        # update ir
        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("LDR: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        # begin to execute
        # the address = address(from instruction) + c(ix)
        self.get_computed_address()

        address_12 = binaryUtils.to_binary_with_length(self.address, 12)
        self.bus.emit_signal_mar(address_12)

        value = self.memory.get(self.address, False)
        value = binaryUtils.to_binary_with_length(value, 16)
        logging.info("The value {%s} will be stored in GPR%i" % (value, self.r))
        self.bus.emit_signal_mbr(value)
        print(self.r)
        print(str(self.r))
        self.bus.emit_signal_gpr(str(self.r), value)

    def STR(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("STR: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        value = self.registers["gpr"][self.r]

        address_12 = binaryUtils.to_binary_with_length(self.address, 12)
        self.bus.emit_signal_mar(address_12)

        self.bus.emit_signal_mbr(value)
        logging.info("The value {%s} will be stored in Memory{%i}" % (value, self.address))
        self.memory.set(str(self.address), str(int(value, 2)), False)
        self.bus.emit_signal_memory(str(self.address), value)

    def LDA(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("LDA: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        address_12 = binaryUtils.to_binary_with_length(self.address, 12)
        address_16 = binaryUtils.to_binary_with_length(self.address, 16)
        logging.info("The address{%s} will be store in GPR{%i}" % (address_16, self.r))
        self.bus.emit_signal_gpr(str(self.r), address_16)
        self.bus.emit_signal_mar(address_12)
        self.bus.emit_signal_mbr(address_16)

    def LDX(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("LDX: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        # self.address = self.address + int(self.registers["ix"][self.x], 2)

        if self.i == 1:
            self.address = self.memory.get(self.address, False)

        value = self.memory.get(self.address, False)
        value = binaryUtils.to_binary_with_length(value, 16)
        address_12 = binaryUtils.to_binary_with_length(self.address, 12)

        self.bus.emit_signal_mar(address_12)
        self.bus.emit_signal_mbr(value)
        logging.info("The content of {%s} will be store in IX{%i}" % (value, self.x))
        self.bus.emit_signal_ix(str(self.x), value)

    def STX(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("STX: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        # self.address = self.address + int(self.registers["ix"][self.x], 2)
        if self.i == 1:
            self.address = self.memory.get(self.address, False)

        value = self.registers["ix"][self.x]
        address_12 = binaryUtils.to_binary_with_length(self.address, 12)
        self.bus.emit_signal_mar(address_12)
        self.bus.emit_signal_mbr(value)

        logging.info("The content of IX{%i} will be store in Memory{%s}" % (self.x, self.address))
        self.memory.set(str(self.address), str(int(value, 2)), False)
        self.bus.emit_signal_memory(str(self.address), value)

    # Transfer Instructions function
    def JZ(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        # set IR
        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("JZ: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        # set MAR
        address_12 = binaryUtils.to_binary_with_length(self.address, 12)
        self.bus.emit_signal_mar(address_12)
        # self.bus.emit_signal_mbr(address_12)

        gpr_value = self.registers["gpr"][self.r]
        if int(gpr_value, 2) == 0:
            logging.info("PC changes into EA(%i)" % self.address)
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(self.address, 12))
        else:
            pc_value = self.registers["pc"]
            pc_value = int(pc_value, 2) + 1;
            logging.info("PC plus 1")
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(pc_value, 12))

    def JNE(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("JNE: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        # MAR
        self.bus.emit_signal_mar(binaryUtils.to_binary_with_length(self.address, 12))

        gpr_value = self.registers["gpr"][self.r]
        if int(gpr_value, 2) != 0:
            logging.info("PC changes into EA(%i)" % self.address)
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(self.address, 12))
        else:
            pc_value = self.registers["pc"]
            pc_value = int(pc_value, 2) + 1;
            logging.info("PC plus 1")
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(pc_value, 12))

    def JCC(self, instruction):
        if type(instruction) == list:
            self.cc = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.cc = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.cc, self.x, self.i, self.address)
        logging.info("JCC: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        self.bus.emit_signal_cc(binaryUtils.to_binary_with_length(self.cc, 2))
        address_12 = binaryUtils.to_binary_with_length(self.address, 12)
        self.bus.emit_signal_mar(address_12)
        # self.bus.emit_signal_mbr(address_12)

        if int(self.cc, 2) == 1:
            logging.info("PC changes into EA(%i)" % self.address)
            self.bus.emit_signal_pc(address_12)
        else:
            pc_value = self.registers["pc"]
            pc_value = int(pc_value, 2) + 1;
            logging.info("PC plus 1")
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(pc_value, 12))

    def JMA(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("JMA: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        self.bus.emit_signal_mar(self.address, 12)
        logging.info("PC changes into EA(%i)" % self.address)
        self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(self.address, 12))

    def JSR(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("JSR: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        pc_value = int(self.registers["pc"], 2) + 1;

        logging.info("The pc+1 value{%s} will be stored in GPR3" % pc_value)
        self.bus.emit_signal_gpr('3', binaryUtils.to_binary_with_length(pc_value, 16))

        self.get_computed_address()
        pc_12 = binaryUtils.to_binary_with_length(self.address, 12)
        self.bus.emit_signal_mar(pc_12)
        logging.info("The PC will be EA{%s}" % pc_12)
        self.bus.emit_signal_pc(pc_12)

    def RFS(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.i = int(instruction[3])
            self.immed = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.ix = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.immed = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.immed)
        logging.info("RFS: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        logging.info("The immed{%i} will be stored in R0." % self.immed)
        self.bus.emit_signal_gpr('0', binaryUtils.to_binary_with_length(self.immed, 16))

        r3_value = self.registers["gpr"][3]
        value = binaryUtils.to_binary_with_length(int(r3_value, 2), 12)
        logging.info("The PC will be changed into C(R3){%s}." % value)
        self.bus.emit_signal_pc(value)

    def SOB(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("SOB: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        # r <- c(r)-1
        logging.info("The GPR%i will minus 1." % self.r)
        newR = int(self.registers['gpr'][self.r], 2) - 1
        #self.r = newR
        self.bus.emit_signal_gpr(str(self.r), binaryUtils.to_binary_with_length(newR, 16))

        #c_r = self.registers['gpr'][self.r]
        if newR > 0:
            # PC <- EA
            value = binaryUtils.to_binary_with_length(self.address, 12)
            logging.info("The PC will be changed into {%s}." % value)
            self.bus.emit_signal_pc(value)
        else:
            pc_value = self.registers['pc']
            pc_value = int(pc_value, 2) + 1
            logging.info("The PC will be +1.")
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(pc_value, 12))

    def JGE(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.address)
        logging.info("JGE: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        self.get_computed_address()

        gpr_value = self.registers["gpr"][self.r]
        if int(gpr_value, 2) >= 0:
            logging.info("PC changes into EA(%i)" % self.address)
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(self.address, 12))
        else:
            pc_value = self.registers["pc"]
            pc_value = int(pc_value, 2) + 1
            logging.info("PC plus 1")
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(pc_value, 12))

    # Arithmetic and Logical Instructions:
    def AMR(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)
        self.get_computed_address()
        value = self.memory.get(self.address, False)
        r_value = int(self.registers['gpr'][self.r], 2)
        value = r_value + value
        value = binaryUtils.to_binary_with_length(value, 16)
        self.bus.emit_signal_gpr(str(self.r), value)

    def SMR(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.address = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[8:10], 2)
            self.i = int(instruction[10:11], 2)
            self.address = int(instruction[11:], 2)
        self.get_computed_address()
        value = self.memory.get(self.address, False)
        r_value = int(self.registers['gpr'][self.r], 2)
        value = r_value - value
        value = binaryUtils.to_binary_with_length(value, 16)
        self.bus.emit_signal_gpr(str(self.r), value)

    def AIR(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.immed = int(instruction[2])
        else:
            self.r = int(instruction[6:8], 2)
            self.immed = int(instruction[11:], 2)

        r_value = int(self.registers['gpr'][self.r], 2)
        value = r_value + self.immed
        value = binaryUtils.to_binary_with_length(value, 16)
        self.bus.emit_signal_gpr(str(self.r), value)

    def SIR(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.immed = int(instruction[2])
        else:
            self.r = int(instruction[6:8], 2)
            self.immed = int(instruction[11:], 2)

        r_value = int(self.registers['gpr'][self.r], 2)
        value = r_value - self.immed
        value = binaryUtils.to_binary_with_length(value, 16)
        self.bus.emit_signal_gpr(str(self.r), value)

    def MLT(self, instruction):
        if type(instruction) == list:
            self.rx = int(instruction[1])
            self.ry = int(instruction[2])
        else:
            self.rx = int(instruction[6:8], 2)
            self.ry = int(instruction[8:10], 2)
        rx_bin = self.registers['gpr'][self.rx]
        ry_bin = self.registers['gpr'][self.ry]
        rx_value = int(rx_bin, 2)
        ry_value = int(ry_bin, 2)
        product = rx_value * ry_value
        if product > 2e32 - 1:
            print('overflow')
        if product > 2 ** 32 - 1:
            self.bus.emit_signal_cc('0001')
        else:
            product_bin = binaryUtils.to_binary_with_length(product, 32)
            high_bits = product_bin[:16]
            low_bits = product_bin[16:]
            self.bus.emit_signal_gpr(str(self.rx), high_bits)
            self.bus.emit_signal_gpr(str(self.rx + 1), low_bits)

    def DVD(self, instruction):
        if type(instruction) == list:
            self.rx = int(instruction[1])
            self.ry = int(instruction[2])
        else:
            self.rx = int(instruction[6:8], 2)
            self.ry = int(instruction[8:10], 2)
        rx_bin = self.registers['gpr'][self.rx]
        ry_bin = self.registers['gpr'][self.ry]
        rx_value = int(rx_bin, 2)
        ry_value = int(ry_bin, 2)
        if ry_value == 0:
            self.bus.emit_signal_cc('0100')
        else:
            quotient = rx_value // ry_value
            remainder = rx_value % ry_value
            quotient_bin = binaryUtils.to_binary_with_length(quotient, 16)
            remainder_bin = binaryUtils.to_binary_with_length(remainder, 16)
            self.bus.emit_signal_gpr(str(self.rx), quotient_bin)
            self.bus.emit_signal_gpr(str(self.rx + 1), remainder_bin)

    def TRR(self, instruction):
        if type(instruction) == list:
            self.rx = int(instruction[1])
            self.ry = int(instruction[2])
        else:
            self.rx = int(instruction[6:8], 2)
            self.ry = int(instruction[8:10], 2)
        rx_bin = self.registers['gpr'][self.rx]
        ry_bin = self.registers['gpr'][self.ry]
        rx_value = int(rx_bin, 2)
        ry_value = int(ry_bin, 2)
        if rx_value == ry_value:
            self.bus.emit_signal_cc('1000')
        else:
            self.bus.emit_signal_cc('0000')

    def AND(self, instruction):
        if type(instruction) == list:
            self.rx = int(instruction[1])
            self.ry = int(instruction[2])
        else:
            self.rx = int(instruction[6:8], 2)
            self.ry = int(instruction[8:10], 2)
        rx_bin = self.registers['gpr'][self.rx]
        ry_bin = self.registers['gpr'][self.ry]
        rx_value = int(rx_bin, 2)
        ry_value = int(ry_bin, 2)
        res = rx_value & ry_value
        res_bin = binaryUtils.to_binary_with_length(res, 16)
        self.bus.emit_signal_gpr(str(self.rx), res_bin)

    def ORR(self, instruction):
        if type(instruction) == list:
            self.rx = int(instruction[1])
            self.ry = int(instruction[2])
        else:
            self.rx = int(instruction[6:8], 2)
            self.ry = int(instruction[8:10], 2)
        rx_bin = self.registers['gpr'][self.rx]
        ry_bin = self.registers['gpr'][self.ry]
        rx_value = int(rx_bin, 2)
        ry_value = int(ry_bin, 2)
        res = rx_value | ry_value
        res_bin = binaryUtils.to_binary_with_length(res, 16)
        self.bus.emit_signal_gpr(str(self.rx), res_bin)

    def NOT(self, instruction):
        if type(instruction) == list:
            self.rx = int(instruction[1])
        else:
            self.rx = int(instruction[6:8], 2)
        rx_bin = self.registers['gpr'][self.rx]
        rx_value = int(rx_bin, 2)
        print(rx_value)
        res = ~rx_value
        print(res)
        res_bin = binaryUtils.to_binary_with_length(res, 16)
        print(res_bin)
        self.bus.emit_signal_gpr(str(self.rx), res_bin)

    # Arithmetic and Logical Instructions:

    def SRC(self, instruction):
        if type(instruction) == list:
            self.R = int(instruction[1])
            self.count = int(instruction[2])
            self.LR = int(instruction[3])
            self.AL = int(instruction[4])
        else:
            self.R = int(instruction[6:8], 2)
            self.count = int(instruction[12:], 2)
            self.LR = int(instruction[9], 2)
            self.AL = int(instruction[8], 2)

        r_bin = self.registers['gpr'][self.R]
        if self.AL == 1:
            if self.LR == 1:
                r_bin = r_bin[self.count:] + '0' * self.count
            else:
                r_bin = '0' * self.count + r_bin[:-self.count]
        else:
            s = r_bin[0]
            r_bin = r_bin[1:]
            if s == '1':
                a = '1'
            else:
                a = '0'
            if self.LR == 1:
                r_bin = r_bin[self.count:] + '0' * self.count
            else:
                if self.count != 0:
                    self.bus.emit_signal_cc('0010')
                r_bin = a * self.count + r_bin[:-self.count]
            r_bin = s + r_bin
        self.bus.emit_signal_gpr(str(self.R), r_bin)

    def RRC(self, instruction):
        if type(instruction) == list:
            self.R = int(instruction[1])
            self.count = int(instruction[2])
            self.LR = int(instruction[3])
            self.AL = int(instruction[4])
        else:
            self.R = int(instruction[6:8], 2)
            self.count = int(instruction[12:], 2)
            self.LR = int(instruction[9], 2)
            self.AL = int(instruction[8], 2)

        r_bin = self.registers['gpr'][self.R]
        if self.AL == 1:
            if self.LR == 1:
                r_bin = r_bin[self.count:] + r_bin[:self.count]
            else:
                r_bin = r_bin[-self.count:] + r_bin[:-self.count]
        else:
            s = r_bin[0]
            r_bin = r_bin[1:]
            if self.LR == 1:
                r_bin = r_bin[self.count:] + r_bin[:self.count]
            else:
                r_bin = r_bin[-self.count:] + r_bin[:-self.count]
            r_bin = s + r_bin
        self.bus.emit_signal_gpr(str(self.R), r_bin)

    # I/O Operations :
    def IN(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.dev_id = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[12:], 2)
            self.i = int(instruction[9], 2)
            self.dev_id = int(instruction[8], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.dev_id)
        logging.info("IN: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        if self.dev_id == 0:
            self.bus.emit_signal_keyboard(True)
            keyboard_value = self.registers['keyboard']
            # convert the keyboard_value into a 16-bit binary number
            if keyboard_value == '':
                logging.error("Error - You didn't input a value!")

            logging.info(keyboard_value)

        value = '1'
        self.bus.emit_signal_gpr(str(self.r), value)


    def OUT(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.dev_id = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[12:], 2)
            self.i = int(instruction[9], 2)
            self.dev_id = int(instruction[8], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.dev_id)
        logging.info("OUT: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        if self.dev_id == 1:
            value = self.registers['gpr'][self.r]
            self.bus.emit_signal_printer(value, True)

    def CHK(self, instruction):
        if type(instruction) == list:
            self.r = int(instruction[1])
            self.x = int(instruction[2])
            self.dev_id = int(instruction[3])
            self.i = int(instruction[4])
        else:
            self.r = int(instruction[6:8], 2)
            self.x = int(instruction[12:], 2)
            self.i = int(instruction[9], 2)
            self.dev_id = int(instruction[8], 2)

        ir_str = self.get_a_ir_str(self.opcode, self.r, self.x, self.i, self.dev_id)
        logging.info("OUT: The {%s} will be executed." % ir_str)
        self.bus.emit_signal_ir(ir_str)

        logging.info("Machine is OK, able to IN/OUT a value!")

    # Floating Point Instructions/Vector Operations:
