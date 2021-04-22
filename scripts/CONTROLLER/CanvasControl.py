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
            drawing.save('user_data/digit_drawing.jpg', "JPEG" )
