from GUI.mainwindow import *
from CONTROLLER.TrainingWindowControl import *
from CONTROLLER.CentralWidgetControl import *

class MainWindowControl():
    def __init__(self, app, digit_recogniser_controller):
        self.main_window = MainWindow(app)
        self.training_window_control = TrainingWindowControl(self.main_window.trainingWindow, digit_recogniser_controller)
        self.centralWidgetController = CentralWidgetControl(self.mainWindow)
        self.onExitActionClick()
        self.onTrainModelActionClick()
        self.onTrainingImagesActionClick()
        self.onTestingImagesActionClick()
    def onExitActionClick(self):
        self.main_window.exitAction.triggered.connect(self.main_window.quitWindow)

    def onTrainModelActionClick(self):
        self.mainWindow.trainModelAction.triggered.connect(self.mainWindow.showTrainingWindow)
    
    def onTrainingImagesActionClick(self):
        self.mainWindow.viewTrainingImagesAction.triggered.connect(self.mainWindow.showTrainingViewerWindow)
    
    def onTestingImagesActionClick(self):
        self.mainWindow.viewTestingImagesAction.triggered.connect(self.mainWindow.showTestingViewerWindow)