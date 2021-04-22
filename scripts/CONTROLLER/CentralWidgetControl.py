from CONTROLLER.CanvasControl import *
from CONTROLLER.ProbabilityPlotControl import *
from GUI.centralwidget import *

class CentralWidgetControl():
    def __init__(self, mainWindow, digit_recogniser_controller):
        self.canvasController = canvasController()
        self.probabilityController = ProbabilityPlotControl()
        self.digit_recogniser_controller = digit_recogniser_controller

        self.mainWindow = mainWindow
        self.mainWindow.setCentralWidget(CentralWidget(self))

        self.on_recognise_button_click()
        
        #self.probabilityPlotControl = ProbabilityPlotControl()
    def setCentralWidget(self, centralWidget):
        self.centralWidget = centralWidget
    
    def openModel(self):
        file_name = QFileDialog.getOpenFileName(self.mainWindow, "Load Model",
                                       "models/",
                                       "Digit Recognizer Models (*.pt)")
        if file_name[0]:
            self.digit_recogniser_controller.load_model(file_name)

    def on_recognise_button_click(self):
        self.centralWidget.recogniseButton.clicked.connect(self.digit_recogniser_controller.recognise_digit)

    def set_predicted_digit(self, digit):
        self.centralWidget.setPredictedDigit(digit)