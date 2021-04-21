from CONTROLLER.CanvasControl import *
from CONTROLLER.ProbabilityPlotControl import *
from GUI.centralwidget import *

class CentralWidgetControl():
    def __init__(self, mainWindow):
        self.canvasController = canvasController()
        self.probabilityController = ProbabilityPlotControl()

        self.mainWindow = mainWindow
        self.mainWindow.setCentralWidget(CentralWidget(self))
        
        #self.probabilityPlotControl = ProbabilityPlotControl()
    def setCentralWidget(self, centralWidget):
        self.centralWidget = centralWidget
    
    def openModel(self):
        fname = QFileDialog.getOpenFileName(self.centralWidget, 'Open file', './') # create file dialog
        if fname[0]:
            f = open(fname[0], 'r')