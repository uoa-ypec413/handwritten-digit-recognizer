# Canvas for drawing, part of the central widget of the main window.

from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QPainter, QPen, QCursor

class Canvas(QLabel):

    # Initialises the canvas object, takes it's controller object as an input
    # so that it can send user mouse events to it's controller.
    def __init__(self, controller):
        super().__init__()
        # Creates a blank image to act as the drawing area
        self.image = QPixmap(700, 700)
        self.image.fill(QtCore.Qt.white)
        self.setPixmap(self.image)
        self.setStyleSheet("border: 1px solid black;") # set border
        self.setCursor(QCursor(QtCore.Qt.CrossCursor)) # set cursor to a cross for easier drawing
        
        self.controller = controller # Save controller object
    
    # Call controller each time the mouse is clicked and dragged to handle drawing functions
    def mouseMoveEvent(self, event):
        self.controller.on_mouse_move(event.pos())
    
    # Call controller each time the mouse is released to handle drawing functions
    def mouseReleaseEvent(self, event):
        self.controller.on_mouse_release()

    # Draws a line on the canvas between two given positions
    def draw_line(self, lastPos, currentPos):
        self.painter = QPainter(self.pixmap())  # QPainter object allows drawing on a pixmap
        self.painter.setPen(QPen(QtCore.Qt.black, 60, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        self.painter.drawLine(lastPos, currentPos) # Draw a line between the two position inputs
        self.painter.end() # Stop drawing
        self.update() # Update image

    # Sets the pixmap to be plain white (blank)
    def clear(self):
        self.setPixmap(self.image) 
