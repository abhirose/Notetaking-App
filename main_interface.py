# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1061, 111))
        self.label.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(12, 73, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.homeButton.setFont(font)
        self.homeButton.setAutoFillBackground(False)
        self.homeButton.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.homeButton.setFlat(True)
        self.homeButton.setObjectName("homeButton")
        self.insertButton = QtWidgets.QToolButton(self.centralwidget)
        self.insertButton.setGeometry(QtCore.QRect(112, 73, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.insertButton.setFont(font)
        self.insertButton.setAutoFillBackground(False)
        self.insertButton.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.insertButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.insertButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.insertButton.setObjectName("insertButton")
        self.drawButton = QtWidgets.QPushButton(self.centralwidget)
        self.drawButton.setGeometry(QtCore.QRect(212, 73, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.drawButton.setFont(font)
        self.drawButton.setAutoFillBackground(False)
        self.drawButton.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.drawButton.setFlat(True)
        self.drawButton.setObjectName("drawButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(864, 48, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 111, 1061, 51))
        self.label_2.setStyleSheet("background-color: rgb(214, 226, 213);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 162, 181, 551))
        self.label_17.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(110, 162, 941, 41))
        self.label_16.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.fontType = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontType.setEnabled(True)
        self.fontType.setGeometry(QtCore.QRect(30, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fontType.setFont(font)
        self.fontType.setAcceptDrops(False)
        self.fontType.setFrame(True)
        font = QtGui.QFont()
        self.fontType.setCurrentFont(font)
        self.fontType.setObjectName("fontType")
        self.fontSize = QtWidgets.QSpinBox(self.centralwidget)
        self.fontSize.setGeometry(QtCore.QRect(280, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fontSize.setFont(font)
        self.fontSize.setObjectName("fontSize")
        self.fontColor = QtWidgets.QPushButton(self.centralwidget)
        self.fontColor.setGeometry(QtCore.QRect(330, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.fontColor.setFont(font)
        self.fontColor.setFlat(True)
        self.fontColor.setObjectName("fontColor")
        self.boldButton = QtWidgets.QPushButton(self.centralwidget)
        self.boldButton.setGeometry(QtCore.QRect(370, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.boldButton.setFont(font)
        self.boldButton.setFlat(True)
        self.boldButton.setObjectName("boldButton")
        self.italicsButton = QtWidgets.QPushButton(self.centralwidget)
        self.italicsButton.setGeometry(QtCore.QRect(410, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        font.setUnderline(False)
        self.italicsButton.setFont(font)
        self.italicsButton.setFlat(True)
        self.italicsButton.setObjectName("italicsButton")
        self.underlineButton = QtWidgets.QPushButton(self.centralwidget)
        self.underlineButton.setGeometry(QtCore.QRect(450, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.underlineButton.setFont(font)
        self.underlineButton.setFlat(True)
        self.underlineButton.setObjectName("underlineButton")
        self.leftAlign = QtWidgets.QPushButton(self.centralwidget)
        self.leftAlign.setGeometry(QtCore.QRect(492, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        font.setKerning(True)
        self.leftAlign.setFont(font)
        self.leftAlign.setFlat(True)
        self.leftAlign.setObjectName("leftAlign")
        self.centerAlign = QtWidgets.QPushButton(self.centralwidget)
        self.centerAlign.setGeometry(QtCore.QRect(580, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        font.setKerning(True)
        self.centerAlign.setFont(font)
        self.centerAlign.setFlat(True)
        self.centerAlign.setObjectName("centerAlign")
        self.middleAlign = QtWidgets.QPushButton(self.centralwidget)
        self.middleAlign.setGeometry(QtCore.QRect(536, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        font.setKerning(True)
        self.middleAlign.setFont(font)
        self.middleAlign.setFlat(True)
        self.middleAlign.setObjectName("middleAlign")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(7, 172, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(132, 132, 132);\n"
"background-color: rgb(234, 234, 234);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(125, 172, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(132, 132, 132);\n"
"")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(9, 198, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line.setFont(font)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(182, 180, 891, 531))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabs.setFont(font)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setStyleSheet("selection-color: rgb(255, 255, 127);")
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabs.setIconSize(QtCore.QSize(21, 21))
        self.tabs.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabs.setUsesScrollButtons(True)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(True)
        self.tabs.setTabBarAutoHide(False)
        self.tabs.setObjectName("tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.canvas = QtWidgets.QTextEdit(self.tab)
        self.canvas.setGeometry(QtCore.QRect(0, 0, 881, 511))
        self.canvas.setObjectName("canvas")
        self.tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.canvas_2 = QtWidgets.QTextEdit(self.tab_2)
        self.canvas_2.setGeometry(QtCore.QRect(0, 0, 881, 511))
        self.canvas_2.setObjectName("canvas_2")
        self.tabs.addTab(self.tab_2, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(6, 6, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "Home"))
        self.insertButton.setText(_translate("MainWindow", "Insert"))
        self.drawButton.setText(_translate("MainWindow", "Draw"))
        self.label_4.setText(_translate("MainWindow", "CloneNote"))
        self.fontColor.setText(_translate("MainWindow", "A"))
        self.boldButton.setText(_translate("MainWindow", "B"))
        self.italicsButton.setText(_translate("MainWindow", "I"))
        self.underlineButton.setText(_translate("MainWindow", "U"))
        self.leftAlign.setText(_translate("MainWindow", "LA"))
        self.centerAlign.setText(_translate("MainWindow", "CA"))
        self.middleAlign.setText(_translate("MainWindow", "MA"))
        self.label_20.setText(_translate("MainWindow", "Notebooks"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_3.setText(_translate("MainWindow", "Created by Team Brute Force"))
