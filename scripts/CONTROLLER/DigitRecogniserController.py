from AI.DigitRecogniser import *

class DigitRecogniserController():
    def __init__(self):
        self.digit_recogniser = DigitRecogniser()

    def download_data(self):
        self.digit_recogniser.data.import_dataset()
