from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit
from interface.ui_mainwindow import Ui_MainWindow
from sqlalchemy.orm import Session
from dataBase.connection import engine
from dataBase.Models import*
import logging
import os



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        
        self.inputs = {}
        self.set_line_edit_termo_tables()
        self.page = 0
        
        if os.path.exists("static/logs/report.log"):
            os.remove("static/logs/report.log")

        logging.basicConfig(filename='static/logs/report.log', encoding='utf-8', level=logging.DEBUG)


        self.set_visible_tabs_avaliation()
        self.next_pages.clicked.connect(self.change_pages_avaliation)
    
    def set_visible_tabs_avaliation(self):
        for i in range(1, self.avaliation_tabs.count()):
            self.avaliation_tabs.setTabVisible(i, False)

    def calculate_tubes_number(self):
        ...
    
    def calculate_avaliation_shell_tube(self):
        ...

    def change_pages_avaliation(self):
        logging.debug("")
        page_atual = self.avaliation_tabs.currentIndex()

        match page_atual:
            case 0:
                # try:
                    self.connvert_table_thermo_input_to_dict()
                    self.avaliation_tabs.setTabVisible(1, True)
                    self.avaliation_tabs.setCurrentIndex(1)
                # except:
                #     trace
                #     self.status_msg.setText("Por Favor preencha todos os dados")
            case 1:
                self.convert_table_design_input_to_dict()
                self.avaliation_tabs.setCurrentIndex(2)
        

    def set_line_edit_termo_tables(self):
        
        for i in range(self.termoTableShell.rowCount()):
            line_edit = QLineEdit()
            self.termoTableShell.setCellWidget(i, 0, line_edit)
            line_edit = QLineEdit()
            self.termoTableTube.setCellWidget(i, 0, line_edit)
            line_edit = QLineEdit()
            self.designInpTable.setCellWidget(i, 0, line_edit)

        

    def connvert_table_thermo_input_to_dict(self):
        params = {
            "t_in": (0, 0),
            "t_o": (1, 0),
            "mi": (2, 0),
            "cp": (3, 0),
            "Rd": (4, 0),
            "k": (5, 0),
            "rho": (6, 0),
            "w": (7, 0),
            "type": (8, 0),
        }

        dict_termo_in_shell = {}
        dict_termo_in_tube = {}

        for param in params:
            
            if param == "type":
                value_shell = self.termoTableShell.cellWidget(*params[param]).text()
                value_tube = self.termoTableTube.cellWidget(*params[param]).text()
            else:
                value_shell = float(self.termoTableShell.cellWidget(*params[param]).text())
                value_tube = float(self.termoTableTube.cellWidget(*params[param]).text())

            dict_termo_in_shell[param] = value_shell
            dict_termo_in_tube[param] = value_tube
        
        
        dict_termo_in_shell['fluid_side'] = "shell"
        dict_termo_in_tube['fluid_side'] = "tube"

        t_in_s = dict_termo_in_shell['t_in'] 
        t_o_s = dict_termo_in_shell['t_o']
        
        self.quente = dict_termo_in_tube
        self.frio = dict_termo_in_shell

        if t_in_s > t_o_s:
            self.quente = dict_termo_in_shell
            self.frio = dict_termo_in_tube

    def convert_table_design_input_to_dict(self):

        params = {
            "Ds": (0, 0),
            "shell_thickness": (1, 0),
            "de_pol": (2, 0),
            "L": (3, 0),
            "passo_pol": (4, 0),
            "a_tubos": (5, 0),
            "n": (6, 0),
            "Nt": (7, 0),
            "ls": (8, 0),
            'lc': (9,0)
        }

        self.design_inps = {}
        for param in params:
            if param == "a_tubos":
                value = self.designInpTable.cellWidget(*param).text()
                continue
            value = float(self.designInpTable.cellWidget(*param).text())

            self.design_inps[param] = value

    def save_termo_table_inputs_avaliation(self):
        engine_ = engine()
        with Session(engine_) as session:
            name_avaliation = self.name_avaliation.text().strip()

            inputs_frio = AvaliationThermoInputsCold(
                t1= self.frio['t_in'],
                t2=self.frio['t_o'],
                mi_f=self.frio['mi'],
                cp_frio=self.frio['cp'],
                Rd_f=self.frio['Rd'],
                k_f=self.frio['k'],
                rho_f=self.frio['rho'],
                w_f=self.frio['w'],
                tipo_f=self.frio['type'],
                fluid_side=self.frio['fluid_side'],

            )

            inputs_quente = AvaliationThermoInputs(
                name_avaliation = name_avaliation,
                T1= self.quente["t_in"],
                T2= self.quente["t_o"],
                mi_q=self.quente["mi"],
                cp_quente=self.quente["cp"],
                Rd_q=self.quente["Rd"],
                k_q=self.quente["k"],
                rho_q=self.quente["rho"],
                w_q=self.quente["w"],
                tipo_q=self.quente["type"],
                fluid_side=self.quente["fluid_side"],
                thermo_inputs_cold= inputs_frio

            )

            session.add_all([inputs_frio, inputs_quente])
            session.commit()

        