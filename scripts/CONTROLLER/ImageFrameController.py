from GUI.imageframe import *

class ImageFrameController():
    def __init__(self):
        self.imageFrame = ImageFrame()
    
    def updatePage(self, page):
        self.imageFrame.setPage(page)
        self.load_dataset(self.dataset)
    
    def load_dataset(self, dataset):
        self.dataset = dataset
        #self.imageFrame.clearGrid()
        self.imageFrame.render_dataset(dataset)
        #self.imageFrame.addImages()