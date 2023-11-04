
import thermo
import math
import sqlite3
from dataBase.constants import*
from dataBase.comandos_sql import*

# TODO -> Rever tipos de arranjos dos tubos por tabelas da norma;
# TODO -> Update - arredondar valores das tabelas
# TODO -> rever se tabelas tem todos tipos de arranjo e se arranjos estão com nomes corretos
# TODO -> consertar tabela delta_sb, pode ter valores de Dn que não se enquadram em nenhuma condição
# TODO -> Ver se é possível aplica order By em alguns filtros

POL2M = 0.0254
class CascoTubo:
    def __init__(self, cp_quente:float, cp_frio:float, T1:float, T2:float, t1:float, t2:float, wq:float, wf:float, num_casco:int):
        self.T1 = T1
        self.T2 = T2
        self.t1 = t1
        self.t2 = t2
        self.wf = wf
        self.wq = wq
        self.cp_quente = cp_quente
        self.cp_frio = cp_frio
        self.num_casco = num_casco
        
        self.balaco_de_energia()
        self.diferenca_temp_deltaT()

    def balaco_de_energia(self):
        
        # TODO -> Fazer código calcular cp_quente e cp_frio, No caso atual só pode faltar um dado e não pode ser cp_frio e cp_quente
        # TODO -> Lógica errada, esse caso pega se tiver 2 valores faltando
        if None in (self.t1, self.t2, self.wq) and  None in (self.T1, self.T2, self.wf):
            print("Não tem nenhum valor.")

        elif None in (self.T1, self.T2, self.wq):
            self.q = self.wf * self.cp_frio * (self.t2 - self.t1)

            if self.T1 is None:
                self.T1 = self.T2 + self.q/(self.wq * self.cp_quente)
            elif self.T2 is None:
                self.T2 = self.T1 - self.q/(self.wq * self.cp_quente)
            else:
                self.wq = self.q/(self.cp_quente * (self.T1 - self.T2 ))

        elif None in (self.t1, self.t2, self.wf):
            self.q = self.wq * self.cp_quente * (self.T1 - self.T2)
        
            if self.t1 is None:
                self.t1 = self.t2 - self.q/(self.wf * self.cp_frio)
            elif self.t2 is None:
                self.t2 = self.t1 + self.q/(self.wf * self.cp_frio)
            else:
                self.wf = self.q/(self.cp_frio * (self.t2 - self.t1 ))
        

        else: # Se tiver todos os parâmetros
            try:
                self.q = self.wf * self.cp_frio * (self.t2 - self.t1) 
            except Exception as erro:
                print("Não há valores suficientes")
        
        return self.q

    def diferenca_temp_deltaT(self):

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

                num = self.S*2**0.5
                a = (2 - self.S*(2 - 2**0.5))
                b = (2 - self.S*(2 + 2**0.5))
                self.F = num/((1 - self.S)*math.log(a/b))   
            
            else:
                self.S = self.S/(self.S - self.S*self.num_casco + self.num_casco)
                
                num = self.S*2**0.5
                a = (2 - self.S*(2 - 2**0.5))
                b = (2 - self.S*(2 + 2**0.5))
                self.F = num/((1 - self.S)*math.log(a/b))

        calculo_diferenca_log_MLDT()
        calculo_R_S()
        calculo_F()
        self.deltaT = self.mldt*self.F
        

    def filtro_tubos(self, n, Ds, de, a_tubos, passo_pol: str):
            """ ## Descrição:
                    - Filtra da tabela de nº de tubos de fabricantes o valor diâmetro do feixe, nº de passagens no tubo e nº de tubos
                ## Args:
                    - n: número de passes no tubos
                    - Ds: diâmetro interno do casco 
                    - de: diâmetro externo do tubo (m) [1' ou 3/4']
                    - a_tubos: arranjo dos tubos ["triangular", "quadrado", "rodado"]
                    - passo_pol: [1, 1 1/4, 15/16 ]
                ## Return
                    - Nt: nº de tubos
                    - Dotl: diâmetor do feixe
            """
            self.n = n
            self.Ds = Ds
            self.de = de
            self.a_tubos = a_tubos
            self.passo = passo_pol

            npt = ""
            if n == 1:
                npt = "Npt1"
            elif n == 2:
                npt = "Npt2"
            elif n == 4:
                npt = "Npt4"
            elif n == 6:
                npt = "Npt6"
            elif n == 8:
                npt = "Npt8"
            
            a_tubos = str(a_tubos) 
            passo = passo_pol

            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_NT = f"SELECT {npt} FROM Contagem_de_tubos WHERE arranjo = '{a_tubos}' AND Ds = {Ds} AND de_pol = {de} AND p_pol = {passo}"
            sql_Dotl = f"SELECT Dotl_m FROM Contagem_de_tubos WHERE arranjo = '{a_tubos}' AND Ds = {Ds} AND de_pol = {de} AND p_pol = {passo}"

            Nt = filtro_sqlite(cursor, sql_NT, True)
            Dotl = filtro_sqlite(cursor, sql_Dotl, True)

            if len(Nt) > 1 or len(Dotl) > 1:
                print(" ERRO: mais de uma correspondência para Nt e Dotl em filtro_tubos")
                return
            
            print("Dotl= ", Dotl[0])
            print("Nt= ", Nt[0])
            return [Nt[0], Dotl[0]]

    def area_projeto(self, Nt: int, de: float, L:float) -> float:
        """Cálculo da área de projeto

        Args:
            Nt (int): nº de tubos
            de (float): diâmetro externo do tubo 
            L (float): comprimento do trocador

        Returns:
            float: _description_
        """
        # TODO -> ver se é com de ou d
        # TODO -> Confirmar se não deveria multiplicar pelo número de passes
        A_proj = Nt * math.pi * de * L  
        print("A_proj= ", A_proj)
        return A_proj 

    def  coef_global_min(self, A_proj: float, delta_t: float, q: float) -> float:
        """Cálculo do coeficiente global mínimo

        Args:
            A_proj (float): área de projeto
            delta_t (float): diferença de temperatura no trocador, calculado com MLDT
            q (float): taxa de transferência de calor

        Returns:
            float: Coeficiente global minímo
        """
        Ud_min = q / (A_proj * delta_t)
        print("Ud_min= ", Ud_min)

        return Ud_min

    # Passo 4 -- Lado do Tubo
    
    def fluido_tubo(self):
        """
        Função para determinar qual o fluido do lado do tubo e qual do lado do casco
        """

    def conveccao_tubo(self, n, Nt, L, w_tubo: float, mi_t:float, rho_t: float,  fluido_t: str, t2_t: float, t1_t: float, de:float,  cp_t: float, k_t:float, d:float):
        # TODO -> Rever cálculo de d (diâmetro interno)
        # TODO -> Temperatura média não pode ser negativa, no caso do fluido quente aqui seria negativo
        # TODO -> verificar corretamente de onde é k_t
                
        print(d)
        n = n
        Nt = Nt
        w = w_tubo       # Vazão mássica fluído do lado do tubo 
        mi = mi_t
        rho = rho_t
        tipo_fluido = fluido_t
        cp = cp_t
        k = k_t
        L_t = L
        de = de #   Diâmetro externo do tubo

        at_ = math.pi*(d**2)/4   #   área escoamento tubo -- unidade
        at = Nt*at_/n           #   área de escoamento tubo
        Gt = w/at               #   vazão mássica por unidade de área
        Re_t = Gt*d/mi          #   Nº de Re
        print(d, Gt, mi)
        print(Re_t)
        v_t = Gt/rho            #   Velocidade escoamento lado do tubo

        if tipo_fluido == "water":
            #   Como a água é um fluido normalmente incrustante não se utilizam velocidades de escoamento inferiores a 1 m/s. Sugere-se ler a parte referente a “Trocadores usando água” , p. 115, do Kern.
            t = (t2_t - t1_t)/2 #   Temperatura média do fluído
            hi = 1055 * (1.352 + 0.0198 * t) * v_t**0.8 / d**0.2   #   (3.24b)

        elif Re_t > 10000:
            
            # Como não temos tw
            a = 1   #   (mi/miw) ** 0.14

            Nu = 0.027 * (d*Gt/mi)**0.8 * (cp*mi/k)**(1/3) * a
            hi = Nu * k/d
        
        elif Re_t < 2100:
            hi = 3.66*k/d

        elif 2100 <= Re_t <=10000:
            # TODO -> rever
            a = 0.1 *((d * Gt / mi) ** (2 / 3) - 125) * (cp * mi / k) ** 0.495
            b = math.exp(-0.0225 * (math.log(cp * mi / k)) ** 2)
            
            # Como não temos tw
            a_ = 1   #   (mi/miw) ** 0.14

            c = a_ * (1 + d/L_t) ** (2/3)  #   Verificar esse L

            Nu = a * b * c
            hi = Nu * k / d
        
        hio = hi * d / de
        
        

        return [at, Gt, Re_t, v_t, hi, hio, d]


    def caract_chicana(self):
        """ ## Descrição: 
                - Define as características das chicanas, caso não tenha sido definida previamente. Aleatoriza o valor de acordo com recomendações da norma.
            ## Return:
                - ls: Espaçamento das chicanas  
                - lc: Corte das chicanas
        """

    def conveccao_casco(self, k:float, cp:float, mi:float, w:float, de, Nt, Dotl, Ds, a_tubos, L_t, ls, lc, p, classe: int):
        """ ## Descrição:
                - Função que faz o cálculo da convecção no casco.
            ## Args:
                - k: condutividade térmica fluido que escoa no casco
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
                - classe: classe de pressão [psi] 
        """
        # TODO -> verificar se é de mesmo 
        # TODO -> tabela de contagem de tubos está errada na coluna a_tubos (ARRUMAR) 
        # TODO -> analisar onde usa Dc ou Ds
        # TODO -> analisar cálculo do diâmetro do casco
        # TODO -> rever tabela dos passos
        # TODO -> rever filtro li, lo - modo de filtrar - ver tabela outras referencias
        
        def tabela_passo(a_tubos, de, p):
            """ ## Descrrição:
                    - Filtra da tabela o valor dos passos em [m].
                ## Args:
                    - a_tubos: arranjo dos tubos
                    - de: diâmetro externo do tubo 
            """
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f" SELECT * FROM Passos_tubos WHERE p = {p} AND  a_tubos = '{a_tubos}' ORDER BY ABS(de - {de}) LIMIT 1; "
            linha = filtro_sqlite(cursor, sql_linha)
            
            if len(linha) > 1 or len(linha) == 0:
                print("Erro: correspondência na tabela de passos")
                return

            print(linha)
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
            
            if len(linha) > 1 or  len(linha) == 0:
                print("Erro: correspondência na tabela de constantes a")
                return
            
            a4 = linha[0][-1]
            a3 = linha[0][-2]
            a2 = linha[0][-3]
            a1 = linha[0][-4]
            

            a = a3 / (1 + 0.14 * Res ** a4)


            ji = a1 *((1.33 / (p / de)) ** a )* Res ** a2

            return ji

        
        def tabela_delta_sb(Dn):
            """ ## Descrição:
                    - Filtra delta_sb [m]
                ## Args:
                    - Dn: diâmetro nominal do caso
                Return:
                    -delta_sb: arbetura diametral casco chicana
            """
            # TODO -> Fazer tabela e terminar
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f"SELECT delta_sb FROM Delta_sb WHERE D_nominal_min <= {Dn} AND D_nominal_max >= {Dn} "
            linha = filtro_sqlite(cursor, sql_linha, True)
            
            if len(linha) > 1 or len(linha) == 0:
                print("Erro: correspondência na tabela de constantes a")
                return
            
            print(linha)
            delta_sb = linha[0]
            return delta_sb

        def diametro_bocal(Dc):
            """ ## Descrição:
                Cálculo o diâmetro do casco e filtra da tabela diâmetro do Bocal
                ## Args:
                    - Dc: diâmetro do casco
                ## Return:
                    - d_bocal: diâmetro do bocal [m]
                    - Dc:   diâmetro do casco    [m]
            """
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f"SELECT d_bocal FROM Diametro_bocal WHERE D_casco_min <= {Dc} AND D_casco_max >= {Dc} "
            linha = filtro_sqlite(cursor, sql_linha, True)

            if len(linha) > 1 :
                print("Erro: mais de uma correspondência na tabela de constantes a")
                return
            
            d_bocal = linha[0]
            
            return d_bocal

        def li_lo_tabela(Dc, classe):
            """ ## Descrição:
                Filtra da tabela a li e lo com base no diâmetro do casco e classe de pressão [Pesquisar mais sobre isso]
                ## Args:
                    - Ds: diâmetro do casco
                    - classe: classe de pressão
                ## Return:
                    - li: [m]
                    - lo: [m]
            """
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f"SELECT * FROM li_lo WHERE Classe_pressao_psi = {classe} ORDER BY ABS(D_casco - {Dc}) LIMIT 1 "
            linha = filtro_sqlite(cursor, sql_linha)

            if len(linha) > 1 :
                print("Erro: mais de uma correspondência na tabela de constantes a")
                return
            
            lo = linha[0][-1]
            li = linha[0][-2]

            return li, lo
            

        #================= Cálculo para feixe de tubos ideal =====================
        pn, pp = tabela_passo(a_tubos, de, p)

        
        if a_tubos == "triangular":
            Sm = ls * (Ds - Dotl + (Dotl - de) / p * (p - de))
        else:
            Sm = ls * (Ds - Dotl + (Dotl - de) / pn * (p - de))

        Res = de * w / (mi * Sm)
        
        if a_tubos == "triangular":
            angulo_tubos = 30
        elif a_tubos == "quadrado":
            angulo_tubos = 90
        elif a_tubos == "rodado":
            angulo_tubos = 45


        ji = fator_ji(Res, de, angulo_tubos, p)

        h_ideal = ji * cp * w/Sm * ((k/(cp * mi))**(2/3)) 

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

        if  folga > 1.5 * POL2M or (folga > 0.5 * POL2M and Sbp/(Sm -Sbp) > 0.1 * POL2M) :
            Nss = Nc // 5       #   Nº de pares de tiras selantes. Costuma-se utilizar umq par de tiras selantes para cada 5 a 7 filas de tubos na seção de escoamento cruzado.
        else:
            Nss = 0

        jb = math.exp(-Cbh * Fbp * (1 - (2 * Nss / Nc) ** (1/3)))

        #================= Fator de correção para o gradiente adverso de temperatura (Jr) =====================
        
        jr_ = 1.51 / (Nc ** 0.18)
        
        if Res > 100:
            jr = 1
        elif Res <= 20:
            jr = jr_
        elif 20<= Res <100:
            jr = jr_ + ((20 - Res) / 80) * (jr_ - 1)
        
        #================= Fator de correção devido ao espaçamento desigual das chicanas na entrada e na saída (Js) =====================
        
        # TODO
        Dc = Ds + 2 * POL2M
        
        
        d_bocal = diametro_bocal(Dc)
        li, lo = li_lo_tabela(Dc, classe)

        lsi = li + d_bocal
        lso = lo + d_bocal

        if Res > 100:
            n = 0.6
        elif Res <= 100:
            n = 1/3
        
        lsi_ = lsi / ls
        lso_ = lso / ls

        Nb = (L_t - lsi - lso) / ls + 1

        Nb  = Nb // 1

        num = (Nb - 1) + (lsi_ ** (1 - n)) + (lso_ ** (1 - n))
        den = (Nb - 1) + (lsi_) + (lso_)

        js = num / den

        #   Cálculo coeficiente de transmissão de calor para o lado do casco
        hs = h_ideal * jc * jl * jb * jr * js

        print("Ds", Ds)
        print("Dc", Dc)

        return [pn, pp, Res, Sm, h_ideal, ji, jc, Fc, jl, Stb, delta_tb, Ssb, delta_sb, jb, Nc, Fbp, jr, lsi, lso, js, Nb, hs, li, lo, d_bocal], Nss, lsi_, lso_
    
    def calculo_temp_parede(self, Tmed, tmed, hs, hio, mi_t, mi_c, fluido_frio:bool, tipo_tubo:str):
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
                - tipo_tubo: tipo de fluido no tubo
            ## Return:
                - tw: temperatura da parede 
                - miw: Viscosidade do fluido avaliada na temperatura da parede
                - phi_t_tubo: valor do termo (mi / miw) ^ 0.14 para o tubo
                - phi_t_casco: valor do termo (mi / miw) ^ 0.14 para o casco
        """

        # TODO -> arrumar para cálculo das propriedades termodinâmicas
        Tc = Tmed    
        tc = tmed 

        if fluido_frio:
            tw = tc + hs/ (hio + hs) * (Tc - tc) 
        else:
            tw = tc + hio/(hio + hs) * (Tc - tc)
        
        print(tw)
        miw = self.propriedades_termodinamicas()

        phi_t_tubo = (mi_t / miw) ** 0.14
        phi_t_casco= (mi_c / miw) ** 0.14
        
        hs = hs * phi_t_casco

        if tipo_tubo != "water":
            hio = hio * phi_t_tubo

        return tw, miw, hs, hio

    def coef_global_limpo(self, hio, hs):
        """## Descrição:
            Cálcula o coeficiente global limpo com base nos cefientes de transmissão de calor cálculados  
        """

        Uc = hio * hs / (hio + hs)
        return Uc
    
    def excesso_area(self, Uc, Ud, Rd_verd, A_proj, delta_t, q):
        """## Descrição:
            Cálcula do fator de inscrustação e excesso da área de troca
        ## Args:
            - Uc: coeficiente global limpo
            - Ud: coeficiente mínimo
            - Rd_verd: fator de incrsutação verdadeiro (soma dos fatores de incrustação dos dois fluidos)
            - A_proje: área de projeto
            - delta_t: diferença de temperatura no trocador
            - q: taxa de transferência de calor no trocador
        
        ## Return:
            - Rd: fator de incrustação calculado
            - Ea: excesso de área de troca [%]
        """
        #   Rd calculados deve ser maior que verdadeiro
        Rd = (Uc - Ud) / (Uc * Ud)
        
        Ud_ = 1 / (1 / Uc + Rd_verd)

        A_nec = q / (Ud_ * delta_t)
        Ea = (A_proj - A_nec)/A_nec * 100

        return Rd, Ud_, A_nec, Ea


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

        return delta_PT

    def perda_carga_casco(self, Nb, mi, miw, de, Res, W, rho, Nc, Stb, Ssb, Sm, Nss, Fbp, p, pp, lc, Ds, Fc, Nt, ls, lsi_, lso_, a_tubo):
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
                - a_tubo: arranjo de tubos
            ## Return
                - delta_Ps: perda de carga do lado do casco   
        """
        def constantes_b(Res:float, angulo_tubo: int) -> list:
            """filtra constantes b

            Args:
                Res (float): nº de Re
                angulo_tubo (int): angulo do arranjo dos tubos

            Returns:
                list: lista [b1, b2, b3, b4]
            """
            cursor = conect_sqlite(DB_CONSTANTS_DIR)
            sql_linha = f"SELECT b1, b2, b3, b4 FROM Constantes_b WHERE angulo_tubo = {angulo_tubo} AND Re_min <= {Res} AND  Re_max > {Res};"
            linha = filtro_sqlite(cursor, sql_linha)

            if len(linha) > 1 :
                print("Erro: mais de uma correspondência na tabela de constantes a")
                return
            
            b1 = linha[0][0]
            b2 = linha[0][1]
            b3 = linha[0][2]
            b4 = linha[0][3]

            return [b1, b2, b3, b4]
        
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
        
        if a_tubo == "triangular":
            angulo_tubo = 30
        elif a_tubo == "quadrado":
            angulo_tubo = 90
        elif a_tubo == "rodado":
            angulo_tubo = 45
       

        b1, b2, b3, b4 = constantes_b(Res, angulo_tubo)
        b = b3 / (1 + 0.14 * Res ** b4)
        fi = b1 * (1.33 / (p / de)) ** b * (Res) ** b2      #   Fator de atrito para um feixe de tubos ideal
        delta_Pbi = (4 * fi * W **2 * Nc / (rho * Sm ** 2) ) # TODO -> implementar depois e verificar eq. (mi / miw) ** -0.14   #   Perda de carga para uma seção ideal de fluxo cruzado
        
        print("deltat_Pb1",delta_Pbi)
        
        delta_Pc = delta_Pbi * (Nb -1) * Rb * Rl
        
    
        #================= Perda de carga nas janelas ==============================================
        Swg_a = 1 - 2 * lc / Ds 
        Swg_b = (1-(Swg_a ** 2)) ** (1/2)
        Swg = ((Ds ** 2) / 4 ) * (math.acos(1 - 2 * lc / Ds) - Swg_a * Swg_b)      #   Área total da janela
        

        

        Swt = Nt / 8 * (1 - Fc) * math.pi * de ** 2     # Área ocupada pelos tubos na janela

        Sw = Swg - Swt      #   Área da seção de escoamento da janela
        
        print("Sw", Sw)

        Ncw = 0.8 * lc / pp     #   Nº de fileiras de tubos efetivamente cruzados em cada janela

        # TODO -> verificar isso, se arredonda pra baixo
        Ncw = Ncw // 1


        if Res >= 100:      #   Escoamento turbulento
            

            delta_Pwi = W ** 2 * (2 + 0.6 * Ncw) / (2 * Sm * Sw * rho)  #   Perda de carga em uma seção de janela ideal
        
        elif Res < 100:     #   Escoamento laminar
            theta_b = 2 * math.acos(1 - 2 * lc / Ds)        #   Ângulo de corte da chicana em radianos
            Dw = 4 * Sw / ((math.pi / 2) * Nt * (1 - Fc) * de + Ds * theta_b)       #   Diâmetro equivalente da janela

            delta_Pwi_a = 26 * mi * W / (rho * ((Sm * Sw) ** (1/2)))
            delta_Pwi_b = (Ncw / (p - de) + ls / (Dw ** 2))
            delta_Pwi_c = 2 * W ** 2 / (2 * Sm * Sw * rho)
            delta_Pwi = delta_Pwi_a * delta_Pwi_b + delta_Pwi_c
        
        print(Nb, delta_Pwi, Rl)
        delta_Pw = Nb * delta_Pwi * Rl

        #================== Perda de carga nas regiões de entrada e saída do casco delta_Pe ============

        if Res <= 100:
            n = 1
        elif Res > 100:
            n = 0.2
        
        # TODO-> conferir contas que envolve valores em pol
        print(n)
        print(lsi_)
        print(lso_)
        print(POL2M)

        Rs = (1 / 2) * (((lsi_ / POL2M) ** (n - 2)) + ((lso_/POL2M) ** (n-2)))      #   Fator de correção devido o espaçamento desigual das chicanas

        print("Rb", Rb)
        print("Rs", Rs)

        delta_Pe = 2 * delta_Pbi * (1 + Ncw / Nc) * Rb * Rs

        
        #================ Perda de carga do lado do casco ===============================================
        delta_Ps = delta_Pc + delta_Pw + delta_Pe       #   Perda de carga lado do casco excluindo os bocais

        return  delta_Pc, delta_Pw, delta_Pe, delta_Ps

if __name__ == "__main__":
    ...
