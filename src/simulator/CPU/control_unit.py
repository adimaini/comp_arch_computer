import sys
sys.path.append("..")
from utils import binaryUtils
from memory.memory import Memory, MemoryData


class ControlUnit:

    def __init__(self):
        self.opcode = '000000'
        self.r = '00'
        self.x = '00'
        self.i = '0'
        self.address = '00000'
        self.map = {
            "MAR": '0',
            "MBR": '0',
            "R0": '0',
            "R1": '0',
            "R2": '0',
            "R3": '0',
            "X1": '0',
            "X2": '0',
            "X3": '0',
        }

        self.switch = {
            0: "HLT",
            1: "LDR",
            2: "SDR",
            3: "LDX",
            42: "STX"
        }

    def decode(self, instruction):
        self.opcode = instruction[0:7]
        self.r = instruction[7:9]
        self.x = instruction[9:11]
        self.i = instruction[11:12]
        self.address = instruction[12:]

    def execute(self, memory: Memory):
        idx_cu = int(self.address, 2)
        mar = binaryUtils.to_binary_with_length(idx_cu, 12)
        mbr = memory.memory_data[idx_cu].value
        self.map['MAR'] = mar
        self.map['MBR'] = mbr
        print(self.map)

        # depend to instruction to change the ix or gpr
        self.switch[int(self.opcode, 2)](memory)

        return self.map

    def LDR(self, memory):
        value = memory.memory_data[int(self.address, 2)]
        if self.r == '00':
            self.map['R0'] = value
        elif self.r == '01':
            self.map['R1'] = value
        elif self.r == '10':
            self.map['R2'] = value
        else:
            self.map['R3'] = value

    # def STR(self, memory):
    #     address_new = binaryUtils.to_binary_with_length(int(self.address), 12)
    #     if self.x == '00':
    #         value = self.le_gpr0.text()
    #     elif self.x == '01':
    #         value = self.le_gpr1.text()
    #     elif self.x == '10':
    #         value = self.le_gpr2.text()
    #     else:
    #         value = self.le_gpr3.text()
    #
    #     # self.memory.set(address, value, True)
    #     # self.tb_memory_detail.setItem(self.row, 0, QtWidgets.QTableWidgetItem(address))
    #     # self.tb_memory_detail.setItem(self.row, 1, QtWidgets.QTableWidgetItem(value))
    #     # self.tb_memory_detail.setItem(self.row, 2, QtWidgets.QTableWidgetItem(str(int(value, 2))))
    #     # self.row += 1
    #
    # def LDA(self, memory):
    #     return
    #
    # def LDX(self, memory):
    #     address = int(instruction[11:], 2)
    #     value = self.memory.get(str(address), False)
    #     '''
    #     if instruction[10] == '1':
    #         value = self.idir_ad(instruction[8:10], value)
    #     '''
    #     r = bin(value).replace('0b', '')
    #     value = '0' * (16 - len(r)) + r
    #     if instruction[8:10] == '01':
    #         self.le_ix1.setText(value)
    #     elif instruction[8:10] == '10':
    #         self.le_ix2.setText(value)
    #     elif instruction[8:10] == '11':
    #         self.le_ix3.setText(value)
    #
    # def STX(self, memory):
    #     address = instruction[11:]
    #     address = '0' * (12 - len(address)) + address
    #
    #     if instruction[8:10] == '01':
    #         value = self.le_ix1.text()
    #     elif instruction[8:10] == '10':
    #         value = self.le_ix2.text()
    #     elif instruction[8:10] == '11':
    #         value = self.le_ix3.text()

    # self.memory.set(address, value, True)
    # self.tb_memory_detail.setItem(self.row, 0, QtWidgets.QTableWidgetItem(address))
    # self.tb_memory_detail.setItem(self.row, 1, QtWidgets.QTableWidgetItem(value))
    # self.tb_memory_detail.setItem(self.row, 2, QtWidgets.QTableWidgetItem(str(int(value, 2))))
    # self.row += 1
