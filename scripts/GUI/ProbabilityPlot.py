# Adds the predicted probability plot in the lower right-hand corner of the main window.
# Shows the probability for each digit class that the model generates for a given user drawing.

import numpy
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class ProbabilityPlot(FigureCanvasQTAgg):

    def __init__(self):
        self.fig = Figure() # Create the plot
        
        self.axes = self.fig.add_subplot(111) # Add a 1x1 grid to the figure for the axis
        # Add the probability axis label, always show probabilities between 0 and 100%
        self.axes.set_xlabel('Probability (%)')
        self.axes.set_xlim(0,100)
        
        self.classes = numpy.arange(0,10) # Generate a list of numbers from 0 to 9, which are the possible digit classes
        self.probabilities = numpy.zeros(10) # Initially, all probabilities are 0%
        self.axes.set_yticks(self.classes) # Add y-axis data-points for each digit
        self.axes.barh(self.classes, self.probabilities) # Set the plot to be a horizontal bar-graph

        FigureCanvasQTAgg.__init__(self, self.fig) # Initialise parent class, the PyQT compatible plot class
    
    # Takes an array of probabilities for each class and updates the plot
    def set_probability(self, probabilities):
        self.probabilities = probabilities

        self.axes.clear() # Clear the plot

        # Re-initialise the axis and plot type
        self.axes.set_xlabel('Probability (%)')
        self.axes.set_xlim(0,100)
        self.axes.set_yticks(self.classes)
        self.axes.barh(self.classes, self.probabilities)

        self.draw() # Re-draw the plot
