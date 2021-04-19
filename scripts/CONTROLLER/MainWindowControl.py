from GUI.mainwindow import *
from CONTROLLER.TrainingWindowControl import *

class MainWindowControl():
    def __init__(self, app):
        self.mainWindow = MainWindow(app)
        self.trainingWindowControl = TrainingWindowControl(self.mainWindow.trainingWindow)
        self.onExitActionClick()
        self.onTrainModelActionClick()
    
    def onExitActionClick(self):
        self.mainWindow.exitAction.triggered.connect(self.mainWindow.quitWindow)

    def onTrainModelActionClick(self):
        self.mainWindow.trainModelAction.triggered.connect(self.mainWindow.showTrainingWindow)