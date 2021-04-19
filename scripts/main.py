# this is the main file for project 1.

#from GUI.mainwindow import *
from CONTROLLER.MainWindowControl import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindowControl = MainWindowControl(app)
    sys.exit(app.exec())