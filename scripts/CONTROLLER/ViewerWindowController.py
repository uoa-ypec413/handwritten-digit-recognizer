from GUI.viewerwindow import *
from CONTROLLER.ImageFrameController import *

class ViewerWindowController():
    def __init__(self):
        self.testImageFrameController = ImageFrameController()
        self.trainImageFrameController = ImageFrameController()

        self.testViewerWindow = ViewerWindow(name = 'test')
        self.trainViewerWindow = ViewerWindow(name = 'train')

        self.testViewerWindow.scrollArea.setWidget(self.testImageFrameController.imageFrame)
        self.trainViewerWindow.scrollArea.setWidget(self.trainImageFrameController.imageFrame)

        self.testViewerWindow.pageComboBox.currentIndexChanged.connect(self.setTestPage)
        self.trainViewerWindow.pageComboBox.currentIndexChanged.connect(self.setTrainPage)

        self.testViewerWindow.okButton.clicked.connect(self.closeTestViewer)
        self.trainViewerWindow.okButton.clicked.connect(self.closeTrainViewer)
    
    def showTrainingViewerWindow(self):
        self.trainViewerWindow.show()
    
    def showTestingViewerWindow(self):
        self.testViewerWindow.show()
    
    def setTestPage(self):
        self.testImageFrameController.updatePage(self.testViewerWindow.pageComboBox.currentIndex())
    
    def setTrainPage(self):
        self.trainImageFrameController.updatePage(self.trainViewerWindow.pageComboBox.currentIndex())

    def closeTestViewer(self):
        self.testViewerWindow.close()
    
    def closeTrainViewer(self):
        self.trainViewerWindow.close()