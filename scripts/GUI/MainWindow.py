# This is the main window for the program

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
        window_geometry = self.frameGeometry() # get window geometry
        center_position = QDesktopWidget().availableGeometry().center() # get monitor center position
        window_geometry.moveCenter(center_position)
        self.move(window_geometry.topLeft()) # move window to monitor centre position

    def add_menu_bar(self):
        self.menubar = self.menuBar()

        # Set up the file sub-menu
        self.file_menu = self.menubar.addMenu('&File')
        self.file_menu.setToolTipsVisible(True)

        # Option to create a new model under file submenu
        self.new_model_menu = self.file_menu.addMenu('New Model')
        self.basic_nn_action = QAction('Basic NN', self)
        self.new_model_menu.addAction(self.basic_nn_action)
        self.lenet5_action = QAction('LeNet-5', self)
        self.new_model_menu.addAction(self.lenet5_action)
        self.adjusted_lenet5_action = QAction('Adjusted LeNet-5', self)
        self.new_model_menu.addAction(self.adjusted_lenet5_action)
        
        # Option to load an existing model under file submenu
        self.load_model_action = QAction('Load Model', self)
        self.load_model_action.setToolTip('Loads an existing model')
        self.file_menu.addAction(self.load_model_action)

        # Option to save the current model under file submenu
        self.save_model_action = QAction('Save Model', self)
        self.file_menu.addAction(self.save_model_action)

        # Option to train the current model under file submenu
        self.train_model_action = QAction('Train Model', self)
        self.file_menu.addAction(self.train_model_action)

        # Option to close the program under file submenu
        self.exit_action = QAction('Quit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setToolTip('Quit application')
        self.file_menu.addAction(self.exit_action)

        # View menu setup, with options to view each dataset
        self.view_menu = self.menubar.addMenu('&View')
        self.view_training_images_action = QAction('View Training Images', self)
        self.view_testing_images_action = QAction('View Testing Images', self)
        self.view_menu.addAction(self.view_training_images_action)
        self.view_menu.addAction(self.view_testing_images_action)
        self.view_training_images_action.setEnabled(False)
        self.view_testing_images_action.setEnabled(False)

    # Initially the dataset viewer buttons in the menu are disabled.
    # Once the MNIST database has been downloaded this function is called
    # to enable them.
    def enable_dataset_viewer(self):
        self.view_testing_images_action.setEnabled(True)
        self.view_training_images_action.setEnabled(True)
