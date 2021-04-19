from GUI.mainwindow import *
from GUI.trainingwindow import *
from CONTROLLER.DigitRecogniserController import *

class TrainingWindowControl():
    def __init__(self, training_window, digit_recogniser_controller):
        self.digit_recogniser_controller = digit_recogniser_controller
        self.training_window = training_window
        self.on_cancel_button_click()
        self.on_download_button_click()

    def on_cancel_button_click(self):
        self.training_window.cancelButton.clicked.connect(self.training_window.close)

    def on_download_button_click(self):
        self.training_window.downloadButton.clicked.connect(self.digit_recogniser_controller.download_data)