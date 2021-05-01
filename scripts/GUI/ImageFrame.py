# Image frame for the viewer window module, displays images in a grid.

from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb
from matplotlib import pyplot as plt
import numpy as np

class ImageFrame(QFrame):

    def __init__(self):
        super().__init__()
        self.page = 0 # Initially on page 1, with an index of 0
        self.image_grid = QGridLayout() # Create the image grid
        self.setLayout(self.image_grid) # Set the layout of the frame to the image grid

        # Images are 28x28 pixels, scaled up to 100x100
        self.image = QPixmap(28, 28)
        self.image = self.image.scaled(100, 100)

        # Create the blank array to hold images
        self.image_array = []

        # Generate 100 blank placeholder images for initialization
        for i in range(100):
            self.image.fill(Qt.black)
            label = QLabel()
            label.setPixmap(self.image)
            self.image_array.append(label)
        
        self.add_images()
        
    # Given a MNIST dataset, render 100 images depending on the page into the image array.
    def render_dataset(self, dataset):
        self.image_array = []
        
        # Select the 100 images for the current page
        page_range = (self.page * 100, (self.page + 1) * 100)
        data_array = dataset.data[page_range[0]:page_range[1]]

        for data in data_array: # Iterate through the 100 images, adding them to image array
            in_image = data
            in_image = np.array(in_image, dtype='uint8').reshape((28, 28))
            # Generate a QImage object from dataset as an 8-bit grayscale image
            image = QImage(in_image, 28, 28, 28, QImage.Format_Indexed8)
            image.setColorTable([qRgb(255-i, 255-i, 255-i) for i in range(256)])

            image = image.scaled(100, 100)
            label = QLabel()
            
            # Once the image has been created it needs to be converted to a QPixmap object before
            # it can be assigned to a label for display.
            label.setPixmap(QPixmap.fromImage(image))
            self.image_array.append(label)

        self.add_images()
    
    # Add images in image array to the image grid.
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
