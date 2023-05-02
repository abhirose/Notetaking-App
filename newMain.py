from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os
import sys
import uuid

class NewMain(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(NewMain, self).__init__(*args, **kwargs)
        uic.loadUi("draw2.ui", self)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Megasolid Idiom")

    window = NewMain()
    app.exec_()
