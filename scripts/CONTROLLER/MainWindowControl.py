from GUI.mainwindow import *

class MainWindowControl():
    def __init__(self, app):
        self.mainWindow = MainWindow(app)
        self.onExitActionClick()
        self.onTrainModelActionClick()
        self.onTrainingImagesActionClick()
        self.onTestingImagesActionClick()
    
    def onExitActionClick(self):
        self.mainWindow.exitAction.triggered.connect(self.mainWindow.quitWindow)

    def onTrainModelActionClick(self):
        self.mainWindow.trainModelAction.triggered.connect(self.mainWindow.showTrainingWindow)
    
    def onTrainingImagesActionClick(self):
        self.mainWindow.viewTrainingImagesAction.triggered.connect(self.mainWindow.showTrainingViewerWindow)
    
    def onTestingImagesActionClick(self):
        self.mainWindow.viewTestingImagesAction.triggered.connect(self.mainWindow.showTestingViewerWindow)