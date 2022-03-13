from PyQt5.QtCore import  QRect
import logging

from PyQt5.QtWidgets import QPlainTextEdit


class QPlainTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.log_area = QPlainTextEdit(parent)
        self.log_area.setObjectName(u"log_area")
        self.log_area.setGeometry(QRect(611, 88, 861, 391))
        self.log_area.setUndoRedoEnabled(False)
        self.log_area.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.log_area.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.log_area.appendPlainText(msg)