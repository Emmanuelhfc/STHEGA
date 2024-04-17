from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit
from interface.ui_mainwindow import Ui_MainWindow
from sqlalchemy.orm import Session
from dataBase.connection import engine
from dataBase.Models import*


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        
        self.inputs = {}
        self.set_line_edit_termo_tables()

    def set_line_edit_termo_tables(self):
        
        for i in range(self.termoTableShell.rowCount()):
            line_edit = QLineEdit()
            
            self.termoTableShell.setCellWidget(i, 1, line_edit)
            
             
            self.termoTableTube.setCellWidget(i, 1, line_edit)

        

    def connvert_table_termo_input_to_dict(self):
        params = {
            "t_in": (0, 1),
            "t_o": (1, 1),
            "mi": (2, 1),
            "cp": (3, 1),
            "Rd": (4, 1),
            "k": (5, 1),
            "rho": (6, 1),
            "w": (1, 1),
            "type": (1, 1),
        }

        self.dict_termo_in_shell = {}
        self.dict_termo_in_tube = {}

        for param in params:
            if param == "type":
                value_shell = self.termoTableShell.cellWidget(*params[param]).text()
                value_tube = self.termoTableTube.cellWidget(*params[param]).text()

            value_shell = float(self.termoTableShell.cellWidget(*params[param]).text())
            value_tube = self.termoTableTube.cellWidget(*params[param]).text()
            #TODO
            

    def save_termo_table_inputs_avaliation(self):
        param = self.mapped_termo_input_table
        t_in = float(self.termoTableShell.cellWidget(param["t_in"]).text())
        t_o = float(self.termoTableShell.cellWidget(param["t_o"]).text())

        if t_in > t_o:

        engine_ = engine()
        

        with Session(engine_) as session:
            ...

        