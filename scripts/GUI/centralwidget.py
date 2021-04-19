from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel
from PyQt5 import QtCore
from GUI.probabilityplot import *

class CentralWidget(QWidget):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.controller.setCentralWidget(self)

        self.clearButton = QPushButton('Clear')
        self.modelButton = QPushButton('Model')
        self.recogniseButton = QPushButton('Recognise')

        self.modelButton.clicked.connect(self.controller.openModel)
        self.clearButton.clicked.connect(self.controller.canvasController.clear)

        self.addPredictedDigit()
        self.setPredictedDigit(' ')

        self.addBoxLayout()

    def addBoxLayout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.clearButton)
        vbox.addWidget(self.modelButton)
        vbox.addWidget(self.recogniseButton)
        vbox.addWidget(self.controller.probabilityController.plot)
        vbox.addWidget(self.predictedDigit)

        hbox = QHBoxLayout()
        hbox.addWidget(self.controller.canvasController.canvas)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def addPredictedDigit(self):
        self.predictedDigit = QLabel()
        self.predictedDigit.setAlignment(QtCore.Qt.AlignCenter)
        font = self.predictedDigit.font()
        font.setPointSize(36)
        self.predictedDigit.setFont(font)
        self.predictedDigit.setStyleSheet("border: 1px solid black;") # set border
    
    def setPredictedDigit(self, d):
        self.predictedDigit.setText(d)