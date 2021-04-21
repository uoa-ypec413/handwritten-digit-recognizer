from AI.DigitRecogniser import *
from CONTROLLER.TrainingWindowControl import *
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtCore import pyqtSignal

class DownloadWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    status = pyqtSignal(str)

    def __init__(self, digit_recogniser):
        super().__init__()
        self.digit_recogniser = digit_recogniser

    def run(self):
        self.progress.emit(5)
        self.status.emit('Downloading train dataset...\n')
        self.digit_recogniser.data.import_train_dataset()

        self.progress.emit(85)
        self.status.emit('Downloading test dataset...\n')

        self.digit_recogniser.data.import_test_dataset()

        self.status.emit('Downloaded both datasets!\n')
        self.progress.emit(100)

        self.finished.emit()

class TrainWorker(QObject):
    finished = pyqtSignal()
    status = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self, digit_recogniser):
        super().__init__()
        self.digit_recogniser = digit_recogniser
        self.digit_recogniser.progress_signal.connect(self.update_progress)
        self.digit_recogniser.status_signal.connect(self.update_status)

    def run(self):
        self.status.emit('Beginning Training...\n')
        self.digit_recogniser.data.load_dataset(self.digit_recogniser.batch_size)
        self.digit_recogniser.train_model()
        self.finished.emit()
    
    def update_progress(self, integer):
        self.progress.emit(integer)
    
    def update_status(self, string):
        self.status.emit(string)

class DigitRecogniserController():
    def __init__(self):
        self.digit_recogniser = DigitRecogniser()

    def set_main_window_control(self, main_window_control):
        self.main_window_control = main_window_control
        self.training_window_control = self.main_window_control.training_window_control

    def download_data(self, signal):
        self.download_thread = QThread()
        self.download_worker = DownloadWorker(self.digit_recogniser)
        self.download_worker.moveToThread(self.download_thread)

        self.download_thread.started.connect(self.download_worker.run)
        self.download_worker.finished.connect(self.download_thread.quit)
        self.download_worker.finished.connect(self.download_worker.deleteLater)
        self.download_thread.finished.connect(self.download_thread.deleteLater)
        self.download_worker.progress.connect(self.training_window_control.on_progress_update)
        self.download_worker.status.connect(self.training_window_control.update_console)
        
        self.download_thread.start()

    def train(self):
        self.train_thread = QThread()
        self.train_worker = TrainWorker(self.digit_recogniser)
        self.train_worker.moveToThread(self.train_thread)

        self.train_worker.status.connect(self.training_window_control.update_console)
        self.train_thread.started.connect(self.training_window_control.reset_progress)
        self.train_worker.progress.connect(self.training_window_control.on_progress_update)

        self.train_thread.started.connect(self.train_worker.run)

        self.train_worker.finished.connect(self.train_thread.quit)
        self.train_thread.finished.connect(self.train_thread.deleteLater)
        self.train_worker.finished.connect(self.train_worker.deleteLater)

        self.train_thread.start()

    def cancel_training(self):
        if self.train_thread.isRunning:
            self.digit_recogniser.cancel_train_model()

    def recognise_digit(self):
        probabilities = self.digit_recogniser.recognise_user_digit()
        probabilities = probabilities.detach().numpy()
        max_digit = numpy.where(probabilities == numpy.amax(probabilities))
        self.main_window_control.centralWidgetController.probabilityController.setProbability(probabilities * 100)
        self.main_window_control.centralWidgetController.set_predicted_digit(str(max_digit[0][0]))


