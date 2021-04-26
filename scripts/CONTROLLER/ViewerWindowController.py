from GUI.viewerwindow import *
from GUI.imageframe import *

class ImageFrameController():
    def __init__(self):
        self.imageFrame = ImageFrame()
    
    def updatePage(self, page):
        self.imageFrame.setPage(page)
        self.load_dataset(self.dataset)
    
    def load_dataset(self, dataset):
        self.dataset = dataset
        #self.imageFrame.clearGrid()
        self.imageFrame.render_dataset(dataset)
        #self.imageFrame.addImages()

class ViewerWindowController():
    def __init__(self, digit_recogniser_controller):
        self.testImageFrameController = ImageFrameController()
        self.trainImageFrameController = ImageFrameController()
        
        self.digit_recogniser_controller = digit_recogniser_controller

        self.testViewerWindow = ViewerWindow(100, name = 'test')
        self.trainViewerWindow = ViewerWindow(600, name = 'train')

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