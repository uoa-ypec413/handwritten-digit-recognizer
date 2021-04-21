from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import random

class ImageFrame(QFrame):

    def __init__(self):
        super().__init__()
        self.imageGrid = QGridLayout()

        self.colour_array = [Qt.white, Qt.red, Qt.green, Qt.blue, Qt.black, Qt.cyan, Qt.magenta, Qt.yellow]

        self.page = 0

        self.imageArray = []
        self.image = QPixmap(28, 28)
        self.image = self.image.scaled(100, 100)

        for i in range(0,60):
            self.image.fill(self.colour_array[random.randrange(0, 7)])
            label = QLabel()
            label.setPixmap(self.image)
            self.imageArray.append(label)
        
        self.addImages()
        self.setLayout(self.imageGrid)

    def addImages(self):

        #range = (self.page * 1000, (self.page + 1) * 1000)
        range = (0,60)
        self.image_range = self.imageArray[range[0]:range[1]]

        row = 0
        column = 0
        for images in self.image_range:
            
            self.imageGrid.addWidget(images, row, column)

            if column == 7:
                row += 1
                column = 0
            else:
                column += 1
    
    def clearGrid(self):
        for images in self.image_range:
            images.setParent(None)


    def setPage(self, page):
        self.page = page
        print(self.page)
        self.clearGrid()
        self.addImages()
