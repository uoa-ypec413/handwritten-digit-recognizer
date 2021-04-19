from AI.DigitRecogniser import *
from CONTROLLER.TrainingWindowControl import *
import threading

class DigitRecogniserController():
    def __init__(self):
        self.digit_recogniser = DigitRecogniser()

    def set_main_window_control(self, main_window_control):
        self.main_window_control = main_window_control
        self.training_window_control = self.main_window_control.training_window_control

    def download_data(self):
        self.training_window_control.update_console('Downloading train dataset...')
        thread_function = self.digit_recogniser.data.import_train_dataset
        download_thread = threading.Thread(target=thread_function, daemon=True)
        download_thread.start()
        #self.training_window_control.update_console('Downloading test dataset...')
        #self.digit_recogniser.data.import_test_dataset()
        #self.training_window_control.update_console('Finished downloading both datasets!')

    def train(self):
        self.digit_recogniser.data.load_dataset(self.digit_recogniser.batch_size)
        self.digit_recogniser.train_model()

