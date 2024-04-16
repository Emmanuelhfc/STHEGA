from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit
from interface.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.showMaximized()

        self.set_line_edit_termo_tables()

    def set_line_edit_termo_tables(self):
        
        for i in range(self.termoTableShell.rowCount()):
            line_edit = QLineEdit()
            self.termoTableShell.setCellWidget(i, 1, line_edit)
            self.termoTableTube.setCellWidget(i, 1, line_edit)

            

            

