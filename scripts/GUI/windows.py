import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class Window(QWidget):

    def __init__(self):
        super().__init__()

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        centerPosition = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(centerPosition)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

class MainWindow(Window):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Handwritten Digit Recognizer")
        self.resize(1000, 800)
        self.center()
        self.show()

class TrainingWindow(Window):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog")
        self.resize(400, 400)
        self.center()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    trainingWindow = TrainingWindow()
    sys.exit(app.exec())


