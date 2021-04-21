from GUI.probabilityplot import *
class ProbabilityPlotControl():
    def __init__(self):
        self.plot = probabilityPlot()
    
    def setProbability(self, probabilities):
        self.plot.setProbability(probabilities)