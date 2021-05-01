# Controllers for the digit recogniser model module.

from AI.DigitRecogniser import *
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtCore import pyqtSignal
import numpy

# QObject that runs functions inside of a QThread,
# Downloads the MNIST database, ensuring that the GUI does not hang.
class DownloadWorker(QObject):
    finished = pyqtSignal() # Signals that download is finished
    progress = pyqtSignal(int) # Signals progress %
    status = pyqtSignal(str) # Signals progress string

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

# QObject that runs functions inside of a QThread,
# Trains the model, ensuring that the GUI does not hang.
class TrainWorker(QObject):
    finished = pyqtSignal() # Signals that download is finished
    progress = pyqtSignal(int) # Signals progress %
    status = pyqtSignal(str) # Signals progress string

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

    def set_main_window_controller(self, main_window_controller):
        self.main_window_controller = main_window_controller
        self.training_window_controller = self.main_window_controller.training_window_controller

    def download_data(self, signal):
        self.download_thread = QThread() # Start a QThread
        self.download_worker = DownloadWorker(self.digit_recogniser) # Initialise worker object
        self.download_worker.moveToThread(self.download_thread) # Move worker to the thread

        self.download_thread.started.connect(self.download_worker.run) # When the thread is started, run the worker
        self.download_worker.finished.connect(self.download_thread.quit) # When the worker is finished, close the thread
        self.download_worker.finished.connect(self.download_worker.deleteLater) # When the worker is finished, delete the worker
        self.download_thread.finished.connect(self.download_thread.deleteLater) # When the thread is finished, delete the thread
        self.download_worker.progress.connect(self.training_window_controller.on_progress_update) # Pass progress to training window controller
        self.download_worker.status.connect(self.training_window_controller.update_console) # Pass progress to training window controller
        
        self.download_thread.start() # Start the thread

    def train(self):
        self.train_thread = QThread() # Start a QThread
        self.train_worker = TrainWorker(self.digit_recogniser) # Initialise worker object
        self.train_worker.moveToThread(self.train_thread) # Move worker to the thread

        self.train_worker.status.connect(self.training_window_controller.update_console) # Pass progress to training window controller
        self.train_thread.started.connect(self.training_window_controller.reset_progress) # Pass progress to training window controller
        self.train_worker.progress.connect(self.training_window_controller.on_progress_update) # Pass progress to training window controller

        self.train_thread.started.connect(self.train_worker.run) # When the thread is started, run the worker

        self.train_worker.finished.connect(self.train_thread.quit) # When the worker is finished, close the thread
        self.train_thread.finished.connect(self.train_thread.deleteLater) # When the worker is finished, delete the thread
        self.train_worker.finished.connect(self.train_worker.deleteLater) # When the worker is finished, delete the worker
        self.train_thread.finished.connect(self.training_window_controller.on_training_complete) # Training window controller function call

        self.train_thread.start() # Start the thread

    def cancel_training(self):
        if self.train_thread.isRunning:
            self.digit_recogniser.cancel_train_model()

    # Recognise the current user digit, pass probabilities and predicted digit to the main window controller.
    def recognise_digit(self):
        probabilities = self.digit_recogniser.recognise_user_digit()
        probabilities = probabilities.detach().numpy()
        max_digit = numpy.where(probabilities == numpy.amax(probabilities))
        self.main_window_controller.central_widget_controller.probability_controller.set_probability(probabilities * 100)
        self.main_window_controller.central_widget_controller.set_predicted_digit(str(max_digit[0][0]))
    
    # Set the model to a new basic NN model
    def set_basic_model(self):
        self.digit_recogniser.create_model(BasicNN)
    
    # Set the model to a new LeNet-5 model
    def set_LN5_model(self):
        self.digit_recogniser.create_model(LeNet5)
    
    # Set the model to a new Adjusted LeNet-5 model
    def set_ALN5_model(self):
        self.digit_recogniser.create_model(AdjustedLeNet5)
    
    # Load a model given a path
    def load_model(self, file_name):
        self.digit_recogniser.load_model(file_name)

    # Save the model given a path
    def save_model(self, file_name):
        self.digit_recogniser.save_model(file_name)

