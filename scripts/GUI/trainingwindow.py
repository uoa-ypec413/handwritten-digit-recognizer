# This is the window from which the user can download the MNIST dataset and train the model

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

class TrainingWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training Window")
        self.resize(400, 400)
        self.center()
        self.add_console()
        self.add_progress_bar()
        self.add_buttons()
        self.set_box_layout()
        self.setWindowIcon(QIcon('media\logo.png'))

    def center(self):
        window_geometry = self.frameGeometry() # get window geometry
        center_position = QDesktopWidget().availableGeometry().center() # get monitor center position
        window_geometry.moveCenter(center_position)
        self.move(window_geometry.topLeft()) # move window to monitor centre position

    def add_buttons(self):
        self.download_button = QPushButton('Download MNIST')
        self.train_button = QPushButton('Train')
        self.cancel_button = QPushButton('Cancel')

    def add_progress_bar(self):
        self.progress_bar = QProgressBar()
    
    def add_console(self):
        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)
    
    def append_console(self, message):
        self.console.insertPlainText(message)

    def set_button_layout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.download_button)
        hbox.addWidget(self.train_button)
        self.train_button.setEnabled(False)
        hbox.addWidget(self.cancel_button)
        self.cancel_button.setEnabled(False)
        hbox.addStretch(1)
        return hbox

    def enable_train_button(self):
        self.train_button.setEnabled(True)

    def enable_cancel_button(self):
        self.cancel_button.setEnabled(True)

    def disable_download_button(self):
        self.download_button.setEnabled(False)
    
    def disable_train_button(self):
        self.train_button.setEnabled(False)
    
    def disable_cancel_button(self):
        self.cancel_button.setEnabled(False)

    def set_progress_bar_layout(self):
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)

    def set_box_layout(self):
        self.set_progress_bar_layout()
    
        vbox = QVBoxLayout()
        vbox.addWidget(self.console)
        vbox.addWidget(self.progress_bar)
        vbox.addLayout(self.set_button_layout())

        self.setLayout(vbox)
