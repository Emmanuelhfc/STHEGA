from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit
from interface.ui_mainwindow import Ui_MainWindow
from sqlalchemy.orm import Session
from dataBase.connection import engine
from dataBase.Models import*
import logging
import os
from modules.CascoTubo import CascoTubo



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        
        if os.path.exists("static/logs/report.log"):
            os.remove("static/logs/report.log")
        logging.basicConfig(filename='static/logs/report.log', encoding='utf-8', level=logging.DEBUG)

        self.inputs = {}
        self.set_line_edit_inputs_tables()
        self.page = 0
    
        self.set_visible_tabs_avaliation()

        # Btns - Avaliation
        self.next_pages.clicked.connect(self.change_pages_avaliation)
        self.calculate_Nt.clicked.connect(self.calculate_tubes_number)

    def set_visible_tabs_avaliation(self):
        for i in range(1, self.avaliation_tabs.count()):
            self.avaliation_tabs.setTabVisible(i, False)

    def calculate_tubes_number(self):
        Nt = self.initial_termo_calculate_shell_and_tube(True)
        self.Nt.setText(str(Nt))
    
    def calculate_avaliation_shell_tube(self):
        ...

    def change_pages_avaliation(self):
        logging.debug("")
        page_atual = self.avaliation_tabs.currentIndex()

        match page_atual:
            case 0:
                try:
                    self.connvert_table_thermo_input_to_dict()
                    self.avaliation_tabs.setTabVisible(1, True)
                    self.avaliation_tabs.setCurrentIndex(1)
                except:
                    self.status_msg.setText("Por Favor preencha todos os dados")
            case 1:
                self.convert_table_design_input_to_dict()
                self.avaliation_tabs.setCurrentIndex(2)
                
    def initial_termo_calculate_shell_and_tube(self, calculate_Nt = False):

        # Nº passes no casco =1
        self.shell_and_tube =  CascoTubo(
            T1 = self.hot['t_in'],
            T2 = self.hot['t_o'],
            t1 = self.cold['t_in'],
            t2 = self.cold['t_o'],
            wf = self.cold['w'],
            wq = self.hot['w'],
            cp_quente = self.hot["cp"],
            cp_frio = self.cold['cp'],
            num_casco = 1,
            rho_q = self.hot['rho'],
            rho_f = self.cold['rho'],
            mi_f = self.cold['mi'],
            mi_q = self.hot['mi'],
            k_q = self.hot['k'],
            k_f = self.cold['k'],
            tipo_q = self.hot['type'],
            tipo_f = self.cold['type'],
            Rd_f = self.cold['Rd'],
            Rd_q = self.hot['Rd'],
        )      

        if calculate_Nt:
            Nt = self.shell_and_tube.filtro_tubos(
                    n= int(self.n.text()),
                    Ds= float(self.Ds.text()),
                    de_inch= float(self.de_pol.text()),
                    layout= self.a_tubos.text(),
                    pitch_inch= float(self.passo_pol.text()),
                )
            return Nt
        
        self.shell_and_tube.Nt = int(self.Nt.text())

    def set_line_edit_inputs_tables(self):
        names_termo_table = ['t_in', 't_o', 'mi', 'cp', 'Rd', 'k', 'rho', 'w', 'type']
        self.names_design_table = ['Ds', 'shell_thickness', 'de_pol', 'L', 'passo_pol', 'a_tubos', 'n', 'Nt', 'ls', 'lc', 'tube_wall_correction']
        
        for i in range(self.termoTableShell.rowCount()):
            
            name_shell = f'shell_{names_termo_table[i]}'
            name_tube = f'tube_{names_termo_table[i]}'
            
            line_edit = QLineEdit()
            setattr(self, name_shell, line_edit)
            self.termoTableShell.setCellWidget(i, 0, line_edit)

            line_edit = QLineEdit()
            setattr(self, name_tube, line_edit)
            self.termoTableTube.setCellWidget(i, 0, line_edit)

        for i in range(self.designInpTable.rowCount()):
            line_edit = QLineEdit()
            setattr(self, self.names_design_table[i], line_edit)
            self.designInpTable.setCellWidget(i, 0, line_edit)



    def connvert_table_thermo_input_to_dict(self):
        dict_termo_in_shell = {
            't_in': float(self.shell_t_in.text()),
            't_o': float(self.shell_t_o.text()),
            'mi': float(self.shell_mi.text()),
            'cp': float(self.shell_cp.text()),
            'Rd': float(self.shell_Rd.text()),
            'k': float(self.shell_k.text()),
            "rho": float(self.shell_rho.text()),
            "w": float(self.shell_w.text()),
            "type": self.shell_type.text(),
        }
        dict_termo_in_tube = {
            't_in': float(self.tube_t_in.text()),
            't_o': float(self.tube_t_o.text()),
            'mi': float(self.tube_mi.text()),
            'cp': float(self.tube_cp.text()),
            'Rd': float(self.tube_Rd.text()),
            'k': float(self.tube_k.text()),
            "rho": float(self.tube_rho.text()),
            "w": float(self.tube_w.text()),
            "type": self.tube_type.text(),
        }
        
        dict_termo_in_shell['fluid_side'] = "shell"
        dict_termo_in_tube['fluid_side'] = "tube"

        t_in_s = dict_termo_in_shell['t_in'] 
        t_o_s = dict_termo_in_shell['t_o']
    
        self.hot = dict_termo_in_tube
        self.cold = dict_termo_in_shell

        if t_in_s > t_o_s:
            self.hot = dict_termo_in_shell
            self.cold = dict_termo_in_tube
        
        if any(value == "" for value in dict_termo_in_shell.values()) or any(value == "" for value in dict_termo_in_shell.values()):
            raise

    # def convert_table_design_input_to_dict(self):
    #     self.design_inps = {}   

    #     for param in self.names_design_table:
            
    #         atribute = getattr(self, param).text()
    #         if param != 'a_tubos':
    #             atribute = float(atribute)

    #         self.design_inps[param] = atribute


    def save_termo_table_inputs_avaliation(self):
        engine_ = engine()
        with Session(engine_) as session:
            name_avaliation = self.name_avaliation.text().strip()

            inputs_frio = AvaliationThermoInputsCold(
                t1= self.cold['t_in'],
                t2=self.cold['t_o'],
                mi_f=self.cold['mi'],
                cp_frio=self.cold['cp'],
                Rd_f=self.cold['Rd'],
                k_f=self.cold['k'],
                rho_f=self.cold['rho'],
                w_f=self.cold['w'],
                tipo_f=self.cold['type'],
                fluid_side=self.cold['fluid_side'],

            )

            inputs_quente = AvaliationThermoInputs(
                name_avaliation = name_avaliation,
                T1= self.hot["t_in"],
                T2= self.hot["t_o"],
                mi_q=self.hot["mi"],
                cp_quente=self.hot["cp"],
                Rd_q=self.hot["Rd"],
                k_q=self.hot["k"],
                rho_q=self.hot["rho"],
                w_q=self.hot["w"],
                tipo_q=self.hot["type"],
                fluid_side=self.hot["fluid_side"],
                thermo_inputs_cold= inputs_frio

            )

            session.add_all([inputs_frio, inputs_quente])
            session.commit()

        