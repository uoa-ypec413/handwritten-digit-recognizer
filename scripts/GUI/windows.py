import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QAction, QPushButton, QHBoxLayout, QVBoxLayout, QTextBrowser, QProgressBar, QLabel, QComboBox, QCheckBox, QGridLayout, QFrame
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from torch import tensor
import numpy

class TrainingWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog")
        self.resize(400, 400)
        self.center()
        self.addConsole()
        self.addProgressBar()
        self.addButtons()
        self.setBoxLayout()

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

    def onCancelButtonClick(self):
        self.close()

    def addButtons(self):
        self.downloadButton = QPushButton('Download MNIST')
        self.trainButton = QPushButton('Train')
        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.onCancelButtonClick)

    def addProgressBar(self):
        self.progressBar = QProgressBar()
    
    def addConsole(self):
        self.console = QTextBrowser()

    def setButtonLayout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.downloadButton)
        hbox.addWidget(self.trainButton)
        hbox.addWidget(self.cancelButton)
        hbox.addStretch(1)

        return hbox

    def setProgressBarLayout(self):
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)

    def setBoxLayout(self):
        self.setProgressBarLayout()
    
        vbox = QVBoxLayout()
        vbox.addWidget(self.console)
        vbox.addWidget(self.progressBar)
        vbox.addLayout(self.setButtonLayout())

        self.setLayout(vbox)

class ImageFrame(QFrame):

    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.Box)
        self.imageGrid = QGridLayout()
        self.addImages()
        self.setLayout(self.imageGrid)
    
    def addImages(self):
        imageArray = []
        image = QPixmap(28, 28)
        image.fill(QtCore.Qt.black)

        for i in range(0,16):
            label = QLabel()
            label.setPixmap(image)
            imageArray.append(label)

        row = 0
        column = 0
        for images in imageArray:
            
            self.imageGrid.addWidget(images, row, column)

            if column == 3:
                row += 1
                column = 0
            else:
                column += 1

class ViewerWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(400, 400)
        self.center()
        self.addOkButton()
        self.addDigitSelect()
        self.addAllSelect()
        self.imageFrame = ImageFrame()
        self.setBoxLayout()

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position
    
    def onOkButtonClick(self):
        self.close()

    def addOkButton(self):
        self.okButton = QPushButton('Ok')
        self.okButton.clicked.connect(self.onOkButtonClick)

    def setOkButtonLayout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        
        return hbox

    def addDigitSelect(self):
        self.digitSelectLabel = QLabel('Digit:')
        self.digitComboBox = QComboBox(self)
        self.digitComboBox.addItem('0')
        self.digitComboBox.addItem('1')
        self.digitComboBox.addItem('2')
        self.digitComboBox.addItem('3')
        self.digitComboBox.addItem('4')
        self.digitComboBox.addItem('5')
        self.digitComboBox.addItem('6')
        self.digitComboBox.addItem('7')
        self.digitComboBox.addItem('8')
        self.digitComboBox.addItem('9')
    
    def setDigitSelectLayout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.digitSelectLabel)
        hbox.addWidget(self.digitComboBox)
        
        return hbox

    def addAllSelect(self):
        self.allSelectLabel = QLabel('All')
        self.allSelectCheckBox = QCheckBox()

    def setAllSelectLayout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.allSelectLabel)
        hbox.addWidget(self.allSelectCheckBox)
        
        return hbox

    def setButtonLayout(self):
        vbox = QVBoxLayout()
        vbox.addLayout(self.setDigitSelectLayout())
        vbox.addLayout(self.setAllSelectLayout())
        vbox.addStretch(1)
        vbox.addLayout(self.setOkButtonLayout())

        return vbox

    def setBoxLayout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.imageFrame)
        hbox.addLayout(self.setButtonLayout())

        self.setLayout(hbox)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Handwritten Digit Recognizer")
        self.resize(1000, 800)
        self.center()
        self.trainingWindow = TrainingWindow()
        self.viewerWindow = ViewerWindow()
        self.addMenuBar()
        self.show()

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

    def addExitAction(self):
        self.exitAction = QAction('Quit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Quit application')
        self.exitAction.triggered.connect(app.quit)
    
    def addTrainModelAction(self):
        self.trainModelAction = QAction('Train Model', self)
        self.trainModelAction.triggered.connect(self.trainingWindow.show)

    def addViewTrainingImagesAction(self):
        self.viewTrainingImagesAction = QAction('View Training Images', self)
        self.viewTrainingImagesAction.triggered.connect(self.viewerWindow.show)

    def addViewTestingImagesAction(self):
        self.viewTestingImagesAction = QAction('View Testing Images', self)
        self.viewTestingImagesAction.triggered.connect(self.viewerWindow.show)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())


