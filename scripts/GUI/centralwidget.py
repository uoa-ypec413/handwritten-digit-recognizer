from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel
from PyQt5 import QtCore
from GUI.ProbabilityPlot import *

class CentralWidget(QWidget):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.clear_button = QPushButton('Clear')
        self.model_button = QPushButton('Model')
        self.recognise_button = QPushButton('Recognise')

        self.add_predicted_digit()
        self.set_predicted_digit(' ')

        self.add_box_layout()

    def add_box_layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.clear_button)
        vbox.addWidget(self.model_button)
        vbox.addWidget(self.recognise_button)
        vbox.addWidget(self.controller.probability_controller.plot)
        vbox.addWidget(self.predicted_digit)

        hbox = QHBoxLayout()
        hbox.addWidget(self.controller.canvas_controller.canvas)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def add_predicted_digit(self):
        self.predicted_digit = QLabel()
        self.predicted_digit.setAlignment(QtCore.Qt.AlignCenter)
        font = self.predicted_digit.font()
        font.setPointSize(36)
        self.predicted_digit.setFont(font)
        self.predicted_digit.setStyleSheet("border: 1px solid black;") # set border
    
    def set_predicted_digit(self, d):
        self.predicted_digit.setText(d)