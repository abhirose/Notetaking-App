from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from resources.textbox import *
import os
import sys

class TextBox(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Textbox()
        self.ui.setupUi(self)
        self.ui.Box.setWindowFlags(Qt.SubWindow)
        self.textpos = 24
        self.Start()
    def Start(self):
        self.ui.MeatballIcon.mousePressEvent = self.mouseDragButton
        self.ui.DragWidget.mousePressEvent = self.mouseDragButton
        self.ui.MeatballIcon.mouseMoveEvent = self.draggingMomemt
        self.ui.DragWidget.mouseMoveEvent = self.draggingMomemt
        self.ui.MeatballIcon.mouseReleaseEvent = self.droppingMoment
        self.ui.DragWidget.mouseReleaseEvent = self.droppingMoment

        self.ui.textEditor.keyReleaseEvent = self.ResizeTextPortion

        self.ui.WidthChanger.mousePressEvent = self.mouseHorizontalButton
        self.ui.HorizontalArrowsIcon.mousePressEvent = self.mouseHorizontalButton
        self.ui.WidthChanger.mouseMoveEvent = self.HorizontalChange
        self.ui.HorizontalArrowsIcon.mouseMoveEvent = self.HorizontalChange
        self.ui.WidthChanger.mouseReleaseEvent = self.HorizontalChangeMade
        self.ui.HorizontalArrowsIcon.mouseReleaseEvent = self.HorizontalChangeMade

    def ResizeTextPortion(self, event): #Doesnt count for font size yet
        if(self.textpos < self.ui.textEditor.document().size().height()):
            self.textpos = self.ui.textEditor.document().size().height()
            self.ui.Box.resize(self.ui.Box.width(), self.ui.Box.height() + 16)
            self.ui.BottomFrame.resize(self.ui.BottomFrame.width(), self.ui.BottomFrame.height() + 16)
            self.ui.textEditor.resize(self.ui.textEditor.width(), int(self.ui.textEditor.document().size().height() + 16))
            self.ui.textEditor.updateGeometry()
            self.ui.textEditor.ensureCursorVisible()
        elif(self.textpos > self.ui.textEditor.document().size().height()):
            self.textpos = self.ui.textEditor.document().size().height()
            self.ui.Box.resize(self.ui.Box.width(), self.ui.Box.height() - 16)
            self.ui.BottomFrame.resize(self.ui.BottomFrame.width(), self.ui.BottomFrame.height() - 16)
            self.ui.textEditor.resize(self.ui.textEditor.width(), int(self.ui.textEditor.height() - 16))
            self.ui.Box.updateGeometry()
            self.ui.BottomFrame.updateGeometry()
            self.ui.textEditor.updateGeometry()
            self.ui.textEditor.ensureCursorVisible()

    def mouseHorizontalButton(self, event):
        if(event.buttons() == Qt.LeftButton):
            self.width = self.ui.Box.width()
            self.oldwidth = event.globalPos()
            self.resizing = True
            event.accept()
    def HorizontalChange(self, event): #Width Resizing Buggy
        if((event.buttons() == Qt.LeftButton) and self.resizing):
            delta = event.globalPos() - self.oldwidth
            width = self.width + delta.x()
            self.ui.Box.resize(self.ui.Box.width() + delta.x(), self.ui.Box.height())
            self.ui.TopFrame.resize(self.ui.TopFrame.width() + delta.x(), self.ui.TopFrame.height())
            self.ui.BottomFrame.resize(self.ui.BottomFrame.width() + delta.x(), self.ui.BottomFrame.height())
            self.ui.textEditor.resize(self.ui.textEditor.width() + delta.x(), self.ui.textEditor.height())
            self.ui.Box.updateGeometry()
            self.ui.TopFrame.updateGeometry()
            self.ui.BottomFrame.updateGeometry()
            self.ui.textEditor.updateGeometry()
        event.accept()

    def HorizontalChangeMade(self, event):
        self.resizing = False
        event.accept()

    def mouseDragButton(self, event):
        if (event.buttons() == Qt.LeftButton):
            self.pos = event.pos()
            
    def draggingMomemt(self, event):
        if (event.buttons() == Qt.LeftButton):
            self.ui.Box.move(self.ui.Box.mapToParent(event.pos() - self.pos))
        event.accept()

    def droppingMoment(self, event):
        event.accept()
