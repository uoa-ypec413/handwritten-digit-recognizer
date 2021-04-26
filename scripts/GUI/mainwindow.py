import sys
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QApplication
from CONTROLLER.ViewerWindowController import *
from GUI.trainingwindow import *
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Handwritten Digit Recognizer")
        self.resize(1000, 800)
        self.center()
        self.addMenuBar()
        self.setWindowIcon(QIcon('media\logo.png'))
        self.show()

    def quitWindow(self):
        self.app.quit()

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

    def addViewTrainingImagesAction(self):
        self.viewTrainingImagesAction = QAction('View Training Images', self)

    def addViewTestingImagesAction(self):
        self.viewTestingImagesAction = QAction('View Testing Images', self)

    def addMenuBar(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.setToolTipsVisible(True)

        self.newModelMenu = fileMenu.addMenu('New Model')
        self.basicNNAction = QAction('Basic NN', self)
        self.newModelMenu.addAction(self.basicNNAction)
        self.leNet5Action = QAction('LeNet-5', self)
        self.newModelMenu.addAction(self.leNet5Action)
        self.adjustedLeNet5Action = QAction('Adjusted LeNet-5', self)
        self.newModelMenu.addAction(self.adjustedLeNet5Action)
        
        self.loadModelAction = QAction('Load Model', self)
        self.loadModelAction.setToolTip('Loads an existing model')
        fileMenu.addAction(self.loadModelAction)

        self.saveModelAction = QAction('Save Model', self)
        fileMenu.addAction(self.saveModelAction)

        self.trainModelAction = QAction('Train Model', self)
        fileMenu.addAction(self.trainModelAction)

        self.exitAction = QAction('Quit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setToolTip('Quit application')
        fileMenu.addAction(self.exitAction)

        viewMenu = menubar.addMenu('&View')
        self.addViewTrainingImagesAction()
        self.addViewTestingImagesAction()
        viewMenu.addAction(self.viewTrainingImagesAction)
        viewMenu.addAction(self.viewTestingImagesAction)
        self.viewTestingImagesAction.setEnabled(False)
        self.viewTrainingImagesAction.setEnabled(False)

    def enableDataSetViewer(self):
        self.viewTestingImagesAction.setEnabled(True)
        self.viewTrainingImagesAction.setEnabled(True)
