from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ImageFrame(QFrame):

    def __init__(self):
        super().__init__()
        self.imageGrid = QGridLayout()
        self.addImages()
        self.setLayout(self.imageGrid)

    def addImages(self):
        imageArray = []
        image = QPixmap(28, 28)
        image = image.scaled(100, 100)
        image.fill(Qt.black)

        for i in range(0,100):
            label = QLabel()
            label.setPixmap(image)
            imageArray.append(label)

        row = 0
        column = 0
        for images in imageArray:
            
            self.imageGrid.addWidget(images, row, column)

            if column == 7:
                row += 1
                column = 0
            else:
                column += 1