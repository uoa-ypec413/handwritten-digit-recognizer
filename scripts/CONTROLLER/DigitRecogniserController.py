from AI.DigitRecogniser import *

class DigitRecogniserController():
    def __init__(self):
        self.digit_recogniser = DigitRecogniser()

    def download_data(self):
        self.digit_recogniser.data.import_dataset()

    def train(self):
        self.digit_recogniser.data.load_dataset(self.digit_recogniser.batch_size)
        self.digit_recogniser.train_model()
