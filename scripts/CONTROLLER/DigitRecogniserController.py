from AI.DigitRecogniser import *
from CONTROLLER.TrainingWindowControl import *
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtCore import pyqtSignal

class DownloadWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, training_window_control, digit_recogniser):
        super().__init__()
        self.training_window_control = training_window_control
        self.digit_recogniser = digit_recogniser

    def run(self):
        self.progress.emit(5)
        self.training_window_control.update_console('Downloading train dataset...\n')
        self.digit_recogniser.data.import_train_dataset()
        self.progress.emit(85)
        self.training_window_control.update_console('Downloaded train dataset...\n')
        self.training_window_control.update_console('Downloading test dataset...\n')
        self.digit_recogniser.data.import_test_dataset()
        self.training_window_control.update_console('Downloaded test dataset...\n')
        self.progress.emit(100)
        self.finished.emit()

class DigitRecogniserController():
    def __init__(self):
        self.digit_recogniser = DigitRecogniser()

    def set_main_window_control(self, main_window_control):
        self.main_window_control = main_window_control
        self.training_window_control = self.main_window_control.training_window_control

    def download_data(self, signal):
        self.thread = QThread()
        self.worker = DownloadWorker(self.training_window_control, self.digit_recogniser)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.training_window_control.on_progress_update)
        
        self.thread.start()

    def train(self):
        self.digit_recogniser.data.load_dataset(self.digit_recogniser.batch_size)
        self.digit_recogniser.train_model()

