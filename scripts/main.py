# this is the main file for project 1.

#from GUI.mainwindow import *
from CONTROLLER.MainWindowControl import *
from CONTROLLER.DigitRecogniserController import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    digit_recogniser_controller = DigitRecogniserController()
    main_window_control = MainWindowControl(app, digit_recogniser_controller)
    digit_recogniser_controller.set_main_window_control(main_window_control)
    sys.exit(app.exec())