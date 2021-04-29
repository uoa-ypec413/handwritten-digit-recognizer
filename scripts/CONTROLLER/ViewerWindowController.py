from GUI.ViewerWindow import *
from GUI.ImageFrame import *

class ImageFrameController():
    def __init__(self):
        self.image_frame = ImageFrame()
    
    def update_page(self, page):
        self.image_frame.set_page(page)
        self.load_dataset(self.dataset)
    
    def load_dataset(self, dataset):
        self.dataset = dataset
        self.image_frame.render_dataset(dataset)

class ViewerWindowController():
    def __init__(self, digit_recogniser_controller):
        self.test_image_frame_controller = ImageFrameController()
        self.train_image_frame_controller = ImageFrameController()
        
        self.digit_recogniser_controller = digit_recogniser_controller

        self.test_viewer_window = ViewerWindow(100, name = 'test')
        self.train_viewer_window = ViewerWindow(600, name = 'train')

        self.test_viewer_window.scroll_area.setWidget(self.test_image_frame_controller.image_frame)
        self.train_viewer_window.scroll_area.setWidget(self.train_image_frame_controller.image_frame)

        self.test_viewer_window.page_combobox.currentIndexChanged.connect(self.set_test_page)
        self.train_viewer_window.page_combobox.currentIndexChanged.connect(self.set_train_page)

        self.test_viewer_window.ok_button.clicked.connect(self.close_test_viewer)
        self.train_viewer_window.ok_button.clicked.connect(self.close_train_viewer)
    
    def show_training_viewer_window(self):
        self.train_image_frame_controller.load_dataset(self.digit_recogniser_controller.digit_recogniser.data.train_dataset)
        self.train_viewer_window.show()
    
    def show_testing_viewer_window(self):
        self.test_image_frame_controller.load_dataset(self.digit_recogniser_controller.digit_recogniser.data.test_dataset)
        self.test_viewer_window.show()
    
    def set_test_page(self):
        self.test_image_frame_controller.update_page(self.test_viewer_window.page_combobox.currentIndex())
    
    def set_train_page(self):
        self.train_image_frame_controller.update_page(self.train_viewer_window.page_combobox.currentIndex())

    def close_test_viewer(self):
        self.test_viewer_window.close()
    
    def close_train_viewer(self):
        self.train_viewer_window.close()