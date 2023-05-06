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
        
        self.fontSize.addItems([str(s) for s in FONT_SIZES])
        self.fontSize.currentIndexChanged[str].connect(lambda s: self.canvas.setFontPointSize(float(s)) )

        self.fontColor.clicked.connect(self.fontColorChange)

        self.boldButton.setShortcut(QKeySequence.Bold)
        self.boldButton.setCheckable(True)
        self.boldButton.toggled.connect(lambda x: self.canvas.setFontWeight(QFont.Bold if x else QFont.Normal))

        self.italicsButton.setShortcut(QKeySequence.Italic)
        self.italicsButton.setCheckable(True)
        self.italicsButton.toggled.connect(self.canvas.setFontItalic)

        self.underlineButton.setShortcut(QKeySequence.Underline)
        self.underlineButton.setCheckable(True)
        self.underlineButton.toggled.connect(self.canvas.setFontUnderline)

        self.leftAlign.setCheckable(True)
        self.leftAlign.toggled.connect(lambda: self.canvas.setAlignment(Qt.AlignLeft))

        self.centerAlign.setCheckable(True)
        self.centerAlign.toggled.connect(lambda: self.canvas.setAlignment(Qt.AlignCenter))

        self.rightAlign.setCheckable(True)
        self.rightAlign.toggled.connect(lambda: self.canvas.setAlignment(Qt.AlignRight))

        self.middleAlign.setCheckable(True)
        self.middleAlign.toggled.connect(lambda: self.canvas.setAlignment(Qt.AlignJustify))



        insertmenu = QMenu("Insert Menu", self.insertButton)
        insertmenu.addAction("Text Box", self.TextBoxInstance)
        self.insertButton.setMenu(insertmenu)

    def fontColorChange(self):
        color = QColorDialog.getColor()
        self.canvas.setTextColor(color)

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
        #self.block_signals(self._format_actions, True)

        self.fontType.setCurrentFont(self.canvas.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        self.fontSize.setCurrentText(str(int(self.canvas.fontPointSize())))

        self.italicsButton.setChecked(self.canvas.fontItalic())
        self.underlineButton.setChecked(self.canvas.fontUnderline())
        self.boldButton.setChecked(self.canvas.fontWeight() == QFont.Bold)

        self.leftAlign.setChecked(self.canvas.alignment() == Qt.AlignLeft)
        self.centerAlign.setChecked(self.canvas.alignment() == Qt.AlignCenter)
        self.rightAlign.setChecked(self.canvas.alignment() == Qt.AlignRight)
        self.middleAlign.setChecked(self.canvas.alignment() == Qt.AlignJustify)

        #self.block_signals(self._format_actions, False)

"""
WILL HAVE TO PUT THEM IN STACKED WIDGET TO WORK IN JUST ONE SCREEN
class DrawScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(DrawScreen, self).__init__(*args, **kwargs)
        uic.loadUi("draw2", self)
        self.show()
"""
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("CloneNote")

    window = NewMain()
    app.exec_()
