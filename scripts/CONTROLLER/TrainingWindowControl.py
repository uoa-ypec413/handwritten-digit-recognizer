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

    def showTrainingWindow(self):
        self.training_window.show()

    def on_cancel_button_click(self):
        self.training_window.cancelButton.clicked.connect(self.digit_recogniser_controller.cancel_training)

    def on_download_button_click(self):    
        self.training_window.downloadButton.clicked.connect(self.digit_recogniser_controller.download_data)
        self.training_window.downloadButton.clicked.connect(self.training_window.enableTrainButton)
        self.training_window.downloadButton.clicked.connect(self.training_window.disableDownloadButton)
        self.training_window.downloadButton.clicked.connect(self.enable_dataset_viewer)
    
    def enable_dataset_viewer(self):
        self.digit_recogniser_controller.main_window_control.enableDatasetViewer()

    def on_progress_update(self, value):
        self.training_window.progressBar.setValue(value)    

    def on_train_button_click(self):
        self.training_window.trainButton.clicked.connect(self.digit_recogniser_controller.train)
        self.training_window.trainButton.clicked.connect(self.training_window.enableCancelButton)
        self.training_window.trainButton.clicked.connect(self.training_window.disableTrainButton)
    
    def on_training_complete(self):
        self.training_window.enableTrainButton()
        self.training_window.disableCancelButton()

    def update_console(self, message):
        self.training_window.appendConsole(message)

    def reset_progress(self):
        self.training_window.progressBar.setValue(0)