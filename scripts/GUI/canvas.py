# Canvas for drawing, part of the central widget of the main window.

from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QPainter, QPen, QCursor

class Canvas(QLabel):

    def __init__(self, controller):
        super().__init__()
        self.image = QPixmap(700, 700)
        self.image.fill(QtCore.Qt.white)
        self.setPixmap(self.image)
        self.setStyleSheet("border: 1px solid black;") # set border
        self.setCursor(QCursor(QtCore.Qt.CrossCursor))

        self.controller = controller
    
    ### Following two functions call controller, to preserve MVC design principle ###
    def mouseMoveEvent(self, event):
        self.controller.on_mouse_move(event.pos())
    
    def mouseReleaseEvent(self, event):
        self.controller.on_mouse_release()

    # Draws a line on the canvas between two given positions
    def draw_line(self, lastPos, currentPos):
        self.painter = QPainter(self.pixmap())
        self.painter.setPen(QPen(QtCore.Qt.black, 60, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        self.painter.drawLine(lastPos, currentPos)
        self.painter.end()
        self.update()

    def clear(self):
        self.setPixmap(self.image)
