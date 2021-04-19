from GUI.mainwindow import *
from GUI.trainingwindow import *

class TrainingWindowControl():
    def __init__(self, trainingWindow):
        self.trainingWindow = trainingWindow
        self.onCancelButtonClick()

    def onCancelButtonClick(self):
        self.trainingWindow.cancelButton.clicked.connect(self.trainingWindow.close)