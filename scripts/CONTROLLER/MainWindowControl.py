from GUI.mainwindow import *
from CONTROLLER.TrainingWindowControl import *

class MainWindowControl():
    def __init__(self, app, digit_recogniser_controller):
        self.main_window = MainWindow(app)
        self.trainingWindowControl = TrainingWindowControl(self.main_window.trainingWindow, digit_recogniser_controller)
        self.onExitActionClick()
        self.onTrainModelActionClick()
    
    def onExitActionClick(self):
        self.main_window.exitAction.triggered.connect(self.main_window.quitWindow)

    def onTrainModelActionClick(self):
        self.main_window.trainModelAction.triggered.connect(self.main_window.showTrainingWindow)