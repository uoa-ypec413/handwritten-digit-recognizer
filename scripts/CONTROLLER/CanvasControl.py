from GUI.canvas import *
import numpy

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
    
    def clear(self):
        self.canvas.clear()

    def getDrawing(self):
            
            drawing = self.canvas.pixmap().toImage()
            drawing = drawing.bits().asstring(700 * 800 * 4)
            drawing = numpy.fromstring(drawing, dtype=numpy.uint8).reshape((800, 700, 4))
            
            return drawing
