
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
                                    'd_int_tubo': None,
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
        self.d = propriedades['d_int_tubo']
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
            self.d # [m]
            self.a_tubos
            self.d_casco # [m]
            self.Nt # número de tubos
    
            
            pass
    # Passo 4 -- Lado do Tubo
    
    def fluido_tubo(self):
        """
        Função para determinar qual o fluido do lado do tubo e qual do lado do casco
        """

    def conveccao_tubo(self,d, n, Nt, L, w_tubo: float, mi_t:float, rho_t: float,  fluido_t: str, t2_t: float, de:float, t1_t: float, cp_t: float, k_t:float, tw:float = None, miw_t = None):
        d = d
        n = n
        Nt = Nt
        w = w_tubo       # Vazão mássica fluído do lado do tubo 
        mi = mi_t
        rho = rho_t
        tipo_fluido = fluido_t
        cp = cp_t
        k = k_t
        miw = miw_t
        L_t = L
        de = de #   Diâmetro externo do tubo

        at_ = math.pi*(d**2)/4   #   área escoamento tubo -- unidade
        at = Nt*at_/n           #   área de escoamento tubo
        Gt = w/at               #   vazão mássica por unidade de área
        Re_t = Gt*d/mi          #   Nº de Re
        v_t = Gt/rho            #   Velocidade escoamento lado do tubo

        if tipo_fluido == "water":
            #   Como a água é um fluido normalmente incrustante não se utilizam velocidades de escoamento inferiores a 1 m/s. Sugere-se ler a parte referente a “Trocadores usando água” , p. 115, do Kern.
            t = (t2_t - t1_t)/2 #   Temperatura média do fluído
            hi = 105 * (1.352 + 0.0198 * t) * v_t**0.8 / d**0.2   #   (3.24b)

        elif Re_t > 10000:

            if miw == None: # Caso não tenha a temperatura da parede
                a = 1
            else:
                a = (mi/miw) ** 0.14

            Nu = 0.027 * (d*Gt/mi)**0.8 * (cp*mi/k)**(1/3) * a
            hi = Nu * k/d
        
        elif Re_t < 2100:
            hi = 3.66*k/d

        elif 2100 <= Re_t <=10000:
            a = 0.1 *((d * Gt / mi) ** (2 / 3) - 125) * (cp * mi / k) ** 0.495
            b = math.exp(-0.0225 * (math.log(cp * mi / k)) ** 2)
            
            if miw == None: # Caso não tenha a temperatura da parede
                a_ = 1
            else:
                a_ = (mi/miw) ** 0.14

            c = a_ * (1 + d/L_t) ** (2/3)  #   Verificar esse L

            Nu = a * b * c
            hi = Nu * k / d
        
        hio = hi * d / de

    def conveccao_casco(self, k_c:float, cp_c:float, mi_c:float, w_c:float, de, Nt, Dotl, Ds, a_tubos, miw_c = None):
        k = k_c     #   Condutividade térmica do fluído
        cp = cp_c   #   Calor específico
        mi = mi_c   #   Viscosidade do fluído
        w = w_c     #   vazão mássica do fluido
        miw = miw_c #   Viscosidade do fluido avaliada na temperatura da parede
        a_tubos = a_tubos
        if miw == None: # Caso não tenha a temperatura da parede
            a_ = 1
        else:
            a_ = (mi/miw) ** 0.14

        
        def caract_chicana(self):
            """ Define as características das chicanas

            Return:
                -ls: Espaçamento das chicanas  
                -lc: Corte das chicanas
                """

        def fator_ji(Re_c, de, a_tubos, p):
            """ Busca na tabela os valores necessário e faz o cálculo do fator ji 
            """
            Re_s = Re_c
            
            #   Trecho para buscar na tabela as constantes
            #   Filtrar pelo arranjo de tubos e Res
            a1 = ""
            a2 = ""
            a3 = ""
            a4 = ""
            
            a = a3 / (1 + 0.14 * (Re_s) ** a4)

            ji = a1 * (1.33 / (p * de)) ** a * (Re_s) ** a2

            return ji

        def tabela_passo(a_tubos, de):
            """ 
                Escolhe o valor dos passos pela tabela em [m]  
            """
        
        def tabela_delta_sb(Ds):
            """ Filtra delta_sb [m]
                Return:
                    -p: passo
                    -pp: passo dos tubos paralelo ao escoamento
                    -pn: passo dos tubos perpendicular ao escoamento
            """

        #================= Cálculo para feixe de tubos ideal =====================
        ls, lc = caract_chicana()
        p, pn, pp = tabela_passo()

        Ds = Ds     #   Diamentro interno do casco
        Dotl = Dotl   #   Diametro do feixe de tubos 
        
        if a_tubos == "triangula_30" or a_tubos == "triangular_60":
            Sm = ls * (Ds - Dotl + (Dotl - de) / p * (p - de))
        else:
            Sm = ls * (Ds - Dotl + (Dotl - de) / pn * (p - de))

        Re_s = de * w / (mi * Sm)
        
        ji = fator_ji(Re_s, de, a_tubos, p)

        h_ideal = ji * cp * w/Sm * ((k/(cp * mi))**(2/3)) * a_

        #================= Fator de correção para os efeitos da configuração da chicana =====================

        Fc = 1/math.pi * (math.pi + 2 * (Ds - 2 * lc) / Dotl * math.sin( math.acos((Ds - 2 * lc) / Dotl)) - 2 * math.acos((Ds - 2 * lc) / Dotl))    #   Nº tubos seção de escoamento cruzado
        
        jc = Fc + 0.54 * (1 - Fc) ** 0.345

        #================= Fator de correção para os efeitos dos vazamentos da chicana =====================
        
        delta_sb  = tabela_delta_sb(Ds)  #   Folga diametral casco chicana
        Ssb = Ds * delta_sb / 2 * (math.pi - math.acos(1 - 2 * lc / Ds))    #   Área de seção de vazamento casco chicana 
        delta_tb = 7.938 * 10 ** - 4       #    [m] - Folga diametral tubo chicana- TEMA - Classe R - Verificar valor
        Stb = math.pi * de * delta_tb * Nt * (Fc + 1) / 4   #   Área da seção de vazamento tubo-chicana
        alpha = 0.44 * (1 - Ssb / (Ssb + Stb))
        jl = alpha + (1 - alpha) * math.exp(-2.2 * (Stb + Ssb) / Sm)

        #================= Fator de correção para os efeitos de contorno (“bypass” ) do feixe =====================
        
        if Re_s <= 100:
            Cbh = 1.35
        else:
            Cbh = 1.25
        
        Nc = Ds * (1 - 2 * (lc / Ds)) / pp   #   N° de fileiras de tubos cruzados pelo escoamento numa seção de escoamento cruzado
        
        jb = math.exp(-Cbh * Fbp * (1 - (2 * Nss / Nc) ** 1/3))

        #   Cálculo coeficiente de transmissão de calor para o lado do casco
        hs = h_ideal * jc * jl * jb * jr * js




    

if __name__ == "__main__":
    a = CascoTubo()
    a.balaco_de_energia()
