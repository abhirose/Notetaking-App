
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
 
# window class
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # title
        self.setWindowTitle("Drawing Tool")
 
        # main window size
        self.setGeometry(100, 100, 800, 600)
 
        # creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)
 
        # setting page background color
        self.image.fill(Qt.white)
 
        # variables
        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 2
        # default color
        self.brushColor = Qt.green
 
        # QPoint object to tract the point
        self.lastPoint = QPoint()
 
        # creating menu bar
        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("color: darkslategray;" "background-color: lightgrey;" "selection-color: white;" "selection-background-color: lightgreen;")
 
        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")
 
        # adding brush size to main menu
        b_size = mainMenu.addMenu("Brush Size")
 
        # adding brush color to main menu
        b_color = mainMenu.addMenu("Brush Color")
 
        # creating save action
        saveAction = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save", self)
        # adding short cut for save action
        saveAction.setShortcut("Ctrl + S")
        # adding save to the file menu
        fileMenu.addAction(saveAction)
        # adding action to the save
        saveAction.triggered.connect(self.save)
 
        # creating clear action
        clearAction = QAction("Clear", self)
        # adding short cut to the clear action
        clearAction.setShortcut("Ctrl + C")
        # adding clear to the file menu
        fileMenu.addAction(clearAction)
        # adding action to the clear
        clearAction.triggered.connect(self.clear)
 
        # creating options for brush sizes
        # creating action for selecting pixel of 1px
        pix_1 = QAction(QIcon(os.path.join('images', '1-px.png')), "1px", self)
        # adding this action to the brush size
        b_size.addAction(pix_1)
        # adding method to this
        pix_1.triggered.connect(self.Pixel_1)
 
        # repeat above steps for additional brush sizes
        pix_2 = QAction(QIcon(os.path.join('images', '2-px.png')), "2px", self)
        b_size.addAction(pix_2)
        pix_2.triggered.connect(self.Pixel_2)
        
        pix_4 = QAction(QIcon(os.path.join('images', '4-px.png')), "4px", self)
        b_size.addAction(pix_4)
        pix_4.triggered.connect(self.Pixel_4)
        
        pix_7 = QAction(QIcon(os.path.join('images', '7-px.png')), "7px", self)
        b_size.addAction(pix_7)
        pix_7.triggered.connect(self.Pixel_7)
 
        pix_9 = QAction(QIcon(os.path.join('images', '9-px.png')), "9px", self)
        b_size.addAction(pix_9)
        pix_9.triggered.connect(self.Pixel_9)
 
        pix_12 = QAction(QIcon(os.path.join('images', '12-px.png')), "12px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)
 
        # creating options for brush color
        # creating action for black color
        black = QAction(QIcon(os.path.join('images', 'black-color.png')), "Black", self)
        # adding this action to the brush colors
        b_color.addAction(black)
        # adding methods to the black
        black.triggered.connect(self.blackColor)
 
        # similarly repeating above steps for different color
        white = QAction(QIcon(os.path.join('images', 'white-color.png')), "White", self)
        b_color.addAction(white)
        white.triggered.connect(self.whiteColor)
 
        green = QAction(QIcon(os.path.join('images', 'green-color.png')), "Green", self)
        b_color.addAction(green)
        green.triggered.connect(self.greenColor)
 
        red = QAction(QIcon(os.path.join('images', 'red-color.png')), "Red", self)
        b_color.addAction(red)
        red.triggered.connect(self.redColor)
  
        yellow = QAction(QIcon(os.path.join('images', 'yellow-color.png')), "Yellow", self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)

 
        blue = QAction(QIcon(os.path.join('images', 'blue-color.png')), "Blue", self)
        b_color.addAction(blue)
        blue.triggered.connect(self.blueColor)
 

 
    # method for checking mouse cicks
    def mousePressEvent(self, event):
 
        # if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            # make drawing flag true
            self.drawing = True
            # make last point to the point of cursor
            self.lastPoint = event.pos()
 
    # method for tracking mouse activity
    def mouseMoveEvent(self, event):
         
        # checking if left button is pressed and drawing flag is true
        if (event.buttons() & Qt.LeftButton) & self.drawing:
             
            # creating painter object
            painter = QPainter(self.image)
             
            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
             
            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())
             
            # change the last point
            self.lastPoint = event.pos()
            # update
            self.update()
 
    # method for mouse left button release
    def mouseReleaseEvent(self, event):
 
        if event.button() == Qt.LeftButton:
            # make drawing flag false
            self.drawing = False
 
    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)
         
        # draw rectangle  on the canvas
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
 
    # method for saving canvas
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                          "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
 
        if filePath == "":
            return
        self.image.save(filePath)
 
    # method for clearing every thing on canvas
    def clear(self):
        # make the whole canvas white
        self.image.fill(Qt.white)
        # update
        self.update()
 
    # methods for changing pixel sizes
    def Pixel_1(self):
        self.brushSize = 1
    
    def Pixel_2(self):
        self.brushSize = 2
        
    def Pixel_4(self):
        self.brushSize = 4
 
    def Pixel_7(self):
        self.brushSize = 7
 
    def Pixel_9(self):
        self.brushSize = 9
 
    def Pixel_12(self):
        self.brushSize = 12
 
    # methods for changing brush color
    def blackColor(self):
        self.brushColor = Qt.black
 
    def whiteColor(self):
        self.brushColor = Qt.white
 
    def greenColor(self):
        self.brushColor = Qt.green
    
    def redColor(self):
        self.brushColor = Qt.red
 
    def yellowColor(self):
        self.brushColor = Qt.yellow
    
    def blueColor(self):
        self.brushColor = Qt.blue
 

 
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# showing the window
window.show()
 
# start the app
sys.exit(App.exec())