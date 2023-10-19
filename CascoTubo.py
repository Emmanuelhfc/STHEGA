
import thermo
import math
import sqlite3
from dataBase.constants import*
from dataBase.comandos_sql import*
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
        self.n = propriedades['Num_passagens_tubo']
        self.d = propriedades['d_int_tubo']
        self.a_tubos = propriedades['arranjo_tubos']
        self.d_casco = propriedades['diametro_interno_casco']

        # Limitações
        self.L_max = limitacoes['L_max']
        self.d_max_casco = limitacoes['d_max_casco']
        self.material_tubos = limitacoes['material_tubos']
        self.material_casco = limitacoes['material_casco']
        self.d_max_tubo = limitacoes['d_max_tubos']


    """ ## Anotações:
            ## Variáveis de controle (Genes)
                - Temperaturas de entrada e saída:
                - vazão:
                - L
                - Ds -> de
                - a_tubos
                - fluido do lado do casco e fluido do lado do tubo
                - lc: corte da chicana
                - ls: espaçamento das chicanas
                - Npt: nº de passagens no casco
            
            ## Por enquanto o programa não tem a lógica da troca de fase 

        TODO -> Rever tipos de arranjos dos tubos por tabelas da norma;
        TODO -> Update - arredondar valores das tabelas
        TODO -> rever se tabelas tem todos tipos de arranjo e se arranjos estão com nomes corretos
        TODO -> consertar tabela delta_sb, pode ter valores de Dn que não se enquadram em nenhuma condição

    """
    
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

    def filtro_tubos(self, n, Ds, de, a_tubos, passo):
            """ ## Descrição:
                    - Filtra da tabela de nº de tubos de fabricantes o valor diâmetro do feixe, nº de passagens no tubo e nº de tubos
                ## Args:
                    - n: número de passes no tubos
                    - Ds: diâmetro interno do casco 
                    - de: diâmetro externo do tubo
                    - a_tubos: arranjo dos tubos
                    - passo:
                ## Return
                    - Nt: nº de tubos
                    - Dotl: diâmetor do feixe
            """
            npt = ""
            if n == 1:
                npt = "Np_1"
            elif n == 2:
                npt = "Np_2"
            elif n == 4:
                npt = "Np_4"
            elif n == 6:
                npt = "Np_6"
            elif n == 8:
                npt = "Np_8"
            
            a_tubos = a_tubos + passo

            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_NT = f"SELECT {npt} FROM Contagem_de_tubos WHERE a_tubos = '{a_tubos}' AND Ds_m = {Ds} AND d_m = {de}"
            sql_Dotl = f"SELECT Dotl_m FROM Contagem_de_tubos WHERE a_tubos = '{a_tubos}' AND Ds_m = {Ds} AND d_m = {de}"

            Nt = filtro_sqlite(cursor, sql_NT, True)
            Dotl = filtro_sqlite(cursor, sql_Dotl, True)

            if len(Nt) > 1 or len(Dotl) > 1:
                print(" ERRO: mais de uma correspondência para Nt e Dotl em filtro_tubos")
                return
            
            return Nt[0], Dotl[0]
            

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
    
    def caract_chicana(self):
        """ ## Descrição: 
                - Define as características das chicanas, caso não tenha sido definida previamente. Aleatoriza o valor de acordo com recomendações da norma.
            ## Return:
                - ls: Espaçamento das chicanas  
                - lc: Corte das chicanas
        """

    def conveccao_casco(self, k:float, cp:float, mi:float, w:float, de, Nt, Dotl, Ds, a_tubos, L_t, ls, lc, p):
        """ ## Descrição:
                - Função que faz o cálculo da convecção no casco.
            ## Args:
                - k: condutividade térmica
                - cp: calor específico do fluído no casco
                - mi: viscosidade do fluido no casco
                - w: vazão mássica do fluido
                - de: diâmetro externo do tubo
                - Nt: nº de tubos
                - Dotl: diâmetro do feixe de tubos
                - Ds: diâmetro do casco
                - a_tubos: arranjo dos tubos
                - L_t:
                - ls: Espaçamento das chicanas
                - lc: Corte das chicanas
                - p: passos dos tubos    
        """
        
        def tabela_passo(a_tubos, de):
            """ ## Descrrição:
                    - Filtra da tabela o valor dos passos em [m].
                ## Args:
                    - a_tubos: arranjo dos tubos
                    - de: diâmetro externo do tubo
                ## Return:
                    - pn
                    - pp 
            """
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f"SELECT * FROM Passos_tubos WHERE de = {de} AND a_tubos = {a_tubos}"
            linha = filtro_sqlite(cursor, sql_linha)
            
            if len(linha) > 1 :
                print("Erro: mais de uma correspondência na tabela de passos")
                return


            pn = linha[0][-1]
            pp = linha[0][-2]

            return pn, pp

        def fator_ji(Res, de, angulo_tubos, p):
            """ ## Descrição:
                    - Filtra da tabela os valores das constantes a e faz o cálculo do fator ji.
                ## Args:
                    - Res: nº de Re lado do casco
                    - de: diâmetro externo do casco
                    - angulo_tubos: angulo dos tubos dependendo do arranjo
                    - p: passo dos tubos
                ## Return:
                    - ji:
            """
                
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f"SELECT * FROM constantes_a WHERE angulo_a_tubos = '{angulo_tubos}' AND Res_max >= {Res} AND Res_min < {Res}"
            linha = filtro_sqlite(cursor, sql_linha)
            
            if len(linha) > 1 :
                print("Erro: mais de uma correspondência na tabela de constantes a")
                return
            
            a4 = linha[0][-1]
            a3 = linha[0][-2]
            a2 = linha[0][-3]
            a1 = linha[0][-4]
            
            a = a3 / (1 + 0.14 * Res ** a4)

            ji = a1 * (1.33 / (p * de)) ** a * Res ** a2

            return ji

        
        def tabela_delta_sb(Dn):
            """ ## Descrição:
                    - Filtra delta_sb [m]
                ## Args:
                    - Dn: diâmetro nominal do caso
                Return:
                    -delta_sb: arbetura diametral casco chicana
            """
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f"SELECT delta_sb FROM Delta_sb WHERE Dn_min <= {Dn} AND Dn_max >= {Dn} "
            linha = filtro_sqlite(cursor, sql_linha)
            
            if len(linha) > 1 :
                print("Erro: mais de uma correspondência na tabela de constantes a")
                return

        def diametro_bocal(Ds):
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
        pn, pp = tabela_passo()

        
        if a_tubos == "triangula_30" or a_tubos == "triangular_60":
            Sm = ls * (Ds - Dotl + (Dotl - de) / p * (p - de))
        else:
            Sm = ls * (Ds - Dotl + (Dotl - de) / pn * (p - de))

        Res = de * w / (mi * Sm)
        
        ji = fator_ji(Res, de, a_tubos, p)

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
        
        Fbp = (Ds - Dotl) * ls / Sm     #   Fração da área de escoamento cruzado em que pode ocorrer a corrente C

        Sbp = (Ds - Dotl) * ls      #   Área para desvio em torno do feixo 

        if Res <= 100:
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
        
        if Res > 100:
            jr = 1
        elif Res <= 20:
            jr = jr_
        elif 20<= Res <100:
            jr = jr_ + ((20 - Res) / 80) * (jr_ - 1)
        
        #================= Fator de correção devido ao espaçamento desigual das chicanas na entrada e na saída (Js) =====================
        d_bocal, Dc = diametro_bocal(Ds)
        li, lo = li_lo_tabela(Dc)

        lsi = li + d_bocal
        lso = lo + d_bocal

        if Res > 100:
            n = 0.6
        elif Res <= 100:
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
            Cálcula a temperatura da parede, busca valor de miw e correige valores dos coeficientes de transmissão de calor multiplicando-os
            pelo fator phi_t. 
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
                - phi_t_tubo: valor do termo (mi / miw) ^ 0.14 para o tubo
                - phi_t_casco: valor do termo (mi / miw) ^ 0.14 para o casco
        """
        Tc = Tmed    
        tc = tmed 

        if fluido_frio:
            tw = tc + hs/ (hio + hs) * (Tc - tc) 
        else:
            tw = tc + hio/(hio + hs) * (Tc - tc)

        miw = self.propriedades_termodinamicas()

        phi_t_tubo = (mi_t / miw) ** 0.14
        phi_t_casco= (mi_c / miw) ** 0.14
        
        hs = hs * phi_t_casco
        hio = hio * phi_t_tubo

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


    def perda_carga_tubo(self, Re_t, rho, di, phi_t, G_t, L, n, v):
        """ ## Descrição:
            - Cálculo da perda de carga do lado do tubo.
            ## Args:
                - Re_t: número de Re do lado do tubo;
                - rho: densidade do fluido lado do tubo
                - di: diâmetro interno do tubo
                - phi_t: termo (mi/miw) ^ 0.14 para lado do tubo
                - Gt: vazão mássica por unidade de área do tubo
                - L: comprimento d tubo
                - v: velocidade do escoamento
                - n: nº de passes do tubos
            ## Return
                - delta_PT: perda de carga do lado do tubo.  
        """
        

        delta_Pr = (4 * n * rho * v ** 2) / 2       #   Perda de carga de retorno 

        f = (1.58 * math.log(Re_t) - 3.28) ** -2    #   Fator de atrito de Fanning

        delta_Pt = (4 * f * G_t ** 2 * L * n) / (di * 2 * rho * phi_t) 

        delta_PT = delta_Pt + delta_Pr

    def perda_carga_casco(self, Nb, mi, miw, de, Res, W, rho, Nc, Stb, Ssb, Sm, Nss, Fbp, p, pp, lc, Ds, Fc, Nt, ls, lsi_, lso_):
        """ ## Descrição:
            - Cálculo da perda de carga do lado do caso.
            ## Args:
                - Nb: nº de chicanas
                - mi: viscosidade do fluido lado do casco
                - miw: viscosidade do fluido avaliada na temperatura da parede
                - de: diâmetro externo do tubo
                - Res: Nº de Re lado do casco
                - W: vazão mássica do fluido do casco
                - Nc: Nº de fileiras de tubos cruzados pelo escoamento numa seção de escoamento 
                - rho: densidade do fluido do lado do casco
                - Stb: Área da seção de vazamento tubo-chicana
                - Ssb: Área de seção de vazamento casco chicana
                - Sm: Área da seção de escoamento cruzado, na ou próxima à linha de centro
                - Nss: Nº de pares de tiras selantes.
                - Fbp: Fração da área de escoamento cruzado em que pode ocorrer a corrente C
                - p: passo dos tubos
                - pp: passo dos tubos perpendicular ao escoamento
                - lc: corte das chicanas
                - Ds: diâmetro interno do casco
                - Fc: Nº tubos seção de escoamento cruzado
                - Nt: Nº de tubos
                - ls: espaçamento das chicanas
                - lsi_: razão entre espaçamento da chicana de entrada e espaçamento das chicanas
                - lso_: razão entre espaçamento da chicana de saída e espaçamento das chicanas
            ## Return
                - delta_Ps: perda de carga do lado do casco   
        """
        def constantes_b():
            ...
        #================ Perda de carga na seção de escoamento cruzado ======================
        if Res <= 100:
            Cbp = 4.5
        elif Res > 100:
            Cbp = 3.7

        Rb_a = (1 - (2 * Nss / Nc) ** (1/3))
        Rb = math.exp(-Cbp * Fbp * Rb_a)        #   Fator de correção para efeito do contorno do feixe    

        m = 0.15 * (1 + Ssb / (Stb + Ssb)) + 0.8
        Rl_b = ((Stb + Ssb) / Sm) ** m 
        Rl_a = (1 + Ssb / (Stb + Ssb)) * -1.33

        Rl = math.exp(Rl_a * Rl_b)      #   Fator de correlção para efeitos de vazamento na chicana
        
        b1, b2, b3, b4 = constantes_b
        b = b3 / (1 + 0.14 * Res ** b4)
        fi = b1 * (1.33 / (p * de)) ** b * (Res) ** b2      #   Fator de atrito para um feixe de tubos ideal
        delta_Pbi = (4 * fi * W **2 * Nc / (rho * Sm ** 2) )* (mi / miw) ** -0.14   #   Perda de carga para uma seção ideal de fluxo cruzado
        delta_Pc = delta_Pbi * (Nb -1) * Rb * Rl

        #================= Perda de carga nas janelas ==============================================
        
        if Res >= 100:      #   Escoamento turbulento
            
            Swg_a = 1 - 2 * lc / Ds 
            Swg_b = (1-Swg_a ** 2) ** (1/2)
            Swg = Ds ** 2 / 4 * (math.acos(1 - 2 * lc / Ds) - Swg_a * Swg_b)      #   Área total da janela

            Swt = Nt / 8 * (1 - Fc) * math.pi * de ** 2     # Área ocupada pelos tubos na janela

            Sw = Swg - Swt      #   Área da seção de escoamento da janela

            Ncw = 0.8 * lc / pp     #   Nº de fileiras de tubos efetivamente cruzados em cada janela
            Ncw = Ncw // 1
            delta_Pwi = W ** 2 * (2 + 0.6 * Ncw) / (2 * Sm * Sw * rho)  #   Perda de carga em uma seção de janela ideal
        
        elif Res < 100:     #   Escoamento laminar
            theta_b = 2 * math.acos(1 - 2 * lc / Ds)        #   Ângulo de corte da chicana em radianos
            Dw = 4 * Sw / ((math.pi / 2) * Nt * (1 - Fc) * de + Ds * theta_b)       #   Diâmetro equivalente da janela

            delta_Pwi_a = 26 * mi * W / (rho * (Sm * Sw) ** (1/2))
            delta_Pwi_b = (Ncw / (p - de) + ls / (Dw ** 2))
            delta_Pwi_c = 2 * W ** 2 / (2 * Sm * Sw * rho)
            delta_Pwi = delta_Pwi_a * delta_Pwi_b + delta_Pwi_c
                
        delta_Pw = Nb * delta_Pwi * Rl

        #================== Perda de carga nas regiões de entrada e saída do casco delta_Pe ============

        if Res <= 100:
            n = 1
        elif Res > 100:
            n = 0.2
        Rs = 1 / 2 * (lsi_ ** (n - 2) + lso_ ** (n-2))      #   Fator de correção devido o espaçamento desigual das chicanas
        delta_Pe = 2 * delta_Pbi * (1 + Ncw / Nc) * Rb * Rs

        
        #================ Perda de carga do lado do casco ===============================================
        delta_Ps = delta_Pc + delta_Pw + delta_Pe       #   Perda de carga lado do casco excluindo os bocais


if __name__ == "__main__":
    a = CascoTubo()
    
