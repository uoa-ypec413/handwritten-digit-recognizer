from GUI.MainWindow import *
from CONTROLLER.TrainingWindowControl import *
from CONTROLLER.CentralWidgetControl import *
from CONTROLLER.ViewerWindowController import *

class MainWindowControl():

    def __init__(self, app, digit_recogniser_controller):
        self.main_window = MainWindow(app)
        self.digit_recogniser_controller = digit_recogniser_controller
        self.training_window_control = TrainingWindowControl(digit_recogniser_controller)
        self.centralWidgetController = CentralWidgetControl(self.main_window, digit_recogniser_controller)
        self.viewerWindowController = ViewerWindowController(digit_recogniser_controller)        
        self.onExitActionClick()
        self.onTrainModelActionClick()
        self.onTrainingImagesActionClick()
        self.onTestingImagesActionClick()
        self.onBasicNNActionClick()
        self.onleNet5ActionClick()
        self.onadjustedLeNet5ActionClick()
        self.onLoadModelActionClick()
        self.onSaveModelActionClick()
        
    def onExitActionClick(self):
        self.main_window.exitAction.triggered.connect(self.main_window.quitWindow)

    def onTrainModelActionClick(self):
        self.main_window.trainModelAction.triggered.connect(self.training_window_control.showTrainingWindow)
    
    def onTrainingImagesActionClick(self):
      self.main_window.viewTrainingImagesAction.triggered.connect(self.viewerWindowController.showTrainingViewerWindow)
     
    def onTestingImagesActionClick(self):
      self.main_window.viewTestingImagesAction.triggered.connect(self.viewerWindowController.showTestingViewerWindow)

    def onBasicNNActionClick(self):
        self.main_window.basicNNAction.triggered.connect(self.digit_recogniser_controller.set_basic_model)
    
    def onleNet5ActionClick(self):
        self.main_window.leNet5Action.triggered.connect(self.digit_recogniser_controller.set_LN5_model)
    
    def onadjustedLeNet5ActionClick(self):
        self.main_window.adjustedLeNet5Action.triggered.connect(self.digit_recogniser_controller.set_ALN5_model)
    
    def onLoadModelActionClick(self):
        self.main_window.loadModelAction.triggered.connect(self.load_model)

    def onSaveModelActionClick(self):
        self.main_window.saveModelAction.triggered.connect(self.save_model)
    
    def enableDatasetViewer(self):
        self.main_window.enableDataSetViewer()
    
    def load_model(self):
        file_name = QFileDialog.getOpenFileName(self.main_window, "Load Model",
                                       "models/",
                                       "Digit Recognizer Models (*.pt)")
        if file_name[0]:
            self.digit_recogniser_controller.load_model(file_name)
    
    def save_model(self):
        file_name = QFileDialog.getSaveFileName(self.main_window, "Save Model",
                                       "models/new_model.pt",
                                       "Digit Recognizer Models (*.pt)")
        if file_name[0]:
            self.digit_recogniser_controller.save_model(file_name)