from PySide6.QtWidgets import QApplication
from interface.MainWindow import MainWindow

def show_app():
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()



