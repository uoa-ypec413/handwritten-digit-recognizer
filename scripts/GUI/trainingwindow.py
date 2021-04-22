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
        self.addConsole()
        self.addProgressBar()
        self.addButtons()
        self.setBoxLayout()
        self.setWindowIcon(QIcon('media\logo.png'))

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

    def addButtons(self):
        self.downloadButton = QPushButton('Download MNIST')
        self.trainButton = QPushButton('Train')
        self.cancelButton = QPushButton('Cancel')

    def addProgressBar(self):
        self.progressBar = QProgressBar()
    
    def addConsole(self):
        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)
    
    def appendConsole(self, message):
        self.console.insertPlainText(message)

    def setButtonLayout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.downloadButton)
        hbox.addWidget(self.trainButton)
        self.trainButton.setEnabled(False)
        hbox.addWidget(self.cancelButton)
        self.cancelButton.setEnabled(False)
        hbox.addStretch(1)

        return hbox

    def enableTrainButton(self):
        self.trainButton.setEnabled(True)

    def enableCancelButton(self):
        self.cancelButton.setEnabled(True)

    def disableDownloadButton(self):
        self.downloadButton.setEnabled(False)
    
    def disableTrainButton(self):
        self.trainButton.setEnabled(False)
    
    def disableCancelButton(self):
        self.cancelButton.setEnabled(False)

    def setProgressBarLayout(self):
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)

    def setBoxLayout(self):
        self.setProgressBarLayout()
    
        vbox = QVBoxLayout()
        vbox.addWidget(self.console)
        vbox.addWidget(self.progressBar)
        vbox.addLayout(self.setButtonLayout())

        self.setLayout(vbox)
