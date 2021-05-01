# Generates a bar-graph for the probability of each class

import numpy
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class ProbabilityPlot(FigureCanvasQTAgg):

    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlabel('Probability (%)')
        self.axes.set_xlim(0,100)

        self.classes = numpy.arange(0,10)
        self.probabilities = numpy.zeros(10)

        self.axes.set_yticks(self.classes)
        self.axes.barh(self.classes, self.probabilities)

        FigureCanvasQTAgg.__init__(self, self.fig)
    
    def set_probability(self, probabilities):
        self.probabilities = probabilities

        self.axes.clear()

        self.axes.set_xlabel('Probability (%)')
        self.axes.set_xlim(0,100)

        self.axes.set_yticks(self.classes)
        self.axes.barh(self.classes, self.probabilities)

        self.draw()