# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLineEdit, QFrame, QPushButton, QInputDialog

from log.stream import QPlainTextEditLogger
from utils import binaryUtils
import os
import logging

class Ui_MainWindow(object):

    gloabl_under_process_status = "background:green"
    gloabl_finish_process_status = "background:red"

    def __init__(self, memory, bus, cu, registers):
        self.memory = memory
        self.bus = bus
        self.cu = cu
        self.registers = registers

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1474, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget.setObjectName("centralwidget")

        # IPL
        self.btn_IPL = QtWidgets.QPushButton(self.centralwidget)
        self.btn_IPL.setGeometry(QtCore.QRect(11, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_IPL.setFont(font)
        self.btn_IPL.setObjectName("btn_IPL")

        # Load
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(111, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_load.setFont(font)
        self.btn_load.setObjectName("btn_load")
        self.btn_load.clicked.connect(self.load)

        # Store
        self.btn_Store = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Store.setGeometry(QtCore.QRect(211, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_Store.setFont(font)
        self.btn_Store.setObjectName("btn_Store")

        # ST
        self.btn_ST = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ST.setGeometry(QtCore.QRect(311, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_ST.setFont(font)
        self.btn_ST.setObjectName("btn_ST")
        self.btn_ST.clicked.connect(self.store_plus)

        # SS
        self.btn_SS = QtWidgets.QPushButton(self.centralwidget)
        self.btn_SS.setGeometry(QtCore.QRect(411, 11, 99, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_SS.setFont(font)
        self.btn_SS.setObjectName("btn_SS")

        # Run
        self.btn_Run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Run.setGeometry(QtCore.QRect(517, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_Run.setFont(font)
        self.btn_Run.setObjectName("btn_Run")
        self.btn_Run.clicked.connect(self.run)

        self.lbl_run = QtWidgets.QLabel(self.centralwidget)
        self.lbl_run.setGeometry(QtCore.QRect(620, 25, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.lbl_run.setFont(font)
        self.lbl_run.setStyleSheet(Ui_MainWindow.gloabl_finish_process_status)
        self.lbl_run.setObjectName("lbl_run")

        # Halt
        self.lbl_halt = QtWidgets.QLabel(self.centralwidget)
        self.lbl_halt.setGeometry(QtCore.QRect(620, 4, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.lbl_halt.setFont(font)
        self.lbl_halt.setStyleSheet(Ui_MainWindow.gloabl_finish_process_status)
        self.lbl_halt.setObjectName("lbl_halt")

        self.btn_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Reset.setGeometry(QtCore.QRect(660, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_Reset.setFont(font)
        self.btn_Reset.setObjectName("btn_Reset")
        self.btn_Reset.clicked.connect(self.reset)

        # GPR0
        # <editor-fold desc="lbl_gpr0">
        self.lbl_gpr0 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr0.setGeometry(QtCore.QRect(12, 52, 45, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr0.setFont(font)
        self.lbl_gpr0.setObjectName("lbl_gpr0")
        # </editor-fold>
        self.le_gpr0 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_gpr0.setGeometry(QtCore.QRect(64, 54, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_gpr0.setFont(font)
        self.le_gpr0.setText("")
        self.le_gpr0.setMaxLength(16)
        self.le_gpr0.setAlignment(QtCore.Qt.AlignCenter)
        self.le_gpr0.setReadOnly(True)
        self.le_gpr0.setObjectName("le_gpr0")

        self.btn_load_gpr0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_gpr0.setGeometry(QtCore.QRect(225, 52, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_gpr0.setFont(font)
        self.btn_load_gpr0.setObjectName("btn_load_gpr0")
        self.btn_load_gpr0.clicked.connect(self.load_gpr0)

        # GPR1
        # <editor-fold desc="lbl_gpr1">
        self.lbl_gpr1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr1.setGeometry(QtCore.QRect(12, 90, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr1.setFont(font)
        self.lbl_gpr1.setObjectName("lbl_gpr1")
        # </editor-fold>
        self.le_gpr1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_gpr1.setGeometry(QtCore.QRect(63, 92, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_gpr1.setFont(font)
        self.le_gpr1.setText("")
        self.le_gpr1.setAlignment(QtCore.Qt.AlignCenter)
        self.le_gpr1.setReadOnly(True)
        self.le_gpr1.setObjectName("le_gpr1")
        self.btn_load_gpr1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_gpr1.setGeometry(QtCore.QRect(224, 90, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_gpr1.setFont(font)
        self.btn_load_gpr1.setObjectName("btn_load_gpr1")
        self.btn_load_gpr1.clicked.connect(self.load_gpr1)

        # GPR2
        # <editor-fold desc="lbl_gpr2">
        self.lbl_gpr2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr2.setGeometry(QtCore.QRect(12, 128, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr2.setFont(font)
        self.lbl_gpr2.setObjectName("lbl_gpr2")
        # </editor-fold>
        self.le_gpr2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_gpr2.setGeometry(QtCore.QRect(63, 130, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_gpr2.setFont(font)
        self.le_gpr2.setText("")
        self.le_gpr2.setAlignment(QtCore.Qt.AlignCenter)
        self.le_gpr2.setReadOnly(True)
        self.le_gpr2.setObjectName("le_gpr2")
        self.btn_load_gpr2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_gpr2.setGeometry(QtCore.QRect(224, 128, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_gpr2.setFont(font)
        self.btn_load_gpr2.setObjectName("btn_load_gpr2")
        self.btn_load_gpr2.clicked.connect(self.load_gpr2)

        # GPR3
        self.le_gpr3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_gpr3.setGeometry(QtCore.QRect(63, 168, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_gpr3.setFont(font)
        self.le_gpr3.setText("")
        self.le_gpr3.setAlignment(QtCore.Qt.AlignCenter)
        self.le_gpr3.setReadOnly(True)
        self.le_gpr3.setObjectName("le_gpr3")
        # <editor-fold desc="lbl_gpr3">
        self.lbl_gpr3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr3.setGeometry(QtCore.QRect(12, 166, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr3.setFont(font)
        self.lbl_gpr3.setObjectName("lbl_gpr3")
        # </editor-fold>
        self.btn_load_gpr3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_gpr3.setGeometry(QtCore.QRect(224, 166, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_gpr3.setFont(font)
        self.btn_load_gpr3.setObjectName("btn_load_gpr3")
        self.btn_load_gpr3.clicked.connect(self.load_gpr3)

        # IX1
        self.lbl_ix1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix1.setGeometry(QtCore.QRect(12, 214, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix1.setFont(font)
        self.lbl_ix1.setObjectName("lbl_ix1")
        self.le_ix1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ix1.setGeometry(QtCore.QRect(63, 216, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_ix1.setFont(font)
        self.le_ix1.setText("")
        self.le_ix1.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ix1.setReadOnly(True)
        self.le_ix1.setObjectName("le_ix1")
        self.btn_load_ix1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_ix1.setGeometry(QtCore.QRect(224, 214, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_ix1.setFont(font)
        self.btn_load_ix1.setObjectName("btn_load_ix1")
        self.btn_load_ix1.clicked.connect(self.load_ix1)

        # IX2
        self.lbl_ix2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix2.setGeometry(QtCore.QRect(12, 252, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix2.setFont(font)
        self.lbl_ix2.setObjectName("lbl_ix2")
        self.le_ix2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ix2.setGeometry(QtCore.QRect(63, 254, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_ix2.setFont(font)
        self.le_ix2.setText("")
        self.le_ix2.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ix2.setReadOnly(True)
        self.le_ix2.setObjectName("le_ix2")
        self.btn_load_ix2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_ix2.setGeometry(QtCore.QRect(224, 252, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_ix2.setFont(font)
        self.btn_load_ix2.setObjectName("btn_load_ix2")
        self.btn_load_ix2.clicked.connect(self.load_ix2)

        # IX3
        self.lbl_ix3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix3.setGeometry(QtCore.QRect(12, 290, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix3.setFont(font)
        self.lbl_ix3.setObjectName("lbl_ix3")
        self.le_ix3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ix3.setGeometry(QtCore.QRect(63, 292, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_ix3.setFont(font)
        self.le_ix3.setText("")
        self.le_ix3.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ix3.setReadOnly(True)
        self.le_ix3.setObjectName("le_ix3")
        self.btn_load_ix3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_ix3.setGeometry(QtCore.QRect(224, 290, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_ix3.setFont(font)
        self.btn_load_ix3.setObjectName("btn_load_ix3")
        self.btn_load_ix3.clicked.connect(self.load_ix3)

        # PC
        self.lbl_pc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pc.setGeometry(QtCore.QRect(397, 53, 33, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pc.setFont(font)
        self.lbl_pc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pc.setObjectName("lbl_pc")
        self.le_pc = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pc.setGeometry(QtCore.QRect(434, 54, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_pc.setFont(font)
        self.le_pc.setText("")
        self.le_pc.setMaxLength(16)
        self.le_pc.setAlignment(QtCore.Qt.AlignCenter)
        self.le_pc.setReadOnly(True)
        self.le_pc.setObjectName("le_pc")
        self.btn_load_pc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_pc.setGeometry(QtCore.QRect(572, 52, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_pc.setFont(font)
        self.btn_load_pc.setObjectName("btn_load_pc")
        self.btn_load_pc.clicked.connect(self.load_pc)

        # MAR
        self.lbl_mar = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mar.setGeometry(QtCore.QRect(397, 92, 33, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mar.setFont(font)
        self.lbl_mar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mar.setObjectName("lbl_mar")
        self.le_mar = QtWidgets.QLineEdit(self.centralwidget)
        self.le_mar.setGeometry(QtCore.QRect(434, 92, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_mar.setFont(font)
        self.le_mar.setText("")
        self.le_mar.setMaxLength(16)
        self.le_mar.setAlignment(QtCore.Qt.AlignCenter)
        self.le_mar.setReadOnly(True)
        self.le_mar.setObjectName("le_mar")
        self.btn_load_mar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_mar.setGeometry(QtCore.QRect(572, 90, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_mar.setFont(font)
        self.btn_load_mar.setObjectName("btn_load_mar")
        self.btn_load_mar.clicked.connect(self.load_mar)

        # MBR
        self.lbl_mbr = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mbr.setGeometry(QtCore.QRect(372, 132, 33, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mbr.setFont(font)
        self.lbl_mbr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mbr.setObjectName("lbl_mbr")
        self.le_mbr = QtWidgets.QLineEdit(self.centralwidget)
        self.le_mbr.setGeometry(QtCore.QRect(412, 134, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_mbr.setFont(font)
        self.le_mbr.setText("")
        self.le_mbr.setMaxLength(16)
        self.le_mbr.setAlignment(QtCore.Qt.AlignCenter)
        self.le_mbr.setReadOnly(True)
        self.le_mbr.setObjectName("le_mbr")
        self.btn_load_mbr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_mbr.setGeometry(QtCore.QRect(570, 131, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_mbr.setFont(font)
        self.btn_load_mbr.setObjectName("btn_load_mbr")
        self.btn_load_mbr.clicked.connect(self.load_mbr)

        # IR
        self.lbl_ir = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ir.setGeometry(QtCore.QRect(372, 170, 33, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ir.setFont(font)
        self.lbl_ir.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ir.setObjectName("lbl_ir")
        self.le_ir = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ir.setGeometry(QtCore.QRect(412, 170, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_ir.setFont(font)
        self.le_ir.setText("")
        self.le_ir.setMaxLength(16)
        self.le_ir.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ir.setReadOnly(True)
        self.le_ir.setObjectName("le_ir")

        # MFR
        self.lbl_mfr = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mfr.setGeometry(QtCore.QRect(460, 210, 33, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mfr.setFont(font)
        self.lbl_mfr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mfr.setObjectName("lbl_mfr")
        self.le_mfr = QtWidgets.QLineEdit(self.centralwidget)
        self.le_mfr.setGeometry(QtCore.QRect(504, 210, 61, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_mfr.setFont(font)
        self.le_mfr.setText("")
        self.le_mfr.setMaxLength(16)
        self.le_mfr.setAlignment(QtCore.Qt.AlignCenter)
        self.le_mfr.setReadOnly(True)
        self.le_mfr.setObjectName("le_mfr")

        # CC
        self.lbl_cc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cc.setGeometry(QtCore.QRect(460, 250, 33, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cc.setFont(font)
        self.lbl_cc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_cc.setObjectName("lbl_cc")
        self.le_cc = QtWidgets.QLineEdit(self.centralwidget)
        self.le_cc.setGeometry(QtCore.QRect(504, 250, 61, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_cc.setFont(font)
        self.le_cc.setText("")
        self.le_cc.setMaxLength(16)
        self.le_cc.setAlignment(QtCore.Qt.AlignCenter)
        self.le_cc.setReadOnly(True)
        self.le_cc.setObjectName("le_cc")

        # FR0
        self.lbl_fr0 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_fr0.setGeometry(QtCore.QRect(372, 284, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fr0.setFont(font)
        self.lbl_fr0.setObjectName("lbl_fr0")
        self.le_fr0 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_fr0.setGeometry(QtCore.QRect(412, 285, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_fr0.setFont(font)
        self.le_fr0.setText("")
        self.le_fr0.setAlignment(QtCore.Qt.AlignCenter)
        self.le_fr0.setReadOnly(True)
        self.le_fr0.setObjectName("le_fr0")

        # FR1
        self.le_fr1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_fr1.setGeometry(QtCore.QRect(412, 320, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_fr1.setFont(font)
        self.le_fr1.setText("")
        self.le_fr1.setAlignment(QtCore.Qt.AlignCenter)
        self.le_fr1.setReadOnly(True)
        self.le_fr1.setObjectName("le_fr1")
        self.lbl_fr1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_fr1.setGeometry(QtCore.QRect(372, 320, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fr1.setFont(font)
        self.lbl_fr1.setObjectName("lbl_fr1")

        # <editor-fold desc="Title of Memory Managemant">
        self.lbl_title_memory = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title_memory.setGeometry(QtCore.QRect(10, 430, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title_memory.setFont(font)
        self.lbl_title_memory.setObjectName("lbl_title_memory")
        # </editor-fold>

        # Table of Memory
        self.tb_memory_detail = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_memory_detail.setGeometry(QtCore.QRect(0, 480, 611, 581))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.tb_memory_detail.setFont(font)
        self.tb_memory_detail.setTabletTracking(True)
        self.tb_memory_detail.setAutoFillBackground(False)
        self.tb_memory_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tb_memory_detail.setLineWidth(1)
        self.tb_memory_detail.setMidLineWidth(0)
        self.tb_memory_detail.setAutoScrollMargin(16)
        self.tb_memory_detail.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_memory_detail.setDragEnabled(False)
        self.tb_memory_detail.setAlternatingRowColors(True)
        self.tb_memory_detail.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_memory_detail.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_memory_detail.setShowGrid(True)
        self.tb_memory_detail.setRowCount(2048)
        self.tb_memory_detail.setColumnCount(3)
        self.tb_memory_detail.setObjectName("tb_memory_detail")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_memory_detail.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_memory_detail.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_memory_detail.setHorizontalHeaderItem(2, item)

        self.tb_memory_detail.setColumnWidth(0, 162)
        self.tb_memory_detail.setColumnWidth(1, 190)
        self.tb_memory_detail.setColumnWidth(2, 190)

        # Operation
        self.le_operation = QtWidgets.QLineEdit(self.centralwidget)
        self.le_operation.setGeometry(QtCore.QRect(10, 360, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_operation.setFont(font)
        self.le_operation.setText("")
        self.le_operation.setAlignment(QtCore.Qt.AlignCenter)
        self.le_operation.setObjectName("le_operation")

        self.le_gpr_input = QtWidgets.QLineEdit(self.centralwidget)
        self.le_gpr_input.setGeometry(QtCore.QRect(160, 360, 61, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_gpr_input.setFont(font)
        self.le_gpr_input.setText("")
        self.le_gpr_input.setMaxLength(16)
        self.le_gpr_input.setAlignment(QtCore.Qt.AlignCenter)
        self.le_gpr_input.setObjectName("le_gpr_input")

        self.le_ixr_input = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ixr_input.setGeometry(QtCore.QRect(220, 360, 61, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_ixr_input.setFont(font)
        self.le_ixr_input.setText("")
        self.le_ixr_input.setMaxLength(16)
        self.le_ixr_input.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ixr_input.setObjectName("le_ixr_input")

        self.le_ir_input = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ir_input.setGeometry(QtCore.QRect(280, 360, 21, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_ir_input.setFont(font)
        self.le_ir_input.setText("")
        self.le_ir_input.setMaxLength(16)
        self.le_ir_input.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ir_input.setObjectName("le_ir_input")

        self.le_address_input = QtWidgets.QLineEdit(self.centralwidget)
        self.le_address_input.setGeometry(QtCore.QRect(300, 360, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_address_input.setFont(font)
        self.le_address_input.setText("")
        self.le_address_input.setAlignment(QtCore.Qt.AlignCenter)
        self.le_address_input.setObjectName("le_address_input")

        # bind the max length for those input value
        self.le_operation.setMaxLength(6)
        self.le_gpr_input.setMaxLength(2)
        self.le_ixr_input.setMaxLength(2)
        self.le_ir_input.setMaxLength(1)
        self.le_address_input.setMaxLength(5)

        # <editor-fold desc="Operation... label">
        self.lbl_ix3_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix3_2.setGeometry(QtCore.QRect(30, 390, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix3_2.setFont(font)
        self.lbl_ix3_2.setObjectName("lbl_ix3_2")
        self.lbl_ix3_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix3_3.setGeometry(QtCore.QRect(160, 390, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix3_3.setFont(font)
        self.lbl_ix3_3.setObjectName("lbl_ix3_3")
        self.lbl_ix3_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix3_4.setGeometry(QtCore.QRect(220, 390, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix3_4.setFont(font)
        self.lbl_ix3_4.setObjectName("lbl_ix3_4")
        self.lbl_ix3_5 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix3_5.setGeometry(QtCore.QRect(280, 390, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix3_5.setFont(font)
        self.lbl_ix3_5.setObjectName("lbl_ix3_5")
        self.lbl_ix3_6 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ix3_6.setGeometry(QtCore.QRect(340, 390, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ix3_6.setFont(font)
        self.lbl_ix3_6.setObjectName("lbl_ix3_6")
        # </editor-fold>

        self.le_inputWord = QLineEdit(self.centralwidget)
        self.le_inputWord.setObjectName(u"le_inputWord")
        self.le_inputWord.setGeometry(QRect(610, 50, 351, 31))

        self.btn_inputWord = QPushButton(self.centralwidget)
        self.btn_inputWord.setObjectName(u"btn_inputWord")
        self.btn_inputWord.setGeometry(QRect(970, 50, 140, 30))
        self.btn_inputWord.setFont(font)

        self.btn_test_log = QPushButton(self.centralwidget)
        self.btn_test_log.setObjectName(u"btn_test_log")
        self.btn_test_log.setGeometry(QRect(1120, 50, 140, 30))
        self.btn_test_log.setFont(font)

        self.log_area = QPlainTextEditLogger(self.centralwidget)
        self.log_area.setFormatter(logging.Formatter('%(asctime)s - %(name)-6s %(levelname)-4s: - %(message)s'))
        # You can control the logging level
        logging.getLogger().addHandler(self.log_area)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(610, 80, 861, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(610, 470, 861, 16))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        # <editor-fold desc="line">
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 1920, 10))
        self.line.setMinimumSize(QtCore.QSize(500, 10))
        self.line.setMaximumSize(QtCore.QSize(1920, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 420, 611, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 203, 321, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(600, 46, 20, 1311))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 340, 611, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        # </editor-fold>

        # <editor-fold desc="raise">
        self.lbl_ir.raise_()
        self.line_2.raise_()
        self.btn_load_ix2.raise_()
        self.lbl_mar.raise_()
        self.le_mar.raise_()
        self.btn_load_mar.raise_()
        self.btn_load_gpr2.raise_()
        self.btn_load_gpr1.raise_()
        self.btn_load_ix1.raise_()
        self.btn_load_ix3.raise_()
        self.tb_memory_detail.raise_()
        self.btn_IPL.raise_()
        self.btn_load.raise_()
        self.btn_Store.raise_()
        self.btn_ST.raise_()
        self.btn_SS.raise_()
        self.btn_Run.raise_()
        self.line.raise_()
        self.lbl_gpr1.raise_()
        self.lbl_gpr2.raise_()
        self.lbl_gpr3.raise_()
        self.lbl_ix1.raise_()
        self.lbl_ix2.raise_()
        self.lbl_ix3.raise_()
        self.le_gpr1.raise_()
        self.le_gpr2.raise_()
        self.le_gpr3.raise_()
        self.le_ix1.raise_()
        self.le_ix2.raise_()
        self.le_ix3.raise_()
        self.lbl_gpr0.raise_()
        self.le_gpr0.raise_()
        self.btn_load_gpr0.raise_()
        self.lbl_pc.raise_()
        self.le_pc.raise_()
        self.btn_load_pc.raise_()
        self.lbl_mbr.raise_()
        self.le_mbr.raise_()
        self.lbl_mfr.raise_()
        self.le_ir.raise_()
        self.le_mfr.raise_()
        self.btn_load_mbr.raise_()
        self.line_4.raise_()
        self.lbl_title_memory.raise_()
        self.lbl_cc.raise_()
        self.le_cc.raise_()
        self.line_3.raise_()
        self.lbl_fr0.raise_()
        self.le_fr0.raise_()
        self.le_fr1.raise_()
        self.lbl_fr1.raise_()
        self.btn_load_gpr3.raise_()
        self.le_operation.raise_()
        self.le_gpr_input.raise_()
        self.le_ixr_input.raise_()
        self.le_ir_input.raise_()
        self.le_address_input.raise_()
        self.lbl_ix3_2.raise_()
        self.lbl_ix3_3.raise_()
        self.lbl_ix3_4.raise_()
        self.lbl_ix3_5.raise_()
        self.lbl_ix3_6.raise_()
        self.line_5.raise_()
        self.lbl_halt.raise_()
        self.lbl_run.raise_()
        self.btn_Reset.raise_()

        self.le_inputWord.raise_()
        self.btn_inputWord.raise_()
        self.btn_test_log.raise_()
        self.line_6.raise_()
        # self.log_area.raise_()
        self.line_7.raise_()
        # </editor-fold>

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # bind a function for button click
        self.btn_IPL.clicked.connect(self.choose_file)
        self.btn_Store.clicked.connect(self.store)
        self.btn_SS.clicked.connect(self.single_step)
        self.btn_inputWord.clicked.connect(self.input_a_word)
        self.btn_test_log.clicked.connect(self.log_test)

        # bind signal function
        self.bus.set_gpr.connect(self.gpr_slot)
        self.bus.set_ix.connect(self.ix_slot)
        self.bus.set_pc.connect(self.pc_slot)
        self.bus.set_mar.connect(self.mar_slot)
        self.bus.set_mbr.connect(self.mbr_slot)
        self.bus.set_ir.connect(self.ir_slot)
        self.bus.set_mfr.connect(self.mfr_slot)
        self.bus.set_cc.connect(self.cc_slot)
        self.bus.set_fr.connect(self.fr_slot)
        self.bus.set_memory.connect(self.memory_slot)
        self.bus.set_console_keyboard.connect(self.keyboard_slot)
        self.bus.set_console_printer.connect(self.printer_slot)

        # self.instructions = instructions()
        self.pc = self.le_pc.text()
        self.address = 8
        self.step = 0
        self.bin_instruction = ''
        self.row = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSCI-6461-Simulator"))
        self.btn_IPL.setText(_translate("MainWindow", "IPL"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.btn_Store.setText(_translate("MainWindow", "Store"))
        self.btn_ST.setText(_translate("MainWindow", "St++"))
        self.btn_SS.setText(_translate("MainWindow", "SingleStep"))
        self.btn_Run.setText(_translate("MainWindow", "Run"))
        self.lbl_gpr0.setText(_translate("MainWindow", "GPR0"))
        self.btn_load_gpr0.setText(_translate("MainWindow", "LD"))
        self.lbl_pc.setText(_translate("MainWindow", " PC"))
        self.btn_load_pc.setText(_translate("MainWindow", "LD"))
        self.lbl_mbr.setText(_translate("MainWindow", "MBR"))
        self.lbl_mfr.setText(_translate("MainWindow", "MFR"))
        self.btn_load_mbr.setText(_translate("MainWindow", "LD"))
        self.lbl_title_memory.setText(_translate("MainWindow", "Memory Mangement"))
        self.tb_memory_detail.setSortingEnabled(False)
        item = self.tb_memory_detail.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tb_memory_detail.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Binary"))
        item = self.tb_memory_detail.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Decemal"))
        self.lbl_cc.setText(_translate("MainWindow", " CC"))
        self.lbl_fr0.setText(_translate("MainWindow", "FR0"))
        self.lbl_fr1.setText(_translate("MainWindow", "FR1"))
        self.btn_load_gpr3.setText(_translate("MainWindow", "LD"))
        self.lbl_ir.setText(_translate("MainWindow", " IR"))
        self.lbl_ix2.setText(_translate("MainWindow", "IXR2"))
        self.btn_load_ix2.setText(_translate("MainWindow", "LD"))
        self.lbl_mar.setText(_translate("MainWindow", "MAR"))
        self.btn_load_mar.setText(_translate("MainWindow", "LD"))
        self.lbl_gpr3.setText(_translate("MainWindow", "GPR3"))
        self.lbl_gpr2.setText(_translate("MainWindow", "GPR2"))
        self.btn_load_gpr2.setText(_translate("MainWindow", "LD"))
        self.lbl_gpr1.setText(_translate("MainWindow", "GPR1"))
        self.btn_load_gpr1.setText(_translate("MainWindow", "LD"))
        self.lbl_ix1.setText(_translate("MainWindow", "IXR1"))
        self.btn_load_ix1.setText(_translate("MainWindow", "LD"))
        self.lbl_ix3.setText(_translate("MainWindow", "IXR3"))
        self.btn_load_ix3.setText(_translate("MainWindow", "LD"))
        self.lbl_ix3_2.setText(_translate("MainWindow", "Operation"))
        self.lbl_ix3_3.setText(_translate("MainWindow", "GPR"))
        self.lbl_ix3_4.setText(_translate("MainWindow", "IXR"))
        self.lbl_ix3_5.setText(_translate("MainWindow", "I"))
        self.lbl_ix3_6.setText(_translate("MainWindow", "Address"))
        self.lbl_halt.setText(_translate("MainWindow", "HALT"))
        self.lbl_run.setText(_translate("MainWindow", "RUN"))
        self.btn_Reset.setText(_translate("MainWindow", "Reset"))
        self.btn_inputWord.setText(_translate("MainWindow", "TestCommand"))
        self.btn_test_log.setText(_translate("MainWindow", "Test Log"))

    def log_test(self):
        logging.info("info")
        logging.debug("debug")
        logging.error("error")
        logging.warning("warning")
        text, ok = input.getText(self.centralwidget, "Console KeyBoard", "Input Value")

    def input_a_word(self):
        word = self.le_inputWord.text()
        if (len(word.strip()) == 0):
            logging.error("Please input a instruction from inputArea")
            return

        logging.info("Get a word {%s} from inputArea" % word)
        self.cu.decodeAWord(word)

    def gpr_slot(self, no, value):
        if no == "0":
            self.registers["gpr"][0] = value
            self.le_gpr0.setText(value)
        elif no == "1":
            self.registers["gpr"][1] = value
            self.le_gpr1.setText(value)
        elif no == "2":
            self.registers["gpr"][2] = value
            self.le_gpr2.setText(value)
        else:
            self.registers["gpr"][3] = value
            self.le_gpr3.setText(value)

    def ix_slot(self, no, value):
        if no == "1":
            self.registers["ix"][1] = value
            self.le_ix1.setText(value)
        elif no == "2":
            self.registers["ix"][2] = value
            self.le_ix2.setText(value)
        else:
            self.registers["ix"][3] = value
            self.le_ix3.setText(value)

    def pc_slot(self, value):
        self.registers["pc"] = value
        self.le_pc.setText(value)

    def mar_slot(self, value):
        self.registers["mar"] = value
        self.le_mar.setText(value)

    def mbr_slot(self, value):
        self.registers["mbr"] = value
        self.le_mbr.setText(value)

    def ir_slot(self, value):
        self.registers["ir"] = value
        self.le_ir.setText(value)

    def mfr_slot(self, value):
        self.registers["mfr"] = value
        self.le_mfr.setText(value)

    def cc_slot(self, value):
        self.registers["cc"] = value
        self.le_cc.setText(value)

    def fr_slot(self, no, value):
        if no == '0':
            self.registers["fr0"] = value
            self.le_fr0.setText(value)
        else:
            self.registers["fr1"] = value
            self.le_fr1.setText(value)

    def memory_slot(self, address, value):
        row = int(address)
        self.tb_memory_detail.item(row, 0).setText(binaryUtils.to_binary_with_length(row, 12))
        self.tb_memory_detail.item(row, 1).setText(value)
        self.tb_memory_detail.item(row, 2).setText(str(int(value, 2)))

    def keyboard_slot(self, value: bool):
        if bool:
            # begin to input the value
            text, ok = QInputDialog.getText(self.centralwidget, "KeyBoard", "Input Value:")
            if text and ok:
                self.registers['keyboard'] = text

    def printer_slot(self, value: str, flag: bool):
        if flag:
            print('out',value,int(value,2))
            logging.info("Output A Value:{%s}" % value)

    def choose_file(self, Filepath):
        list = self.memory.memory_data
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Choose File", "./",
                                                          "All Files (*);;Text Files (*.txt)")

        if file_name[0] == '':
            return

        if os.path.splitext(file_name[0])[-1] != '.txt':
            self.messageDialog("Open File Error", "Please choose the .txt file!")
            return

        # begin to load the file, all the data will be store in global_memory_tbale_data
        f = open(file_name[0])
        line = f.readline()
        while line:
            if line[0] == '#' or line == '\n':
                line = f.readline()
                continue

            if line.find('#') != -1:
                end_index = line.find('#')
                line = line[0:end_index]

            line = line.strip('\n')
            line = line.strip(' ')
            strs = line.split(" ")
            address_bin_str = binaryUtils.hex_to_bin(strs[0])
            value_bin_str = binaryUtils.hex_to_bin(strs[1])

            idx = int(address_bin_str, 2)
            list[idx].value = int(value_bin_str, 2)

            line = f.readline()
        f.close()

        # write into table
        for i in range(0, len(list)):
            if list[i].value == None:
                list[i].value = 0
            self.add_a_row_in_tb_by_row(
                data=[binaryUtils.to_binary_with_length(i, 12), binaryUtils.to_binary_with_length(list[i].value, 16),
                      int(list[i].value)], row_No=i)
        self.tb_memory_detail.viewport().update()

    def reset(self):
        self.lbl_halt.setStyleSheet(Ui_MainWindow.gloabl_finish_process_status)
        self.lbl_run.setStyleSheet(Ui_MainWindow.gloabl_finish_process_status)
        #str = '0'
        self.registers["gpr"][0] = '0' * 16
        self.registers["gpr"][1] = '0' * 16
        self.registers["gpr"][2] = '0' * 16
        self.registers["gpr"][3] = '0' * 16
        self.registers["ix"][1] = '0' * 16
        self.registers["ix"][2] = '0' * 16
        self.registers["ix"][3] = '0' * 16
        self.registers["pc"] = '0' * 12
        self.registers["mar"] = '0' * 12
        self.registers["mbr"] = '0' * 16
        self.registers["ir"] = '0' * 16
        self.registers["MFR"] = '0' * 4
        self.registers["cc"] = '0' * 4
        self.registers["fr0"] = '0' * 16
        self.registers["fr1"] = '0' * 16

        self.le_gpr0.setText('0' * 16)
        self.le_gpr1.setText('0' * 16)
        self.le_gpr2.setText('0' * 16)
        self.le_gpr3.setText('0' * 16)
        self.le_ix1.setText('0' * 16)
        self.le_ix2.setText('0' * 16)
        self.le_ix3.setText('0' * 16)
        self.le_pc.setText('0' * 12)
        self.le_mar.setText('0' * 12)
        self.le_mbr.setText('0' * 16)
        self.le_ir.setText('0' * 16)
        self.le_fr0.setText('0' * 16)
        self.le_fr1.setText('0' * 16)
        self.le_cc.setText('0' * 4)
        self.le_mfr.setText('0' * 4)
        self.le_operation.setText(('0' * 6))
        self.le_gpr_input.setText(('0' * 2))
        self.le_ixr_input.setText(('0' * 2))
        self.le_ir_input.setText(('0' * 1))
        self.le_address_input.setText(('0' * 5))

    def get_input(self):
        OP = self.le_operation.text()
        R = self.le_gpr_input.text()
        IX = self.le_ixr_input.text()
        I = self.le_ir_input.text()
        Address = self.le_address_input.text()
        return OP + R + IX + I + Address

    def load_pc(self):
        code = self.get_input()
        self.registers["pc"] = code[4:]
        self.le_pc.setText(code[4:])

    def load_mar(self):
        code = self.get_input()
        self.registers["mar"] = code[4:]
        self.le_mar.setText(code[4:])

    def load_mbr(self):
        code = self.get_input()
        self.registers["mbr"] = code[4:]
        self.le_mbr.setText(code)

    def load_gpr0(self):
        code = self.get_input()
        self.registers["gpr"][0] = code
        self.le_gpr0.setText(code)

    def load_gpr1(self):
        code = self.get_input()
        self.registers["gpr"][1] = code
        self.le_gpr1.setText(code)

    def load_gpr2(self):
        code = self.get_input()
        self.registers["gpr"][2] = code
        self.le_gpr2.setText(code)

    def load_gpr3(self):
        code = self.get_input()
        self.registers["gpr"][3] = code
        self.le_gpr3.setText(code)

    def load_ix1(self):
        code = self.get_input()
        self.registers["ix"][1] = code
        self.le_ix1.setText(code)

    def load_ix2(self):
        code = self.get_input()
        self.registers["ix"][2] = code
        self.le_ix2.setText(code)

    def load_ix3(self):
        code = self.get_input()
        self.registers["ix"][3] = code
        self.le_ix3.setText(code)

    # store function
    def store(self):
        address = self.le_mar.text()
        value = self.le_mbr.text()
        row_No = int(address, 2)
        self.memory.set(address, value, True)
        self.tb_memory_detail.setItem(row_No, 0, QtWidgets.QTableWidgetItem(address))
        self.tb_memory_detail.setItem(row_No, 1, QtWidgets.QTableWidgetItem(value))
        self.tb_memory_detail.setItem(row_No, 2, QtWidgets.QTableWidgetItem(str(int(value, 2))))
        self.row += 1

    # store++ function
    def store_plus(self):
        address = self.le_mar.text()
        value = self.le_mbr.text()
        row_No = int(address, 2)
        self.memory.set(address, value, True)
        self.tb_memory_detail.setItem(row_No, 0, QtWidgets.QTableWidgetItem(address))
        self.tb_memory_detail.setItem(row_No, 1, QtWidgets.QTableWidgetItem(value))
        self.tb_memory_detail.setItem(row_No, 2, QtWidgets.QTableWidgetItem(str(int(value, 2))))
        address = bin(int(address, 2) + 1).replace('0b', '')
        address_new = '0' * (12 - len(address)) + address
        self.le_mar.setText(address_new)
        # self.row += 1
        self.tb_memory_detail.viewport().update()

    # load function
    def load(self):
        address = self.le_mar.text()
        value = self.memory.get(address, True)
        value_str = bin(value).replace('0b', '')
        value = '0' * (16 - len(value_str)) + value_str
        self.le_mbr.setText(str(value))

    def messageDialog(self, title, message):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, title, message)
        msg_box.exec_()

    # Single step function
    def single_step(self):
        if self.le_pc.text() == '':
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Warning',
                                            'You should reset the machine before single_step or run.')
            msg_box.exec_()
            return
        self.lbl_halt.setStyleSheet(Ui_MainWindow.gloabl_finish_process_status)
        self.lbl_run.setStyleSheet(Ui_MainWindow.gloabl_under_process_status)

        address = self.le_pc.text()
        instruction = self.memory.get(address, True)

        instruction = binaryUtils.to_binary_with_length(instruction, 16)
        logging.info('SS: Get a instruction to %s' % instruction)
        if oct(int(instruction[0:9], 2))[2:] == '0':
            logging.info('Machine Stop!')
            return self.HLT()

        self.cu.decodeAWord(instruction)

        # pc + 1
        opcode = oct(int(instruction[0:6], 2))[2:]

        if int(opcode, 8) < int('10', 8) or int(opcode, 8) > int('17', 8):
            address = self.le_pc.text()
            address = int(address, 2) + 1
            pc_str = binaryUtils.to_binary_with_length(address, 12)
            self.registers['pc'] = pc_str
            self.le_pc.setText(pc_str)

        self.lbl_halt.setStyleSheet(Ui_MainWindow.gloabl_under_process_status)
        self.lbl_run.setStyleSheet(Ui_MainWindow.gloabl_finish_process_status)

    # run function
    def run(self):
        self.lbl_run.setStyleSheet(self.gloabl_under_process_status)
        while (oct(int(binaryUtils.to_binary_with_length(self.memory.get(self.le_pc.text(), True), 16)[0:9], 2))[
               2:] != '0'):
            self.single_step()

        self.messageDialog("Halt", "Machine Stopped!")
        self.reset()
        # self.lbl_run.setStyleSheet(Ui_MainWindow.gloabl_finish_process_status)
        self.lbl_halt.setStyleSheet(Ui_MainWindow.gloabl_under_process_status)

    # Halt function
    def HLT(self):
        print('stop')
        self.reset()
        self.lbl_halt.setStyleSheet(Ui_MainWindow.gloabl_under_process_status)
        self.messageDialog("Halt", "Machine stopped!")

    def add_a_row_in_tb_by_row(self, row_No, data):
        for i in range(0, 3):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(data[i]))
            self.tb_memory_detail.setItem(row_No, i, item)