# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
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
        self.btn_IPL = QtWidgets.QPushButton(self.centralwidget)
        self.btn_IPL.setGeometry(QtCore.QRect(11, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_IPL.setFont(font)
        self.btn_IPL.setObjectName("btn_IPL")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(111, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_load.setFont(font)
        self.btn_load.setObjectName("btn_load")
        self.btn_Store = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Store.setGeometry(QtCore.QRect(211, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_Store.setFont(font)
        self.btn_Store.setObjectName("btn_Store")
        self.btn_ST = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ST.setGeometry(QtCore.QRect(311, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_ST.setFont(font)
        self.btn_ST.setObjectName("btn_ST")
        self.btn_SS = QtWidgets.QPushButton(self.centralwidget)
        self.btn_SS.setGeometry(QtCore.QRect(411, 11, 99, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_SS.setFont(font)
        self.btn_SS.setObjectName("btn_SS")
        self.btn_Run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Run.setGeometry(QtCore.QRect(517, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_Run.setFont(font)
        self.btn_Run.setObjectName("btn_Run")
        self.btn_Halt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Halt.setGeometry(QtCore.QRect(617, 11, 93, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_Halt.setFont(font)
        self.btn_Halt.setObjectName("btn_Halt")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 1920, 10))
        self.line.setMinimumSize(QtCore.QSize(500, 10))
        self.line.setMaximumSize(QtCore.QSize(1920, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lbl_gpr0 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr0.setGeometry(QtCore.QRect(12, 52, 45, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr0.setFont(font)
        self.lbl_gpr0.setObjectName("lbl_gpr0")
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
        self.btn_load_mbr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_mbr.setGeometry(QtCore.QRect(570, 131, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_mbr.setFont(font)
        self.btn_load_mbr.setObjectName("btn_load_mbr")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(600, 46, 20, 1311))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lbl_title_memory = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title_memory.setGeometry(QtCore.QRect(10, 430, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title_memory.setFont(font)
        self.lbl_title_memory.setObjectName("lbl_title_memory")
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
        self.tb_memory_detail.setRowCount(2)
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
        self.tb_memory_detail.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_memory_detail.horizontalHeader().setDefaultSectionSize(196)
        self.tb_memory_detail.horizontalHeader().setMinimumSectionSize(30)
        self.tb_memory_detail.horizontalHeader().setSortIndicatorShown(False)
        self.tb_memory_detail.horizontalHeader().setStretchLastSection(False)
        self.tb_memory_detail.verticalHeader().setVisible(True)
        self.tb_memory_detail.verticalHeader().setCascadingSectionResizes(False)
        self.tb_memory_detail.verticalHeader().setDefaultSectionSize(36)
        self.tb_memory_detail.verticalHeader().setSortIndicatorShown(False)
        self.tb_memory_detail.verticalHeader().setStretchLastSection(False)
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
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 420, 611, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
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
        self.btn_load_gpr3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_gpr3.setGeometry(QtCore.QRect(224, 166, 31, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_gpr3.setFont(font)
        self.btn_load_gpr3.setObjectName("btn_load_gpr3")
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
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 203, 321, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
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
        self.lbl_gpr3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr3.setGeometry(QtCore.QRect(12, 166, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr3.setFont(font)
        self.lbl_gpr3.setObjectName("lbl_gpr3")
        self.lbl_gpr2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr2.setGeometry(QtCore.QRect(12, 128, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr2.setFont(font)
        self.lbl_gpr2.setObjectName("lbl_gpr2")
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
        self.lbl_gpr1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gpr1.setGeometry(QtCore.QRect(12, 90, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gpr1.setFont(font)
        self.lbl_gpr1.setObjectName("lbl_gpr1")
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
        self.le_operation = QtWidgets.QLineEdit(self.centralwidget)
        self.le_operation.setGeometry(QtCore.QRect(10, 360, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_operation.setFont(font)
        self.le_operation.setText("")
        self.le_operation.setAlignment(QtCore.Qt.AlignCenter)
        self.le_operation.setReadOnly(True)
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
        self.le_gpr_input.setReadOnly(True)
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
        self.le_ixr_input.setReadOnly(True)
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
        self.le_ir_input.setReadOnly(True)
        self.le_ir_input.setObjectName("le_ir_input")
        self.le_address_input = QtWidgets.QLineEdit(self.centralwidget)
        self.le_address_input.setGeometry(QtCore.QRect(300, 360, 154, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.le_address_input.setFont(font)
        self.le_address_input.setText("")
        self.le_address_input.setAlignment(QtCore.Qt.AlignCenter)
        self.le_address_input.setReadOnly(True)
        self.le_address_input.setObjectName("le_address_input")
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
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 340, 611, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.le_store = QtWidgets.QLineEdit(self.centralwidget)
        self.le_store.setGeometry(QtCore.QRect(810, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.le_store.setFont(font)
        self.le_store.setStatusTip("")
        self.le_store.setAccessibleDescription("")
        self.le_store.setObjectName("le_store")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 9, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.btn_Halt.raise_()
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
        self.le_store.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_IPL.setText(_translate("MainWindow", "IPL"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.btn_Store.setText(_translate("MainWindow", "Store"))
        self.btn_ST.setText(_translate("MainWindow", "St++"))
        self.btn_SS.setText(_translate("MainWindow", "SingleStep"))
        self.btn_Run.setText(_translate("MainWindow", "Run"))
        self.btn_Halt.setText(_translate("MainWindow", "Halt"))
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
        self.label.setText(_translate("MainWindow", "Input:"))

