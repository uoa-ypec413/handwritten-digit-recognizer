from GUI.centralwidget import *
from GUI.canvas import *
from GUI.probabilityplot import *

class ProbabilityPlotControl():
    def __init__(self):
        self.plot = probabilityPlot()
    
    def setProbability(self, probabilities):
        self.plot.setProbability(probabilities)

class CanvasController():
    def __init__(self):

        self.canvas = Canvas(self)
        self.lastPos = None

    def onMouseMove(self, position):
        if self.lastPos is None: # On the first mouse event, do not paint, just save position
            self.lastPos = position
        else:
            currentPos = position
            self.canvas.drawLine(self.lastPos, currentPos)
            self.lastPos = currentPos
    
    def onMouseRelease(self):
        self.lastPos = None
        self.saveDrawing()
    
    def clear(self):
        self.canvas.clear()

    def saveDrawing(self):

            drawing = self.canvas.pixmap()
            drawing.save('user_data/digit_drawing.jpg', "JPEG" )

class CentralWidgetControl():
    def __init__(self, mainWindow, digit_recogniser_controller):
        self.canvasController = CanvasController()
        self.probabilityController = ProbabilityPlotControl()
        self.digit_recogniser_controller = digit_recogniser_controller

        self.mainWindow = mainWindow
        self.centralWidget = CentralWidget(self)
        self.mainWindow.setCentralWidget(self.centralWidget)

        self.on_clear_button_click()
        self.on_model_button_click()
        self.on_recognise_button_click()

    def on_clear_button_click(self):
        self.centralWidget.clearButton.clicked.connect(self.canvasController.clear)

    def on_model_button_click(self):
        self.centralWidget.modelButton.clicked.connect(self.openModel)

    
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