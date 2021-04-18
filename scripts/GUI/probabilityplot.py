import numpy
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class probabilityPlot(FigureCanvasQTAgg):

    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel('Probability (%)')
        self.axes.set_xlim(0,100)

        classes = numpy.arange(0,10)
        probabilities = [5,10,20,40,20,10,5,0,0,0]

        self.axes.set_yticks(classes)
        self.axes.barh(classes,probabilities)

        FigureCanvasQTAgg.__init__(self, fig)