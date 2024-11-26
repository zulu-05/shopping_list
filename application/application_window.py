from PySide6.QtWidgets import QWidget
from application.gui import GUI


class ApplicationWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Shopping List")
        self.gui = GUI()
        self.init_ui()  


    def init_ui(self):

        self.gui.setup_ui(self)



