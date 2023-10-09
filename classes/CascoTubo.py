
import thermo
import math
POL2M = 0.0254
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

    def conveccao_casco(self, k_c:float, cp_c:float, mi_c:float, w_c:float, de, Nt, Dotl, Ds, a_tubos,L_t, miw_c = None):
        k = k_c     #   Condutividade térmica do fluído
        cp = cp_c   #   Calor específico
        mi = mi_c   #   Viscosidade do fluído
        w = w_c     #   vazão mássica do fluido
        miw = miw_c #   Viscosidade do fluido avaliada na temperatura da parede
        L_t = L_t     #   Comprimento dos tubos 
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
        def diametroBocal(Ds):
            """ ## Descrição:
                Cálculo o diâmetro do casco e filtra da tabela diâmetro do Bocal
                ## Args:
                    - Ds: diâmetro interno do casco
                ## Return:
                    - d_bocal: diâmetro do bocal [m]
                    - Dc:   diâmetro do casco    [m]
            """
        def li_lo_tabela(Dc):
            """ ## Descrição:
                Filtra da tabela a li e lo com base no diâmetro do casco e classe de pressão [Pesquisar mais sobre isso]
                ## Args:
                    - Ds: diâmetro do casco
                ## Return:
                    - li: [m]
                    - lo: [m]
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
        
        Fbp = (Ds - Dotl) * ls / Sm

        Sbp = (Ds - Dotl) * ls      #   Área para desvio em torno do feixo 

        if Re_s <= 100:
            Cbh = 1.35
        else:
            Cbh = 1.25
        
        Nc = Ds * (1 - 2 * (lc / Ds)) / pp   #   N° de fileiras de tubos cruzados pelo escoamento numa seção de escoamento cruzado

        Nc = Nc // 1        #   Nº Inteiro
        
        folga = (Ds - Dotl)
        if  folga > 1.5 * POL2M or (folga > 0.5 and Sbp/(Sm -Sbp) > 0.1 * POL2M) :
            Nss = Nc // 5       #   Nº de pares de tiras selantes. Costuma-se utilizar umq par de tiras selantes para cada 5 a 7 filas de tubos na seção de escoamento cruzado.
        
        jb = math.exp(-Cbh * Fbp * (1 - (2 * Nss / Nc) ** 1/3))

        #================= Fator de correção para o gradiente adverso de temperatura (Jr) =====================
        
        jr_ = 1.51 / (Nc ** 0.18)
        
        if Re_s > 100:
            jr = 1
        elif Re_s <= 20:
            jr = jr_
        elif 20<= Re_s <100:
            jr = jr_ + ((20 - Re_s) / 80) * (jr_ - 1)
        
        #================= Fator de correção devido ao espaçamento desigual das chicanas na entrada e na saída (Js) =====================
        d_bocal, Dc = diametroBocal(Ds)
        li, lo = li_lo_tabela(Dc)

        lsi = li + d_bocal
        lso = lo + d_bocal

        if Re_s > 100:
            n = 0.6
        elif Re_s <= 100:
            n = 1/3
        
        lsi_ = lsi / ls
        lso_ = lso / ls

        Nb = (L_t - lsi - lso) / ls + 1

        num = (Nb - 1) + (lsi_ ** (1 - n)) + (lso_ ** (1 - n))
        den = (Nb - 1) + (lsi_) + (lso_)

        js = num / den

        #   Cálculo coeficiente de transmissão de calor para o lado do casco
        hs = h_ideal * jc * jl * jb * jr * js
    
    def calculo_temp_parede(self, Tmed, tmed, hs, hio, mi_t, mi_c, fluido_frio:bool):
        """ ## Descrição:
            Cálcula a temperatura da parede, busca valor de miw e correige valores dos coeficientes de transmissão de calor 
            ## Args
                - Tmed: Temperatura calórica ou média do fluído quente 
                - tmed: Temperatura calórica ou média do fluído frio
                - hs: coeficiente de transmissão de calor por convecção lado do casco
                - hio: coeficientes de transmissão de calor por convecção lado do tubo
                - fluido_frio:bool Se o fluído frio estiver no interior do tubo - True
                - mi_t: Viscosidade do fluido do tubo
                - mi_c: Viscosidade do fluido do casco
            ## Return:
                - tw: temperatura da parede 
                - miw: Viscosidade do fluido avaliada na temperatura da parede
        """
        Tc = Tmed    
        tc = tmed 

        if fluido_frio:
            tw = tc + hs/ (hio + hs) * (Tc - tc) 
        else:
            tw = tc + hio/(hio + hs) * (Tc - tc)

        miw = self.propriedades_termodinamicas()

        termo_correcao_tubo = (mi_t / miw) ** 0.14
        termo_correcao_casco= (mi_c / miw) ** 0.14
        
        hs = hs * termo_correcao_casco
        hio = hio * termo_correcao_tubo

    def coef_global_limpo(self, hio, hs):
        """## Descrição:
            Cálcula o coeficiente global limpo com base nos cefientes de transmissão de calor cálculados  
        """

        Uc = hio * hs / (hio + hs)
    
    def fator_incrustacao(self, Uc, Ud, Rd_verd):
        """## Descrição:
            Cálcula do fator de inscrustação e excesso da área de troca
        ## Args:
            - Rd_verd: fator de incrsutação verdadeiro
        
        ## Return:
            - Rd: fator de incrustação calculado
            - Ea: excesso de área de troca [%]
        """
        #   Rd calculados deve ser maior que verdadeiro
        Rd = (Uc - Ud) / (Uc * Ud)
        
        Ud_ = 1 / (1 / Uc + Rd + Rd_verd)
        A_nec = Q / (Ud_ * delta_t)
        Ea = (A_proj - A_nec)/A_nec * 100

    



        

if __name__ == "__main__":
    a = CascoTubo()
    a.balaco_de_energia()
