# Central widget for the main window

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel
from PyQt5 import QtCore

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

    # Layout function for the central widget
    def add_box_layout(self):
        # Vertically stacked widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.clear_button)
        vbox.addWidget(self.model_button)
        vbox.addWidget(self.recognise_button)
        vbox.addWidget(self.controller.probability_controller.plot)
        vbox.addWidget(self.predicted_digit)

        # Horizontally stacked widgets
        hbox = QHBoxLayout()
        hbox.addWidget(self.controller.canvas_controller.canvas)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    # Adds the predicted digit display in the lower right-hand corner of the main window.
    # The predicted digit is the digit class that the model thinks is most likely for a given user drawing.
    def add_predicted_digit(self):
        self.predicted_digit = QLabel()
        self.predicted_digit.setAlignment(QtCore.Qt.AlignCenter)
        font = self.predicted_digit.font()
        font.setPointSize(36)
        self.predicted_digit.setFont(font)
        self.predicted_digit.setStyleSheet("border: 1px solid black;") # set border
    
    def set_predicted_digit(self, d):
        self.predicted_digit.setText(d)
