import logging

from PyQt5.QtCore import QObject, pyqtSignal


class Communicate(QObject):

    set_gpr = pyqtSignal(str, str)

    set_ix = pyqtSignal(str, str)

    set_pc = pyqtSignal(str)

    set_mar = pyqtSignal(str)

    set_mbr = pyqtSignal(str)

    set_ir = pyqtSignal(str)

    set_mfr = pyqtSignal(str)

    set_cc = pyqtSignal(str)

    set_fr = pyqtSignal(str, str)

    set_memory = pyqtSignal(str, str)

    def emit_signal_gpr(self, no, value):
        self.set_gpr.emit(no, value)

    def emit_signal_ix(self, no, value):
        self.set_ix.emit(no, value)

    def emit_signal_pc(self, value):
        self.set_pc.emit(value)

    def emit_signal_mar(self, address):
        self.set_mar.emit(address)

    def emit_signal_mbr(self, value):
        self.set_mbr.emit(value)

    def emit_signal_ir(self, value):
        self.set_ir.emit(value)

    def emit_signal_mfr(self, value):
        self.set_mfr.emit(value)

    def emit_signal_cc(self, value):
        self.set_cc.emit(value)

    def emit_signal_fr(self, no, value):
        self.set_fr.emit(no, value)

    def emit_signal_memory(self, address, value):
        self.set_memory.emit(address, value)

