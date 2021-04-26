from GUI.viewerwindow import *
from CONTROLLER.ImageFrameController import *

class ViewerWindowController():
    def __init__(self, main_window, digit_recogniser_controller):
        self.testViewerWindow = main_window.testViewerWindow
        self.trainViewerWindow = main_window.trainViewerWindow

        self.testImageFrameController = ImageFrameController()
        self.trainImageFrameController = ImageFrameController()
        
        self.digit_recogniser_controller = digit_recogniser_controller

        self.testViewerWindow.scrollArea.setWidget(self.testImageFrameController.imageFrame)
        self.trainViewerWindow.scrollArea.setWidget(self.trainImageFrameController.imageFrame)

        self.testViewerWindow.pageComboBox.currentIndexChanged.connect(self.setTestPage)
        self.trainViewerWindow.pageComboBox.currentIndexChanged.connect(self.setTrainPage)

        self.testViewerWindow.okButton.clicked.connect(self.closeTestViewer)
        self.trainViewerWindow.okButton.clicked.connect(self.closeTrainViewer)
    
    def showTrainingViewerWindow(self):
        self.trainImageFrameController.load_dataset(self.digit_recogniser_controller.digit_recogniser.data.train_dataset)
        self.trainViewerWindow.show()
    
    def showTestingViewerWindow(self):
        self.testImageFrameController.load_dataset(self.digit_recogniser_controller.digit_recogniser.data.test_dataset)
        self.testViewerWindow.show()
    
    def setTestPage(self):
        self.testImageFrameController.updatePage(self.testViewerWindow.pageComboBox.currentIndex())
    
    def setTrainPage(self):
        self.trainImageFrameController.updatePage(self.trainViewerWindow.pageComboBox.currentIndex())

    def closeTestViewer(self):
        self.testViewerWindow.close()
    
    def closeTrainViewer(self):
        self.trainViewerWindow.close()