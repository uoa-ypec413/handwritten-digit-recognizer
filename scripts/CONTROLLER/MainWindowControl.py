from GUI.mainwindow import *
from CONTROLLER.TrainingWindowControl import *
from CONTROLLER.CentralWidgetControl import *
from CONTROLLER.ViewerWindowController import *

class MainWindowControl():

    def __init__(self, app, digit_recogniser_controller):
        self.main_window = MainWindow(app)
        self.training_window_control = TrainingWindowControl(self.main_window.trainingWindow, digit_recogniser_controller)

        self.centralWidgetController = CentralWidgetControl(self.main_window, digit_recogniser_controller)
        self.viewerWindowController = ViewerWindowController()
        
        self.onExitActionClick()
        self.onTrainModelActionClick()
        self.onTrainingImagesActionClick()
        self.onTestingImagesActionClick()
        
    def onExitActionClick(self):
        self.main_window.exitAction.triggered.connect(self.main_window.quitWindow)

    def onTrainModelActionClick(self):
        self.main_window.trainModelAction.triggered.connect(self.main_window.showTrainingWindow)
    
    def onTrainingImagesActionClick(self):
      self.main_window.viewTrainingImagesAction.triggered.connect(self.viewerWindowController.showTrainingViewerWindow)
     
    def onTestingImagesActionClick(self):
      self.main_window.viewTestingImagesAction.triggered.connect(self.viewerWindowController.showTestingViewerWindow)