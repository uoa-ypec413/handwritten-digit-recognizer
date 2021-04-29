from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb
from matplotlib import pyplot as plt
import numpy as np

class ImageFrame(QFrame):

    def __init__(self):
        super().__init__()
        self.page = 0
        self.image_grid = QGridLayout()
        self.setLayout(self.image_grid)
        self.image = QPixmap(28, 28)
        self.image = self.image.scaled(100, 100)
        self.image_array = []
        for i in range(100):
            self.image.fill(Qt.black)
            label = QLabel()
            label.setPixmap(self.image)
            self.image_array.append(label)
        
        self.add_images()
        

    def render_dataset(self, dataset):
        self.image_array = []
        
        page_range = (self.page * 100, (self.page + 1) * 100)
        data_array = dataset.data[page_range[0]:page_range[1]]

        for data in data_array:
            in_image = data
            in_image = np.array(in_image, dtype='uint8').reshape((28, 28))
            image = QImage(in_image, 28, 28, 28, QImage.Format_Indexed8)
            image.setColorTable([qRgb(255-i, 255-i, 255-i) for i in range(256)])
            image = image.scaled(100, 100)
            label = QLabel()
            label.setPixmap(QPixmap.fromImage(image))
            self.image_array.append(label)

        self.add_images()
    
    def add_images(self):
        self.row = 0
        self.column = 0

        for images in self.image_array:
            
            self.image_grid.addWidget(images, self.row, self.column)

            if self.column == 7:
                self.row += 1
                self.column = 0
            else:
                self.column += 1


    def set_page(self, page):
        self.page = page
