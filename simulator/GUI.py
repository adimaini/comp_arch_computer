import sys
import Project1
from PyQt5.QtWidgets import QApplication, QMainWindow

from instructions.bus_signal import Communicate
from instructions.control_unit import ControlUnit
from memory.memory import Memory


class Simulator:

    registers = {
        "gpr": {0: '0', 1: '0', 2: '0', 3: '0'},
        "ix": {0: '0', 1: '0', 2: '0', 3: '0'},
        "pc": '',
        "mar": '',
        'mbr': '',
        'ir': '',
        'mfr': '',
        'cc': '',
        "fr0": '',
        "fr1": ''
    }

    # memory
    memory = Memory()

    # bus
    bus = Communicate()

    def createApplication(self):
        # Control Unit
        cu = ControlUnit(Simulator.memory, Simulator.bus, Simulator.registers)

        # 创建QApplication类的实例
        app = QApplication(sys.argv)

        mainWindow = QMainWindow()
        ui = Project1.Ui_MainWindow(Simulator.memory,
                                    Simulator.bus,
                                    cu,
                                    Simulator.registers)

        ui.setupUi(mainWindow)

        mainWindow.show()
        # 进入程序的主循环，并通过exit函数确保主循环安全结束
        sys.exit(app.exec_())

if __name__ == '__main__':
   s = Simulator()
   s.createApplication()
