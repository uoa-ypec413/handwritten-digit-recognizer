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
        fname = QFileDialog.getOpenFileName(self.centralWidget, 'Open file', './trained_models') # create file dialog
        if fname[0]:
            f = open(fname[0], 'r')

    def on_recognise_button_click(self):
        self.centralWidget.recogniseButton.clicked.connect(self.digit_recogniser_controller.recognise_digit)