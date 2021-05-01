# Controllers for the central widget GUI module

from GUI.CentralWidget import *
from GUI.Canvas import *
from GUI.ProbabilityPlot import *

# Controller for the probability plot in the central widget in the main window
class ProbabilityPlotControl():
    def __init__(self):
        self.plot = ProbabilityPlot()
    
    def set_probability(self, probabilities):
        self.plot.set_probability(probabilities)

# Controller for the drawing canvas in the central widget in the main window
class CanvasController():
    def __init__(self):

        self.canvas = Canvas(self)
        self.last_position = None # Initially there is no last position

    def on_mouse_move(self, position):
        if self.last_position is None: # On the first mouse event, do not paint, just save position
            self.last_position = position
        else:
            current_position = position # Set the current position
            self.canvas.draw_line(self.last_position, current_position) # Draw a line from the last position to the current position
            self.last_position = current_position # Save the current position as the last position
    
    def on_mouse_release(self):
        self.last_position = None # Re-set the last position to be none
        self.save_drawing() # Save the drawing
    
    def clear(self):
        self.canvas.clear()

    def save_drawing(self):
        drawing = self.canvas.pixmap()
        drawing.save('user_data/digit_drawing.jpg', "JPEG" )

# Controller for the central widget in the main window
class CentralWidgetController():
    def __init__(self, main_window, digit_recogniser_controller):
        # Controller setup
        self.canvas_controller = CanvasController()
        self.probability_controller = ProbabilityPlotControl()
        self.digit_recogniser_controller = digit_recogniser_controller

        # Widget setup
        self.main_window = main_window
        self.central_widget = CentralWidget(self)
        self.main_window.setCentralWidget(self.central_widget)

        # Button slots
        self.on_clear_button_click()
        self.on_model_button_click()
        self.on_recognise_button_click()

    def on_clear_button_click(self):
        self.central_widget.clear_button.clicked.connect(self.canvas_controller.clear)

    def on_model_button_click(self):
        self.central_widget.model_button.clicked.connect(self.open_model)

    def open_model(self):
        file_name = QFileDialog.getOpenFileName(self.main_window, "Load Model",
                                       "models/",
                                       "Digit Recognizer Models (*.pt)")
        if file_name[0]: # If path exists (user didn't click cancel)
            self.digit_recogniser_controller.load_model(file_name)

    def on_recognise_button_click(self):
        self.central_widget.recognise_button.clicked.connect(self.digit_recogniser_controller.recognise_digit)

    def set_predicted_digit(self, digit):
        self.central_widget.set_predicted_digit(digit)