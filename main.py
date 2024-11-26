import sys
from PySide6.QtWidgets import QApplication
from application.application_window import ApplicationWindow


if __name__ == 'main':

    app = QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec())

