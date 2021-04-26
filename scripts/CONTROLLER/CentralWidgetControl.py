# This is the controller for the central widget, displayed in the main window.
# It includes controllers for the probability plot and the drawing canvas as well.

from GUI.probabilityplot import *
from GUI.centralwidget import *
from GUI.canvas import *

class ProbabilityPlotControl():
    def __init__(self):
        self.plot = probabilityPlot() # Create an instance of a probability polot
    
    def setProbability(self, probabilities):
        self.plot.setProbability(probabilities)

class canvasController():
    def __init__(self):

        self.canvas = Canvas(self) # Create an canvas instance
        self.lastPos = None # Set the last mouse position to be none

    def onMouseMove(self, position):
        if self.lastPos is None: # On the first mouse event, do not paint, just save position
            self.lastPos = position
        else: # On concurrent mouse events save the current position and draw a line from the last position
            currentPos = position
            self.canvas.drawLine(self.lastPos, currentPos)
            self.lastPos = currentPos
    
    def onMouseRelease(self): # When the user is done drawing set the last position as none and save the drawing
        self.lastPos = None
        self.saveDrawing()
    
    def clear(self):
        self.canvas.clear()

    def saveDrawing(self):
            drawing = self.canvas.pixmap()
            drawing.save('user_data/digit_drawing.jpg', "JPEG" )

class CentralWidgetControl(): # Control module for the central widget
    def __init__(self, mainWindow, digit_recogniser_controller):
        self.canvasController = canvasController()
        self.probabilityController = ProbabilityPlotControl()
        self.digit_recogniser_controller = digit_recogniser_controller

        self.mainWindow = mainWindow
        self.mainWindow.setCentralWidget(CentralWidget(self))

        self.on_recognise_button_click() # Connect the signal from the recognise button to the appropriate slot in
                                         # digit recogniser controller.
        
    def setCentralWidget(self, centralWidget):
        self.centralWidget = centralWidget
    
    def openModel(self):
        file_name = QFileDialog.getOpenFileName(self.mainWindow, "Load Model",
                                       "models/",
                                       "Digit Recognizer Models (*.pt)")
        if file_name[0]:
            self.digit_recogniser_controller.load_model(file_name)

    # Connect the signal from the recognise button to the appropriate slot in
    # digit recogniser controller.
    def on_recognise_button_click(self):
        self.centralWidget.recogniseButton.clicked.connect(self.digit_recogniser_controller.recognise_digit)

    def set_predicted_digit(self, digit):
        self.centralWidget.setPredictedDigit(digit)