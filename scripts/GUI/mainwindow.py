import sys
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QApplication
from GUI.centralwidget import *
from GUI.viewerwindow import *
from GUI.trainingwindow import *

class MainWindow(QMainWindow):
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Handwritten Digit Recognizer")
        self.resize(1000, 800)
        self.center()
        self.trainingWindow = TrainingWindow()
        self.trainingViewerWindow = ViewerWindow("Training Image Viewer")
        self.testingViewerWindow = ViewerWindow("Testing Image Viewer")
        self.addMenuBar()
        self.setCentralWidget(CentralWidget())
        self.show()

    def quitWindow(self):
        self.app.quit()

    def showTrainingWindow(self):
        self.trainingWindow.show()
    
    def showTrainingViewerWindow(self):
        self.trainingViewerWindow.show()
    
    def showTestingViewerWindow(self):
        self.testingViewerWindow.show()

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

    def addExitAction(self):
        self.exitAction = QAction('Quit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Quit application')
    
    def addTrainModelAction(self):
        self.trainModelAction = QAction('Train Model', self)

    def addViewTrainingImagesAction(self):
        self.viewTrainingImagesAction = QAction('View Training Images', self)

    def addViewTestingImagesAction(self):
        self.viewTestingImagesAction = QAction('View Testing Images', self)

    def addMenuBar(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        self.addTrainModelAction()
        self.addExitAction()
        fileMenu.addAction(self.trainModelAction)
        fileMenu.addAction(self.exitAction)

        viewMenu = menubar.addMenu('&View')
        self.addViewTrainingImagesAction()
        self.addViewTestingImagesAction()
        viewMenu.addAction(self.viewTrainingImagesAction)
        viewMenu.addAction(self.viewTestingImagesAction)