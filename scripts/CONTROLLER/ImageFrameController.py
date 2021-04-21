from GUI.imageframe import *

class ImageFrameController():
    def __init__(self):
        self.imageFrame = ImageFrame()
    
    def updatePage(self, page):
        self.imageFrame.setPage(page)