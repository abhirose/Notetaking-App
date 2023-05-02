from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os
import sys
import uuid

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS = ['.jpg','.png','.bmp']
HTML_EXTENSIONS = ['.htm', '.html']

def hexuuid():
    return uuid.uuid4().hex

def splitext(p):
    return os.path.splitext(p)[1].lower()

class NewMain(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(NewMain, self).__init__(*args, **kwargs)
        uic.loadUi("main2.ui", self)
        self.show()

        self.canvas.setAutoFormatting(QTextEdit.AutoAll)
        self.canvas.selectionChanged.connect(self.update_format)
        # Initialize default font size.
        font = QFont('Times', 12)
        self.canvas.setFont(font)
        # We need to repeat the size to init the current format.
        self.canvas.setFontPointSize(12)

        self.fontType.currentFontChanged.connect(self.canvas.setCurrentFont)

        self.fontSize = QComboBox()
        self.fontSize.addItems([str(s) for s in FONT_SIZES])
        self.fontSize.currentIndexChanged[str].connect(lambda s: self.canvas.setFontPointSize(float(s)) )

        self.boldButton.setShortcut(QKeySequence.Bold)
        self.boldButton.setCheckable(True)
        self.boldButton.toggled.connect(lambda x: self.canvas.setFontWeight(QFont.Bold if x else QFont.Normal))



    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        #self.block_signals(self._format_actions, True)

        self.fontType.setCurrentFont(self.canvas.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        self.fontSize.setCurrentText(str(int(self.canvas.fontPointSize())))

        self.italic_action.setChecked(self.canvas.fontItalic())
        self.underline_action.setChecked(self.canvas.fontUnderline())
        self.boldButton.setChecked(self.canvas.fontWeight() == QFont.Bold)

        self.alignl_action.setChecked(self.canvas.alignment() == Qt.AlignLeft)
        self.alignc_action.setChecked(self.canvas.alignment() == Qt.AlignCenter)
        self.alignr_action.setChecked(self.canvas.alignment() == Qt.AlignRight)
        self.alignj_action.setChecked(self.canvas.alignment() == Qt.AlignJustify)

        #self.block_signals(self._format_actions, False)

    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Megasolid Idiom")

    window = NewMain()
    app.exec_()
