# This is the window that allows the user to view either the training or testing dataset

from PyQt5.QtWidgets import *
from GUI.ImageFrame import *
import numpy
from PyQt5.QtGui import QIcon

class ViewerWindow(QWidget):

    # Take the number of pages and the name of the window.
    # Initialise the viewer window to display the correct number of pages and window name.
    def __init__(self, pages, name: str):
        super().__init__()
        self.name = name

        if self.name == 'train':
            self.setWindowTitle('Training Dataset Viewer')
        elif self.name == 'test':
            self.setWindowTitle('Testing Dataset Viewer')

        self.setWindowIcon(QIcon('media\logo.png'))
        
        self.display(pages)

    # Center the window in the user's display
    def center(self):
        window_geometry = self.frameGeometry() # get window geometry
        center_position = QDesktopWidget().availableGeometry().center() # get monitor center position
        window_geometry.moveCenter(center_position)
        self.move(window_geometry.topLeft()) # move window to monitor centre position

    def add_ok_button(self):
        self.ok_button = QPushButton('Ok')

    def set_ok_button_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.ok_button)
        return hbox

    def add_page_select(self, pages):
        self.page_select_label = QLabel('Page:')
        self.page_combobox = QComboBox(self)
        # Create a list of every whole number between 1 and pages + 1.
        # This is the human-readable list of possible pages for the user to select from.
        pages = numpy.arange(1, pages + 1)
        # Add each page number as an item in the page select combobox
        for page in pages:
            self.page_combobox.addItem(str(page))

    def add_digit_select(self):
        self.digit_select_label = QLabel('Digit:')
        self.digit_combobox = QComboBox(self)
        # Generate a list of whole numbers from 0 to 9, which acts as the list of digit classes
        digits = numpy.arange(10)
        # Add each digit to the digit selection combobox
        for digit in digits:
            self.digit_combobox.addItem(str(digit))
    
    def set_page_select_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.page_select_label)
        hbox.addWidget(self.page_combobox)
        return hbox

    def set_digit_select_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.digit_select_label)
        hbox.addWidget(self.digit_combo_box)
        return hbox

    def add_all_select(self):
        self.all_select_label = QLabel('All')
        self.all_select_checkbox = QCheckBox()

    def set_all_select_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.all_select_label)
        hbox.addWidget(self.all_select_checkbox)
        return hbox

    def set_button_layout(self):
        vbox = QVBoxLayout()
        vbox.addLayout(self.set_page_select_layout())
        vbox.addStretch(1)
        vbox.addLayout(self.set_ok_button_layout())
        return vbox

    def set_box_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.scroll_area)
        hbox.addLayout(self.set_button_layout())

        self.setLayout(hbox)

    def display(self, pages):
        self.resize(1100, 800)
        self.center()
        self.add_ok_button()
        self.add_page_select(pages)
        self.scroll_area = QScrollArea() # Create a scrollable area to contain the images in the dataset
        self.set_box_layout()
