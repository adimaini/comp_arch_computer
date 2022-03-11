import logging

from utils import binaryUtils

class ControlUnit:

    def __init__(self, memory, bus, registers):
        self.memory = memory
        self.bus = bus
        self.registers = registers

        self.opcode = 0
        self.r = 0
        self.ix = 0
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
        self.command_dict = {
            'LDR': 1, 'STR': 2, 'LDA': 3, 'LDX': 41, 'STX': 42,
            'JZ': 10, 'JNE': 11, 'JCC': 12, 'JMA': 13, 'JSR': 14, 'RFS': 15, 'SOB': 16, 'JGE': 17,
        }

    # decode a word: LDR,0,0,1,ADDRESS
    def decodeAWord(self, word: str):
        if word.find(',') != -1:
            command = word.split(',')
            self.opcode = self.command_dict[command[0]]
            self.execute_function(command)
        else:
            self.opcode = int(word[0:6], 2)
            self.execute_function(word)

    # notify the function
    def execute_function(self, command):
        number_func_dict = {
            1: self.LDR, 2: self.STR, 3: self.LDA, 41: self.LDX, 42: self.STX,
            10: self.JZ, 11: self.JNE, 12: self.JCC, 13: self.JSR, 14: self.RFS, 15: self.SOB, 16: self.JGE
        }

        method = number_func_dict.get(self.opcode)
        if method:
            method(command) # execute the function
        else:
            logging.error("Machine can't execute this instruction. Still need to improvement!")
            return

    def get_a_ir_str(self, opcode, r, x, i, address):
        opcode_bin = binaryUtils.to_binary_with_length(opcode, 6)
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

        #self.address = self.address + int(self.registers["ix"][self.x], 2)

        if self.i == 1:
            self.address = self.memory.get(self.address, False)

        value = self.memory.get(self.address, False)
        value = binaryUtils.to_binary_with_length(value,16)
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

        #self.address = self.address + int(self.registers["ix"][self.x], 2)
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
        #self.bus.emit_signal_mbr(address_12)

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
        #self.bus.emit_signal_mbr(address_12)

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

    def JSR(self):
        pass

    def RFS(self):
        pass

    def SOB(self):
        pass

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
            pc_value = int(pc_value, 2) + 1;
            logging.info("PC plus 1")
            self.bus.emit_signal_pc(binaryUtils.to_binary_with_length(pc_value, 12))

    # Arithmetic and Logical Instructions:

    # I/O Operations :

    # Floating Point Instructions/Vector Operations: