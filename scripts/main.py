# This is the main file for the program. Run this script to run the program.

from CONTROLLER.MainWindowController import *
from CONTROLLER.DigitRecogniserController import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    digit_recogniser_controller = DigitRecogniserController()
    main_window_controller = MainWindowController(app, digit_recogniser_controller)
    digit_recogniser_controller.set_main_window_controller(main_window_controller)
    sys.exit(app.exec())