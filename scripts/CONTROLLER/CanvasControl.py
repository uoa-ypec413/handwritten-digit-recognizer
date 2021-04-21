from GUI.canvas import *
import numpy
from PyQt5.QtCore import Qt

class canvasController():
    def __init__(self):

        self.canvas = Canvas(self)
        self.lastPos = None

    def onMouseMove(self, position):
        if self.lastPos is None: # On the first mouse event, do not paint, just save position
            self.lastPos = position
        else:
            currentPos = position
            self.canvas.drawLine(self.lastPos, currentPos)
            self.lastPos = currentPos
    
    def onMouseRelease(self):
        self.lastPos = None
        self.saveDrawing()
    
    def clear(self):
        self.canvas.clear()

    def saveDrawing(self):

            drawing = self.canvas.pixmap()
            drawing = drawing.scaled(28, 28, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            drawing.save('user_data/digit_drawing.jpg', "JPEG" )

            '''drawing = self.canvas.pixmap().toImage()
            drawing = drawing.bits().asstring(700 * 800 * 4)
            drawing = numpy.fromstring(drawing, dtype=numpy.uint8).reshape((800, 700, 4))'''
