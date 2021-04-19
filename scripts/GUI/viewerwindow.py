from PyQt5.QtWidgets import *
from GUI.imageframe import *

class ViewerWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(1100, 800)
        self.center()
        self.addOkButton()
        self.addDigitSelect()
        self.addAllSelect()
        self.imageFrame = ImageFrame()
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(self.imageFrame)
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
