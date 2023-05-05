from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from main_interface import *
from TextBox_Tool import *

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

class TextEdit(QTextEdit):

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = splitext(str(u.toLocalFile()))
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break

            else:
                # If all were valid images, finish here.
                return


        elif source.hasImage():
            image = source.imageData()
            uuid = hexuuid()
            document.addResource(QTextDocument.ImageResource, uuid, image)
            cursor.insertImage(uuid)
            return

        super(TextEdit, self).insertFromMimeData(source)


class NewMain(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(NewMain, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.canvas.setAutoFormatting(QTextEdit.AutoAll)
        self.ui.canvas.selectionChanged.connect(self.update_format)
        # Initialize default font size.
        font = QFont('Times', 12)
        self.ui.canvas.setFont(font)
        # We need to repeat the size to init the current format.
        self.ui.canvas.setFontPointSize(12)

        self.ui.fontType.currentFontChanged.connect(self.ui.canvas.setCurrentFont)
        
        self.ui.fontSize = QComboBox()
        self.ui.fontSize.addItems([str(s) for s in FONT_SIZES])
        self.ui.fontSize.currentIndexChanged[str].connect(lambda s: self.ui.canvas.setFontPointSize(float(s)) )

        self.ui.boldButton.setShortcut(QKeySequence.Bold)
        self.ui.boldButton.setCheckable(True)
        self.ui.boldButton.toggled.connect(lambda x: self.ui.canvas.setFontWeight(QFont.Bold if x else QFont.Normal))

        self.ui.italicsButton.setShortcut(QKeySequence.Italic)
        self.ui.italicsButton.setCheckable(True)
        self.ui.italicsButton.toggled.connect(self.ui.canvas.setFontItalic)

        self.ui.underlineButton.setShortcut(QKeySequence.Underline)
        self.ui.underlineButton.setCheckable(True)
        self.ui.underlineButton.toggled.connect(self.ui.canvas.setFontUnderline)

        self.ui.leftAlign.setCheckable(True)
        self.ui.leftAlign.toggled.connect(lambda: self.ui.canvas.setAlignment(Qt.AlignLeft))

        self.ui.centerAlign.setCheckable(True)
        self.ui.centerAlign.toggled.connect(lambda: self.ui.canvas.setAlignment(Qt.AlignCenter))

        #self.rightAlign.setCheckable(True)
        #self.rightAlign.toggled.connect(lambda: self.canvas.setAlignment(Qt.AlignRight))

        self.ui.middleAlign.setCheckable(True)
        self.ui.middleAlign.toggled.connect(lambda: self.ui.canvas.setAlignment(Qt.AlignJustify))

        insertmenu = QMenu("Insert Menu", self.ui.insertButton)
        insertmenu.addAction("Text Box", self.TextBoxInstance)
        self.ui.insertButton.setMenu(insertmenu)

    def TextBoxInstance(self):
        textbox = TextBox()
        #Text Box cannot be displayed to canvas since canvas widget is a QTextEdit so it would have to another type
        #of widget like QGraphicsView/QGraphicsScene

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
        #self.ui.block_signals(self._format_actions, True)

        self.ui.fontType.setCurrentFont(self.ui.canvas.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        self.ui.fontSize.setCurrentText(str(int(self.ui.canvas.fontPointSize())))

        self.ui.italicsButton.setChecked(self.ui.canvas.fontItalic())
        self.ui.underlineButton.setChecked(self.ui.canvas.fontUnderline())
        self.ui.boldButton.setChecked(self.ui.canvas.fontWeight() == QFont.Bold)

        self.ui.leftAlign.setChecked(self.ui.canvas.alignment() == Qt.AlignLeft)
        self.ui.centerAlign.setChecked(self.ui.canvas.alignment() == Qt.AlignCenter)
        #self.ui.alignr_action.setChecked(self.canvas.alignment() == Qt.AlignRight)
        self.ui.middleAlign.setChecked(self.ui.canvas.alignment() == Qt.AlignJustify)

        #self.ui.block_signals(self._format_actions, False)

"""
WILL HAVE TO PUT THEM IN STACKED WIDGET TO WORK IN JUST ONE SCREEN
class DrawScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(DrawScreen, self).__init__(*args, **kwargs)
        uic.loadUi("draw2.ui", self)
        self.show()
"""
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("CloneNote")

    window = NewMain()
    window.show()
    app.exec_()
