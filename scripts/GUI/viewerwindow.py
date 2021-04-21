from PyQt5.QtWidgets import *
from GUI.imageframe import *
import numpy

class ViewerWindow(QWidget):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

        if self.name == 'train':
            self.setWindowTitle('Training Dataset Viewer')
        elif self.name == 'test':
            self.setWindowTitle('Testing Dataset Viewer')
        
        self.display()
        

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

    def addOkButton(self):
        self.okButton = QPushButton('Ok')

    def setOkButtonLayout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        
        return hbox

    def addPageSelect(self):
        self.pageSelectLabel = QLabel('Page:')
        self.pageComboBox = QComboBox(self)
        pages = numpy.arange(60)
        for page in pages:
            self.pageComboBox.addItem(str(page))

    def addDigitSelect(self):
        self.digitSelectLabel = QLabel('Digit:')
        self.digitComboBox = QComboBox(self)
        digits = numpy.arange(10)
        for digit in digits:
            self.digitComboBox.addItem(str(digit))
    
    def setPageSelectLayout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.pageSelectLabel)
        hbox.addWidget(self.pageComboBox)
        
        return hbox

    def setDigitSelectLayout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.digitSelectLabel)
        hbox.addWidget(self.digitComboBox)
        
        return hbox

    def addAllSelect(self):
        self.allSelectLabel = QLabel('All')
        self.allSelectCheckBox = QCheckBox()

    def setAllSelectLayout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.allSelectLabel)
        hbox.addWidget(self.allSelectCheckBox)
        
        return hbox

    def setButtonLayout(self):
        vbox = QVBoxLayout()
        vbox.addLayout(self.setPageSelectLayout())
        vbox.addLayout(self.setDigitSelectLayout())
        vbox.addLayout(self.setAllSelectLayout())
        vbox.addStretch(1)
        vbox.addLayout(self.setOkButtonLayout())

        return vbox

    def setBoxLayout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.scrollArea)
        hbox.addLayout(self.setButtonLayout())

        self.setLayout(hbox)

    def display(self):
        self.resize(1100, 800)
        self.center()
        self.addOkButton()
        self.addAllSelect()
        self.addPageSelect()
        self.addDigitSelect()
        self.scrollArea = QScrollArea()
        self.setBoxLayout()
