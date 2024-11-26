from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QListWidget


class GUI:
    
    def setup_ui(self, parent):

        self.layout = QVBoxLayout(parent)
        self.create_list_btn = QPushButton("Create New List")
        self.layout.addWidget(self.create_list_btn)


