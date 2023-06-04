import thermo
import math

class CascoTubo:
    def __init__(self):       
        self.ent_Tq = None
        self.sai_Tq =  None
        self.sai_Tf =  None
        self.ent_Tf =  None
        self.v_frio =  None
        self.v_quente =  None
        self.tipo_quente =  None
        self.tipo_frio =  None
        self.num_casco = None

        self.comprimento_max =  None
        self.diametro_max =  None
        self.material_tubos =  None
        self.material_casco =  None
  
    def add_dados_iniciais(self,propriedades = {
                                    'temp_ent_fluido_quente': None,
                                    'temp_sai_fluido_quente': None,
                                    'temp_sai_fluido_frio': None,
                                    'temp_ent_fluido_frio': None,
                                    'vazao_fluido_frio': None,
                                    'vazao_fluido_quente': None,
                                    'tipo_fluido_quente': None,
                                    'tipo_fluido_frio': None,
                                    'Num_passagens_casco': None
                                },
                                limitacoes = {
                                    'comprimento_max': None,
                                    'diametro_max': None,
                                    'material_tubos': None,
                                    'material_casco': None,
                                }):
        
        self.ent_Tq = propriedades['temp_ent_fluido_quente']
        self.sai_Tq = propriedades['temp_sai_fluido_quente']
        self.sai_Tf = propriedades['temp_sai_fluido_frio']
        self.ent_Tf = propriedades['temp_ent_fluido_frio']
        self.v_frio = propriedades['vazao_fluido_frio']
        self.v_quente = propriedades['vazao_fluido_quente']
        self.tipo_quente = propriedades['tipo_fluido_quente']
        self.tipo_frio = propriedades['tipo_fluido_frio']
        self.num_casco = propriedades['Num_passagens_casco'] 

        self.comprimento_max = limitacoes['comprimento_max']
        self.diametro_max = limitacoes['diametro_max']
        self.material_tubos = limitacoes['material_tubos']
        self.material_casco = limitacoes['material_casco']

    def propriedades_termodinamicas(self):
        self.cp_frio = 1
        self.cp_quente = 1
        pass

    def balaco_de_energia(self):
        self.propriedades_termodinamicas()

        if None in (self.ent_Tq, self.sai_Tq, self.v_quente):
            self.q = self.v_frio * self.cp_frio * (self.sai_Tf - self.ent_Tf)
            if self.ent_Tq is None:
                self.ent_Tq = self.ent_Tq + self.q/(self.v_quente * self.cp_quente)
            elif self.sai_Tq is None:
                self.sai_Tq = self.sai_Tq - self.q/(self.v_quente * self.cp_quente)
            else:
                self.v_quente = self.q/(self.cp_quente * (self.ent_Tq - self.sai_Tq ))

        elif None in (self.ent_Tf, self.sai_Tf, self.v_quente):
            self.q = self.v_frio * self.cp_frio * (self.ent_Tq - self.sai_Tq)
            if self.ent_Tf is None:
                self.ent_Tf = self.sai_Tf - self.q/(self.v_frio * self.cp_frio)
            elif self.sai_Tf is None:
                self.sai_Tf = self.ent_Tf + self.q/(self.v_frio * self.cp_frio)
            else:
                self.v_frio = self.q/(self.cp_frio * (self.sai_Tf - self.ent_Tf ))
        
        else:
            self.q = self.v_frio * self.cp_frio * (self.sai_Tf - self.ent_Tf)

    def diferenca_temp_deltaT(self):
        calculo_diferenca_log_MLDT()
        calculo_R_S()
        calculo_F()

        self.deltaT = self.mldt*self.F

        def calculo_diferenca_log_MLDT():
            num = ((self.ent_Tq - self.sai_Tf)-(self.sai_Tq - self.ent_Tf))
            den = math.log(((self.ent_Tq - self.sai_Tf)/(self.sai_Tq - self.ent_Tf)))
            self.mldt = num / den
        
        def calculo_R_S():
            self.R = (self.ent_Tq - self.sai_Tq)/(self.sai_Tf - self.ent_Tf)
            self.S = (self.sai_Tf - self.ent_Tf)/(self.ent_Tq - self.ent_Tf)   

        def calculo_F():
            if self.num_casco  == 1 and self.R != 1:
                num = ((1 + self.R**2)**0.5) * math.log((1 - self.S*self.R)/(1 - self.S))
                a = (2 - self.S * (self.R + 1 - (self.R**2 + 1)**0.5))
                b = (2 - self.S * (self.R + 1 + (self.R**2 + 1)**0.5))
                den = (1 - self.R)*math.log(a/b)

                self.F = num/den

            elif self.num_casco > 1 and self.R != 1:
                nums = (((1 - self.S*self.R)/(1-self.S))**(1/self.num_casco) - 1)
                dens = (((1 - self.S*self.R)/(1 - self.S))**(1/self.num_casco) - self.R)
                self.S = nums/dens

                num = self.S*2**0.5;
                a = (2 - self.S*(2 - 2**0.5))
                b = (2 - self.S*(2 + 2**0.5))
                self.F = num/((1 - self.S)*math.log(a/b))   
            
            else:
                self.S = self.S/(self.S - self.S*self.num_casco + self.num_casco)
                
                num = self.S*2**0.5
                a = (2 - self.S*(2 - 2**0.5))
                b = (2 - self.S*(2 + 2**0.5))
                self.F = num/((1 - self.S)*math.log(a/b))
    
    def n_tubos(self):
        


    def calcular_perda_de_carga():
        pass
    def calcular_efetividade_termica():
        pass
    def calcular_dimensoes():
        pass