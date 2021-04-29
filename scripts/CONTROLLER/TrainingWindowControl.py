from GUI.MainWindow import *
from GUI.TrainingWindow import *
from CONTROLLER.DigitRecogniserController import *

class TrainingWindowControl():
    def __init__(self, digit_recogniser_controller):
        self.digit_recogniser_controller = digit_recogniser_controller
        self.training_window = TrainingWindow()
        self.on_cancel_button_click()
        self.on_download_button_click()
        self.on_train_button_click()

    def show_training_window(self):
        self.training_window.show()

    def on_cancel_button_click(self):
        self.training_window.cancel_button.clicked.connect(self.digit_recogniser_controller.cancel_training)

    def on_download_button_click(self):    
        self.training_window.download_button.clicked.connect(self.digit_recogniser_controller.download_data)
        self.training_window.download_button.clicked.connect(self.training_window.enable_train_button)
        self.training_window.download_button.clicked.connect(self.training_window.disable_download_button)
        self.training_window.download_button.clicked.connect(self.enable_dataset_viewer)
    
    def enable_dataset_viewer(self):
        self.digit_recogniser_controller.main_window_control.enable_dataset_viewer()

    def on_progress_update(self, value):
        self.training_window.progress_bar.setValue(value)    

    def on_train_button_click(self):
        self.training_window.train_button.clicked.connect(self.digit_recogniser_controller.train)
        self.training_window.train_button.clicked.connect(self.training_window.enable_cancel_button)
        self.training_window.train_button.clicked.connect(self.training_window.disable_train_button)
    
    def on_training_complete(self):
        self.training_window.enable_train_button()
        self.training_window.disable_cancel_button()

    def update_console(self, message):
        self.training_window.append_console(message)

    def reset_progress(self):
        self.training_window.progress_bar.setValue(0)