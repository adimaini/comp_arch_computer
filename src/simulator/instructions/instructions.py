from memory.memory import Memory
from Project1 import Ui_MainWindow

class instructions(Ui_MainWindow):
    def __init__(self):
        self.ins = {'LDR': 1, 'STR': 2, 'LDA': 3, 'LDX': 41, 'STX': 42}
        #self.memory = Memory()
        #self.ui = Ui_MainWindow()
        self

    def LDR(self, instruction, memory):
        address = int(instruction[11:],2)
        print(address)
        value = memory.get(str(address), False)
        print(value)
        if instruction[10] == '1':
            r = bin(value).replace('0b', '')
            ix = '0' * (16 - len(r)) + r
            if instruction[8:10] == '01':
                self.ui.le_ix1.setText(ix)
            elif instruction[8:10] == '02':
                self.ui.le_ix2.setText(ix)
            else:
                self.ui.le_ix3.setText(ix)
            value = memory.get(str(value), False)
            print(value)

        r = bin(value).replace('0b', '')
        value = '0' * (16 - len(r)) + r

        if instruction[6:8] == '00':
            self.ui.le_gpr0.setText(value)
        elif instruction[6:8] == '01':
            self.ui.le_gpr1.setText(value)
        elif instruction[6:8] == '10':
            self.ui.le_gpr2.setText(value)
        else:
            self.ui.le_gpr3.setText(value)


    def STR(self):

        return

    def LDA(self):

        return

    def LDX(self):

        return

    def STX(self):

        return



    def load(self):

        instruction = self.OP + self.R + self.IX + self.I + self.Address




if __name__ == '__main__':

    instruction = '0000011100011111'

    instructions = instructions()
    in_encoded,a = instructions.LDR(instruction)

    print(in_encoded,a)


