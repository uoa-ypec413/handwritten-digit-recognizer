from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QPainter, QPen, QCursor

class Canvas(QLabel):

    def __init__(self):
        super().__init__()
        self.image = QPixmap(700, 800)
        self.image.fill(QtCore.Qt.white)

        self.setPixmap(self.image)
        self.setStyleSheet("border: 1px solid black;") # set border
        self.setCursor(QCursor(QtCore.Qt.CrossCursor))

        self.lastPos = None

    def mouseMoveEvent(self, event):
        if self.lastPos is None: # On the first mouse event, do not paint, just save position
            self.lastPos = event.pos()
        else:
            currentPos = event.pos()
            self.painter = QPainter(self.pixmap())
            self.painter.setPen(QPen(QtCore.Qt.black,  12, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            self.painter.drawLine(self.lastPos, currentPos)
            self.painter.end()

            self.lastPos = currentPos
            self.update()

    def mouseReleaseEvent(self, event):
        self.lastPos = None

    def clearCanvas(self):
        self.setPixmap(self.image)