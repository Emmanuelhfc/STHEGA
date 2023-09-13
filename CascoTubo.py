
import thermo
import math
class CascoTubo:
    def __init__(self,propriedades = {
                                    'temp_ent_fluido_quente': None,
                                    'temp_sai_fluido_quente': None,
                                    'temp_sai_fluido_frio': None,
                                    'temp_ent_fluido_frio': None,
                                    'vazao_fluido_frio': None,
                                    'vazao_fluido_quente': None,
                                    'tipo_fluido_quente': None,
                                    'tipo_fluido_frio': None,
                                    'Num_passagens_casco': None,
                                    'L':None,
                                    'Num_passagens_tubo': None,
                                    'd_tubo': None,
                                    'arranjo_tubos': None,
                                    'diametro_interno_casco': None
                                },
                                limitacoes = {
                                    'L_max': None,
                                    'd_max_casco': None,
                                    'd_max_tubos': None,
                                    'material_tubos': None,
                                    'material_casco': None,
                                }):
        
        # Propriedades termodinâmicas
        self.T1 = propriedades['temp_ent_fluido_quente']
        self.T2 = propriedades['temp_sai_fluido_quente']
        self.t2 = propriedades['temp_sai_fluido_frio']
        self.t1 = propriedades['temp_ent_fluido_frio']
        self.wf = propriedades['vazao_fluido_frio']
        self.wq = propriedades['vazao_fluido_quente']
        self.tipo_quente = propriedades['tipo_fluido_quente']
        self.tipo_frio = propriedades['tipo_fluido_frio']

        # Propriedades mecânicas
        self.num_casco = propriedades['Num_passagens_casco'] 
        self.L = propriedades['L'] 
        self.nump_tubos = propriedades['Num_passagens_tubo']
        self.d = propriedades['d_tubo']
        self.a_tubos = propriedades['arranjo_tubos']
        self.d_casco = propriedades['diametro_interno_casco']

        # Limitações
        self.L_max = limitacoes['L_max']
        self.d_max_casco = limitacoes['d_max_casco']
        self.material_tubos = limitacoes['material_tubos']
        self.material_casco = limitacoes['material_casco']
        self.d_max_tubo = limitacoes['d_max_tubos']


    def propriedades_termodinamicas(self):
        self.cp_frio = 1
        self.cp_quente = 1
        pass

    def balaco_de_energia(self):
        self.propriedades_termodinamicas()

        if None in (self.t1, self.t2, self.wq) and  None in (self.T1, self.T2, self.wq):
            print("Não tem nenhum valor.")

        elif None in (self.T1, self.T2, self.wq):
            self.q = self.wf * self.cp_frio * (self.t2 - self.t1)
            if self.T1 is None:
                self.T1 = self.T1 + self.q/(self.wq * self.cp_quente)
            elif self.T2 is None:
                self.T2 = self.T2 - self.q/(self.wq * self.cp_quente)
            else:
                self.wq = self.q/(self.cp_quente * (self.T1 - self.T2 ))

        elif None in (self.t1, self.t2, self.wq):
            self.q = self.wf * self.cp_frio * (self.T1 - self.T2)
            if self.t1 is None:
                self.t1 = self.t2 - self.q/(self.wf * self.cp_frio)
            elif self.t2 is None:
                self.t2 = self.t1 + self.q/(self.wf * self.cp_frio)
            else:
                self.wf = self.q/(self.cp_frio * (self.t2 - self.t1 ))
        
        else: # Se tiver todos os parâmetros
            self.q = self.wf * self.cp_frio * (self.t2 - self.t1) 

            

    def diferenca_temp_deltaT(self):
        calculo_diferenca_log_MLDT()
        calculo_R_S()
        calculo_F()
        self.deltaT = self.mldt*self.F

        def calculo_diferenca_log_MLDT():
            num = ((self.T1 - self.t2)-(self.T2 - self.t1))
            den = math.log(((self.T1 - self.t2)/(self.T2 - self.t1)))
            self.mldt = num / den
        
        def calculo_R_S():
            self.R = (self.T1 - self.T2)/(self.t2 - self.t1)
            self.S = (self.t2 - self.t1)/(self.T1 - self.t1)   

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
            """
            Busca no banco de dados o número de tubos e diâmetro do feixe  
            """

            self.L
            self.nump_tubos
            self.d 
            self.a_tubos
            self.d_casco 
    
            
            pass

if __name__ == "__main__":

    a = CascoTubo()
    a.balaco_de_energia()


