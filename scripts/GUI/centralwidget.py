from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5 import QtCore
from GUI.probabilityplot import *
from GUI.canvas import *

class CentralWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.classProbability = probabilityPlot()
        self.canvas = Canvas()
        self.clearButton = QPushButton('Clear')
        self.modelButton = QPushButton('Model')
        self.recogniseButton = QPushButton('Recognise')
        self.modelButton.clicked.connect(self.openModel)
        self.clearButton.clicked.connect(self.canvas.clearCanvas)
        self.addPredictedDigit()
        self.setPredictedDigit()
        self.addBoxLayout()

    def addBoxLayout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.clearButton)
        vbox.addWidget(self.modelButton)
        vbox.addWidget(self.recogniseButton)
        vbox.addWidget(self.classProbability)
        vbox.addWidget(self.predictedDigit)

        hbox = QHBoxLayout()
        hbox.addWidget(self.canvas)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def addPredictedDigit(self):
        self.predictedDigit = QLabel()
        self.predictedDigit.setAlignment(QtCore.Qt.AlignCenter)
        font = self.predictedDigit.font()
        font.setPointSize(36)
        self.predictedDigit.setFont(font)
        self.predictedDigit.setStyleSheet("border: 1px solid black;") # set border
    
    def setPredictedDigit(self):
        self.predictedDigit.setText('3')

    def openModel(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './') # create file dialog
        if fname[0]:
            f = open(fname[0], 'r')