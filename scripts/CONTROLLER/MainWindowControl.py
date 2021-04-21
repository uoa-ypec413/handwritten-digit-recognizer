from GUI.mainwindow import *
from CONTROLLER.CentralWidgetControl import *
from CONTROLLER.ViewerWindowController import *

class MainWindowControl():
    def __init__(self, app):
        self.mainWindow = MainWindow(app)
        self.centralWidgetController = CentralWidgetControl(self.mainWindow)
        self.viewerWindowController = ViewerWindowController()
        self.onExitActionClick()
        self.onTrainModelActionClick()
        self.onTrainingImagesActionClick()
        self.onTestingImagesActionClick()

    
    def onExitActionClick(self):
        self.mainWindow.exitAction.triggered.connect(self.mainWindow.quitWindow)

    def onTrainModelActionClick(self):
        self.mainWindow.trainModelAction.triggered.connect(self.mainWindow.showTrainingWindow)
    
    def onTrainingImagesActionClick(self):
        self.mainWindow.viewTrainingImagesAction.triggered.connect(self.viewerWindowController.showTrainingViewerWindow)
    
    def onTestingImagesActionClick(self):
        self.mainWindow.viewTestingImagesAction.triggered.connect(self.viewerWindowController.showTestingViewerWindow)