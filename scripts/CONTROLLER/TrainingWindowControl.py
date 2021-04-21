from GUI.mainwindow import *
from GUI.trainingwindow import *
from CONTROLLER.DigitRecogniserController import *

class TrainingWindowControl():
    def __init__(self, training_window, digit_recogniser_controller):
        self.digit_recogniser_controller = digit_recogniser_controller
        self.training_window = training_window
        self.on_cancel_button_click()
        self.on_download_button_click()
        self.on_train_button_click()

    def on_cancel_button_click(self):
        self.training_window.cancelButton.clicked.connect(self.digit_recogniser_controller.cancel_training)

    def on_download_button_click(self):    
        self.training_window.downloadButton.clicked.connect(self.digit_recogniser_controller.download_data)

    def on_progress_update(self, value):
        self.training_window.progressBar.setValue(value)    

    def on_train_button_click(self):
        self.training_window.trainButton.clicked.connect(self.digit_recogniser_controller.train)

    def update_console(self, message):
        self.training_window.appendConsole(message)

    def reset_progress(self):
        self.training_window.progressBar.setValue(0)