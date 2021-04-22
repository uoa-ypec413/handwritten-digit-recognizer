from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb
from matplotlib import pyplot as plt
import numpy as np

class ImageFrame(QFrame):

    def __init__(self):
        super().__init__()
        self.page = 0
        self.imageArray = []
        self.imageGrid = QGridLayout()
        self.setLayout(self.imageGrid)
        self.image = QPixmap(28, 28)
        self.image = self.image.scaled(100, 100)
        self.imageArray = []
        for i in range(100):
            self.image.fill(Qt.black)
            label = QLabel()
            label.setPixmap(self.image)
            self.imageArray.append(label)
        
        self.addImages()
        

    def render_dataset(self, dataset):
        self.imageArray = []
        
        page_range = (self.page * 100, (self.page + 1) * 100)
        dataArray = dataset.data[page_range[0]:page_range[1]]

        for data in dataArray:
            in_image = data
            in_image = np.array(in_image, dtype='uint8').reshape((28, 28))
            image = QImage(in_image, 28, 28, 28, QImage.Format_Indexed8)
            image.setColorTable([qRgb(255-i, 255-i, 255-i) for i in range(256)])
            image = image.scaled(100, 100)
            label = QLabel()
            label.setPixmap(QPixmap.fromImage(image))
            self.imageArray.append(label)

        # in_image = dataset.data[0]
        # in_image = np.array(in_image, dtype='uint8').reshape((28, 28))

        # image = QImage(in_image, 28, 28, 28, QImage.Format_Indexed8)
        # image.setColorTable([qRgb(255-i, 255-i, 255-i) for i in range(256)])
        # image = image.scaled(100, 100)
        # label = QLabel()
        # label.setPixmap(QPixmap.fromImage(image))
        # self.imageArray.append(label)
        self.addImages()
    
    def addImages(self):
        
        #page_range = (self.page * 50, (self.page + 1) * 50)
        #self.image_range = self.imageArray[page_range[0]:page_range[1]]
        self.row = 0
        self.column = 0

        for images in self.imageArray:
            
            self.imageGrid.addWidget(images, self.row, self.column)

            if self.column == 7:
                self.row += 1
                self.column = 0
            else:
                self.column += 1


    def setPage(self, page):
        self.page = page
