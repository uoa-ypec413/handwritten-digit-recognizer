import sys
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Handwritten Digit Recognizer")
        self.resize(1000, 800)
        self.center()
        self.add_menu_bar()
        self.setWindowIcon(QIcon('media\logo.png'))
        self.show()

    def quit_window(self):
        self.app.quit()

    def center(self):
        qRectangle = self.frameGeometry() # get window geometry
        center_position = QDesktopWidget().availableGeometry().center() # get monitor center position
        qRectangle.moveCenter(center_position)
        self.move(qRectangle.topLeft()) # move window to monitor centre position

    def add_menu_bar(self):
        self.menubar = self.menuBar()

        self.file_menu = self.menubar.addMenu('&File')
        self.file_menu.setToolTipsVisible(True)

        self.new_model_menu = self.file_menu.addMenu('New Model')
        self.basic_nn_action = QAction('Basic NN', self)
        self.new_model_menu.addAction(self.basic_nn_action)
        self.lenet5_action = QAction('LeNet-5', self)
        self.new_model_menu.addAction(self.lenet5_action)
        self.adjusted_lenet5_action = QAction('Adjusted LeNet-5', self)
        self.new_model_menu.addAction(self.adjusted_lenet5_action)
        
        self.load_model_action = QAction('Load Model', self)
        self.load_model_action.setToolTip('Loads an existing model')
        self.file_menu.addAction(self.load_model_action)

        self.save_model_action = QAction('Save Model', self)
        self.file_menu.addAction(self.save_model_action)

        self.train_model_action = QAction('Train Model', self)
        self.file_menu.addAction(self.train_model_action)

        self.exit_action = QAction('Quit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setToolTip('Quit application')
        self.file_menu.addAction(self.exit_action)

        self.view_menu = self.menubar.addMenu('&View')
        self.view_training_images_action = QAction('View Training Images', self)
        self.view_testing_images_action = QAction('View Testing Images', self)
        self.view_menu.addAction(self.view_training_images_action)
        self.view_menu.addAction(self.view_testing_images_action)
        self.view_training_images_action.setEnabled(False)
        self.view_testing_images_action.setEnabled(False)

    def enable_dataset_viewer(self):
        self.view_testing_images_action.setEnabled(True)
        self.view_training_images_action.setEnabled(True)
