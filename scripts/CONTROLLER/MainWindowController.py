# Controller for the Main Window GUI Module

from GUI.MainWindow import *
from CONTROLLER.TrainingWindowController import *
from CONTROLLER.CentralWidgetController import *
from CONTROLLER.ViewerWindowController import *

class MainWindowController():
    # Takes the digit recogniser controller as many functions need this
    def __init__(self, app, digit_recogniser_controller):
        self.main_window = MainWindow(app)
        self.digit_recogniser_controller = digit_recogniser_controller
        # Create GUI Controller instances
        self.training_window_controller = TrainingWindowController(digit_recogniser_controller)
        self.central_widget_controller = CentralWidgetController(self.main_window, digit_recogniser_controller)
        self.viewer_window_controller = ViewerWindowController(digit_recogniser_controller)

        # Signal-Slot Connections
        self.on_exit_action_click()
        self.on_train_model_action_click()
        self.on_training_images_action_click()
        self.on_testing_images_action_click()
        self.on_basic_nn_action_click()
        self.on_lenet5_action_click()
        self.on_adjusted_lenet5_action_click()
        self.on_load_model_action_click()
        self.on_save_model_action_click()
        
    def on_exit_action_click(self):
        self.main_window.exit_action.triggered.connect(self.main_window.quit_window)

    def on_train_model_action_click(self):
        self.main_window.train_model_action.triggered.connect(self.training_window_controller.show_training_window)
    
    def on_training_images_action_click(self):
      self.main_window.view_training_images_action.triggered.connect(self.viewer_window_controller.show_training_viewer_window)
     
    def on_testing_images_action_click(self):
      self.main_window.view_testing_images_action.triggered.connect(self.viewer_window_controller.show_testing_viewer_window)

    def on_basic_nn_action_click(self):
        self.main_window.basic_nn_action.triggered.connect(self.digit_recogniser_controller.set_basic_model)
    
    def on_lenet5_action_click(self):
        self.main_window.lenet5_action.triggered.connect(self.digit_recogniser_controller.set_LN5_model)
    
    def on_adjusted_lenet5_action_click(self):
        self.main_window.adjusted_lenet5_action.triggered.connect(self.digit_recogniser_controller.set_ALN5_model)
    
    def on_load_model_action_click(self):
        self.main_window.load_model_action.triggered.connect(self.load_model)

    def on_save_model_action_click(self):
        self.main_window.save_model_action.triggered.connect(self.save_model)
    
    def enable_dataset_viewer(self):
        self.main_window.enable_dataset_viewer()
    
    def load_model(self):
        file_name = QFileDialog.getOpenFileName(self.main_window, "Load Model",
                                       "models/",
                                       "Digit Recognizer Models (*.pt)")
        if file_name[0]: # If path exists (user didn't click cancel)
            self.digit_recogniser_controller.load_model(file_name)
    
    def save_model(self):
        file_name = QFileDialog.getSaveFileName(self.main_window, "Save Model",
                                       "models/new_model.pt",
                                       "Digit Recognizer Models (*.pt)")
        if file_name[0]: # If path exists (user didn't click cancel)
            self.digit_recogniser_controller.save_model(file_name)