from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit
from interface.ui_mainwindow import Ui_MainWindow
from sqlalchemy.orm import Session
from dataBase.connection import engine
from dataBase.models import*
import logging
import os
from modules.CascoTubo import CascoTubo
import pint


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        
        if os.path.exists("static/logs/report.log"):
            os.remove("static/logs/report.log")
        logging.basicConfig(filename='static/logs/report.log', encoding='utf-8', level=logging.DEBUG)

        self.inputs = {}
        self.set_combo_data_thermo()
        self.set_combo_data_design()
        # self.set_line_edit_inputs_tables()
        self.page = 0
    
        self.set_visible_tabs_avaliation()

        # Btns - Avaliation
        self.next_pages.clicked.connect(self.change_pages_avaliation)
        self.calculate_Nt.clicked.connect(self.calculate_tubes_number)
        self.btn_test.clicked.connect(self.fill_values_test)

    def fill_values_test(self):
        self.shell_t_in.setText('219')
        self.shell_t_o.setText('100.4')
        self.shell_cp.setText('0.52')
        self.shell_Rd.setText('0.001')
        self.shell_k.setText('0.0699')
        self.shell_rho.setText('46.8537')
        self.shell_mi.setText('0.375')
        self.shell_w.setText('110687')

        self.tube_t_in.setText('86')
        self.tube_t_o.setText('100.4')
        self.tube_cp.setText('0.998')
        self.tube_Rd.setText('0.002')
        self.tube_k.setText('0.336')
        self.tube_rho.setText('62.2427')
        self.tube_mi.setText('0.7')
        self.tube_w.setText('59.95')


    def set_visible_tabs_avaliation(self):
        for i in range(1, self.avaliation_tabs.count()):
            self.avaliation_tabs.setTabVisible(i, False)

    def calculate_tubes_number(self):
        Nt, limites_ls, limites_lc = self.initial_termo_calculate_shell_and_tube(True)
        self.Nt.setText(str(Nt))
        self.ls.setText(str(limites_ls))
        self.lc.setText(str(limites_lc))
    
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
                self.initial_termo_calculate_shell_and_tube(False)
                self.calculate_shell_and_tube()
                self.avaliation_tabs.setCurrentIndex(2)
                
    def initial_termo_calculate_shell_and_tube(self, calculate_Nt = True):
        self.convert_table_design_input_to_dict()
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

        
        Nt = self.shell_and_tube.filtro_tubos(
                n= self.design_inps['n'],
                Ds= self.design_inps['Ds'],
                de_inch= self.design_inps['de_inch'],
                layout= self.design_inps['layout'],
                pitch_inch= self.design_inps['pitch_inch'],
            )
        
        self.shell_and_tube.area_projeto(self.design_inps["L"])
        self.shell_and_tube.coef_global_min()
        self.shell_and_tube.diametro_interno_tubo(self.design_inps['tube_thickness'])
        
        tube_hot = False
        if self.hot["fluid_side"] == 'tube':            
            tube_hot = True
        
        self.shell_and_tube.conveccao_tubo(tube_hot) 
        limites_ls, limites_lc = self.shell_and_tube.caract_chicana(self.tube_material.currentData())  
                
        if calculate_Nt:
            return Nt, limites_ls, limites_lc
        
        self.shell_and_tube.Nt = int(self.Nt.text())
        # self.shell_and_tube.ls = self.design_inps['ls']
        # self.shell_and_tube.lc = self.design_inps['lc']
        
    def calculate_shell_and_tube(self):
        self.shell_and_tube.diametro_casco(self.design_inps['shell_thickness'])
        self.shell_and_tube.conveccao_casco(self.design_inps['ls'], self.design_inps['lc'], int(self.c_pressure_class.currentText()))
        self.shell_and_tube.calculo_temp_parede()
        self.shell_and_tube.coef_global_limpo()
        self.shell_and_tube.excesso_area()
        self.shell_and_tube.perda_carga_tubo()
        self.shell_and_tube.perda_carga_casco()

    # def set_line_edit_inputs_tables(self):
    #     names_termo_table = ['t_in', 't_o', 'mi', 'cp', 'Rd', 'k', 'rho', 'w', 'type']
    #     self.names_design_table = ['Ds', 'shell_thickness', 'de_pol', 'L', 'passo_pol', 'a_tubos', 'n', 'Nt', 'ls', 'lc', 'tube_wall_correction']
        
    #     for i in range(self.termoTableShell.rowCount()):
            
    #         name_shell = f'shell_{names_termo_table[i]}'
    #         name_tube = f'tube_{names_termo_table[i]}'
            
    #         line_edit = QLineEdit()
    #         setattr(self, name_shell, line_edit)
    #         self.termoTableShell.setCellWidget(i, 0, line_edit)

    #         line_edit = QLineEdit()
    #         setattr(self, name_tube, line_edit)
    #         self.termoTableTube.setCellWidget(i, 0, line_edit)

    #     for i in range(self.designInpTable.rowCount()):
    #         line_edit = QLineEdit()
    #         setattr(self, self.names_design_table[i], line_edit)
    #         self.designInpTable.setCellWidget(i, 0, line_edit)

    
    def set_combo_data_thermo(self):
        self.name_thermos_table = ['t_in', 't_o', 'mi', 'cp', 'Rd', 'k', 'rho', 'w']
        data_units = {
            't_in': [ ('Farenheit', 'degF'), ('Celsius', 'degC'), ('Kelvin', 'degK'),],
            't_o': [ ('Farenheit', 'degF'), ('Celsius', 'degC'), ('Kelvin', 'degK')],
            'cp': [('Btu /lb . F', 'Btu/(lb * degF)'),("J/(kg . K)", 'J/(kg*degK)') ],
            'mi': [('cP', 'cP'), ('kg/(m.s)', 'kg/(m*s)')],
            'Rd': [ ('h.ft^2.°F/Btu', 'h*ft^2*degF/Btu'), ('K.m^2/W', 'degK * m^2/(W)') ],
            'k': [ ('Btu/(h.ft.°F)', 'Btu/(h*ft*degF)'), ('W/K', 'W/degK')],
            'rho': [('lb/ft^3', 'lb/ft^3'), ('kg/m^3', 'kg/m^3')],
            'w': [('lb/h', 'lb/h'), ('kg/s', 'kg/s')]
        }

        for name in self.name_thermos_table:

            combo_name_shell = 'c_shell_' + name
            combo_name_tube = 'c_tube_' + name

            combo_shell = getattr(self, combo_name_shell)
            combo_tube = getattr(self, combo_name_tube)
            
            for unit in data_units[name]:
                combo_shell.addItem(unit[0])
                combo_shell.setItemData(combo_shell.count() - 1, unit[1])

                combo_tube.addItem(unit[0])
                combo_tube.setItemData(combo_shell.count() - 1, unit[1])

    def convert_base_units(self, dict_shell, dict_tube):
        ureg = pint.UnitRegistry()
        Q_ = ureg.Quantity

        for name in self.name_thermos_table:
            shell_combo = getattr(self, 'c_shell_' + name)
            tube_combo = getattr(self, 'c_tube_' + name)

            dict_shell[name] = Q_(dict_shell[name], shell_combo.currentData()).to_base_units().magnitude
            dict_tube[name] = Q_(dict_tube[name], tube_combo.currentData()).to_base_units().magnitude
    

    def connvert_table_thermo_input_to_dict(self):
        dict_thermo_in_shell = {
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
        dict_thermo_in_tube = {
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

        
        self.convert_base_units(dict_thermo_in_shell, dict_thermo_in_tube)

        print(dict_thermo_in_shell)
        print(dict_thermo_in_tube)
        
        dict_thermo_in_shell['fluid_side'] = "shell"
        dict_thermo_in_tube['fluid_side'] = "tube"

        t_in_s = dict_thermo_in_shell['t_in'] 
        t_o_s = dict_thermo_in_shell['t_o']
    
        self.hot = dict_thermo_in_tube
        self.cold = dict_thermo_in_shell

        if t_in_s > t_o_s:
            self.hot = dict_thermo_in_shell
            self.cold = dict_thermo_in_tube
        
        if any(value == "" for value in dict_thermo_in_shell.values()) or any(value == "" for value in dict_thermo_in_shell.values()):
            raise
    

    def set_combo_data_design(self):
        names_design_table = ['Ds', 'shell_thickness',"tube_thickness", 'L',  'ls', 'lc']

        de_inch_values = [1, 0.75]
        for de_inch in de_inch_values:
            self.de_inch.addItem(str(de_inch))
        self.c_de_inch.addItem('inch')

        values_layou = [TubeLayout.ROTATED_SQUARE, TubeLayout.TRIANGULAR, TubeLayout.SQUARE]
        for value in values_layou:
            self.c_layout.addItem(value.name)
        
        n_values = [1, 2, 4, 6, 8]
        for value in n_values:
            self.n.addItem(str(value))
        
        pitch_values = [1.25, 1]
        for value in pitch_values:
            self.pitch_inch.addItem(str(value))
        self.c_pitch_inch.addItem('inch')

        units = ['m', 'inch', 'ft']
        for name in names_design_table:
            name = 'c_' + name
            obj = getattr(self, name)

            for uni in units:
                obj.addItem(uni)
        
        material_values = [('Cu', 2), ('Al',2) , ('Ti', 2)]
        for material in material_values:
            self.tube_material.addItem(material[0])
            self.tube_material.setItemData(self.tube_material.count()-1, str(material[1]))

    def convert_table_design_input_to_dict(self):
        ureg = pint.UnitRegistry()
        Q_ = ureg.Quantity
        self.design_inps = {}   
        inp_names_design_table = ['Ds', 'shell_thickness','tube_thickness', 'L', 'Nt', 'ls', 'lc']
        c_names_desgin_table = ['de_inch', 'pitch_inch', 'c_layout', 'n']
        for param in inp_names_design_table:
            
            atribute = getattr(self, param).text()
            

            if param != 'Nt':
                unit = getattr(self, 'c_'+param).currentText()
                try:
                    atribute = Q_(float(atribute), unit).to_base_units().magnitude
                except:
                    atribute = ''

            self.design_inps[param] = atribute

        for combo_name in c_names_desgin_table:
            combo = getattr(self, combo_name)
            if combo_name == 'c_layout':
                match combo.currentText():
                    case TubeLayout.TRIANGULAR.name:
                        self.design_inps[combo_name.strip('c_')] = TubeLayout.TRIANGULAR
                    case TubeLayout.SQUARE.name:
                        self.design_inps[combo_name.strip('c_')] = TubeLayout.SQUARE
                    case TubeLayout.ROTATED_SQUARE.name:
                        self.design_inps[combo_name.strip('c_')] = TubeLayout.ROTATED_SQUARE
            else:
                self.design_inps[combo_name.strip('c_')]= float(combo.currentText())
        
        print(self.design_inps)

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

        