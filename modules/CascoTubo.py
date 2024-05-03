
import math
import sqlite3
from dataBase.constants import*
from dataBase.comandos_sql import*
import logging
import os
import json


# TODO -> Rever tipos de arranjos dos tubos por tabelas da norma;
# TODO -> Update - arredondar valores das tabelas
# TODO -> rever se tabelas tem todos tipos de arranjo e se arranjos estão com nomes corretos
# TODO -> consertar tabela delta_sb, pode ter valores de Dn que não se enquadram em nenhuma condição
# TODO -> Ver se é possível aplica order By em alguns filtros

POL2M = 0.0254
class CascoTubo:
    def __init__(self, *args, **kwargs):

        self.T1 = kwargs["T1"] + 273.15
        self.T2 = kwargs["T2"] + 273.15
        self.t1 = kwargs["t1"] + 273.15
        self.t2 = kwargs["t2"] + 273.15
        self.wf = kwargs["wf"]
        self.wq = kwargs["wq"]
        self.cp_quente = kwargs["cp_quente"]
        self.cp_frio = kwargs["cp_frio"]
        self.num_casco = kwargs["num_casco"]
        self.rho_q = kwargs["rho_q"]
        self.rho_f = kwargs["rho_f"]
        self.mi_f = kwargs["mi_f"]
        self.mi_q = kwargs["mi_q"]
        self.k_q = kwargs["k_q"]
        self.k_f = kwargs["k_f"]
        self.tipo_q = kwargs["tipo_q"]
        self.tipo_f = kwargs["tipo_f"]
        self.Rd_f = kwargs["Rd_f"]
        self.Rd_q = kwargs["Rd_q"]
  
        self._balaco_de_energia()
        self._diferenca_temp_deltaT()
    
    def __setattr__(self, __name: str, __value) -> None:
        logging.debug(f"  {__name}: {__value}")
        super().__setattr__(__name, __value)

    def _balaco_de_energia(self):
        
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

    def _diferenca_temp_deltaT(self):

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
        

    def filtro_tubos(self, n, Ds, de_pol, a_tubos, passo_pol: str) -> int:
        """_summary_

        Args:
            n (_type_): _description_
            Ds (_type_): _description_
            de_pol (_type_): _description_
            a_tubos (_type_): _description_
            passo_pol (str): _description_

        Returns:
            int: Nº de tubos
        """
        self.n = n
        self.Ds = Ds
        self.a_tubos = a_tubos

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
        sql_NT =f""" 
            SELECT {npt} 
            FROM Contagem_de_tubos 
            WHERE arranjo = '{a_tubos}' AND de_pol = {de_pol} AND p_pol = {passo}
            ORDER BY ABS(Ds - {Ds})
            LIMIT 1

            """ 
        
        sql_Dotl = f"""  
            SELECT Dotl 
            FROM Contagem_de_tubos 
            WHERE arranjo = '{a_tubos}' AND de_pol = {de_pol} AND p_pol = {passo}
            ORDER BY ABS(Ds - {Ds})
            LIMIT 1
        
        """
        
        Nt = filtro_sqlite(cursor, sql_NT, True)
        Dotl = filtro_sqlite(cursor, sql_Dotl, True)

        if len(Nt) > 1 or len(Dotl) > 1:
            print(" ERRO: mais de uma correspondência para Nt e Dotl em filtro_tubos")
            return
        
        self.de = de_pol * POL2M
        self.passo = passo_pol * POL2M
        self.Nt = Nt[0]
        self.Dotl = Dotl[0]

        return self.Nt

    def area_projeto(self, L:float) -> float:
        """Cálculo da área de projeto

        Args: 
            L (float): comprimento do trocador
        """
        # TODO -> ver se é com de ou d
        # TODO -> Confirmar se não deveria multiplicar pelo número de passes
        Nt = self.Nt
        de = self.de
        A_proj = Nt * math.pi * de * L  

        self.L = L
        self.A_proj = A_proj

    def  coef_global_min(self) -> float:
        """Cálculo do coeficiente global mínimo
        """
        q = self.q
        delta_t = self.deltaT
        A_proj = self.A_proj
        Ud_min = q / (A_proj * delta_t)

        self.Ud_min = Ud_min

    # Passo 4 -- Lado do Tubo
    def diametro_interno_tubo(self, espe:float):
        """Cálcula o diâmetro interno do tubo com base na espessura passada

        Args:
            expe (float): espessura dos tubos em [m]
        """

        
        self.di = self.de - 2*espe
        self.tube_thickness = espe
        


    def conveccao_tubo(self, fluido_tubo_quente:bool):
        """Faz o cálculo da convecção no lado do tubo

        Args:
            fluido_tubo_quente (bool): True para fluido quente no lado do tubo, False para o contrário

        """
        
        # TODO -> Rever cálculo de d (diâmetro interno)
        # TODO -> Temperatura média não pode ser negativa, no caso do fluido quente aqui seria negativo
        # TODO -> verificar corretamente de onde é k_t
                
        n = self.n
        Nt = self.Nt
        L = self.L
        de = self.de
        di = self.di

        if fluido_tubo_quente:
            w = self.wq
            mi = self.mi_q
            rho = self.rho_q
            tipo_fluido = self.tipo_q
            t2_t = self.T1
            t1_t = self.T2
            cp = self.cp_quente
            k = self.k_q

            self.fluido_casco = "frio"

        else:
            w = self.wf
            mi = self.mi_f
            rho = self.rho_f
            tipo_fluido = self.tipo_f
            t2_t = self.t2
            t1_t = self.t1
            cp = self.cp_frio
            k = self.k_f

            self.fluido_casco = "quente"

        L_t = L

        at_ = math.pi*(di**2)/4   #   área escoamento tubo -- unidade
        at = Nt*at_/n           #   área de escoamento tubo
        Gt = w/at               #   vazão mássica por unidade de área
        Re_t = Gt*di/mi          #   Nº de Re

        v_t = Gt/rho            #   Velocidade escoamento lado do tubo

        if tipo_fluido == "water":
            #   Como a água é um fluido normalmente incrustante não se utilizam velocidades de escoamento inferiores a 1 m/s. Sugere-se ler a parte referente a “Trocadores usando água” , p. 115, do Kern.
            t = (t2_t - t1_t)/2 #   Temperatura média do fluído
            hi = 1055 * (1.352 + 0.0198 * t) * v_t**0.8 / di**0.2   #   (3.24b)

        elif Re_t > 10000:
            
            # Como não temos tw
            a = 1   #   (mi/miw) ** 0.14

            Nu = 0.027 * (di*Gt/mi)**0.8 * (cp*mi/k)**(1/3) * a
            hi = Nu * k/di
        
        elif Re_t < 2100:
            hi = 3.66*k/di

        elif 2100 <= Re_t <=10000:
            # TODO -> rever
            a = 0.1 *((di * Gt / mi) ** (2 / 3) - 125) * (cp * mi / k) ** 0.495
            b = math.exp(-0.0225 * (math.log(cp * mi / k)) ** 2)
            
            # Como não temos tw
            a_ = 1   #   (mi/miw) ** 0.14

            c = a_ * (1 + di/L_t) ** (2/3)  #   Verificar esse L

            Nu = a * b * c
            hi = Nu * k / di
        
        hio = hi * di / de
        
        try:
            self.Nu_t = Nu
        except:
            ...
        self.hot_fluid_tube = fluido_tubo_quente
        self.area_one_tube = at_
        self.area_tube = at
        self.Gt = Gt
        self.Re_t = Re_t
        self.tube_velocity = v_t
        self.hi = hi
        self.hio = hio


    def caract_chicana(self, grupo_de_material:int) -> list:
        """Defini os limites máximos e mínimos para o espaçamento das chicanas (ls) e o corte (lc)

        Args:
            grupo_de_material (int): de acordo com TEMA. 2 para Al, Cu, Ti.

        Returns:
            list: limites_ls(list), limites_lc(list)
        """
        espacamento_min = 1/5 *self.Ds
        
        if espacamento_min < (2*POL2M):
            espacamento_min = 2*POL2M

        espacamento_max = 74 * self.de ** 0.75

        if grupo_de_material ==2:
            espacamento_max =espacamento_max * 0.88

        limites_ls = [espacamento_min, espacamento_max] 

        min_lc = 0.15 * self.Ds
        max_lc = 0.4 * self.Ds

        limite_lc = [min_lc, max_lc]

        return limites_ls, limite_lc

    
    def diametro_casco(self, espessura:float):
        """Determinação do diâmetro externo do casco.

        Args:
            espessura (float): espessura do casco em [m]
        """
        
        Dc = self.Ds + 2 * espessura
        
        self.shell_thickness = espessura
        self.Dc = Dc



    def conveccao_casco(self, ls, lc, classe: int):
        """ ## Descrição:
                - Função que faz o cálculo da convecção no casco.
            ## Args:
                - ls: Espaçamento das chicanas
                - lc: Corte das chicanas  
                - classe: classe de pressão (150 ou 600 psi)[psi] 
        """
        de = self.de
        Nt = self.Nt
        Dotl = self.Dotl
        Ds = self.Ds
        a_tubos = self.a_tubos
        L = self.L
        p = self.passo
        self.classe = classe
        Dc = self.Dc

        self.lc = lc
        self.ls = ls

        if self.fluido_casco == "quente":
            k = self.k_q
            cp = self.cp_quente
            mi = self.mi_q
            w = self.wq
        elif self.fluido_casco == "frio":
            k = self.k_f
            cp = self.cp_frio
            mi = self.mi_f
            w = self.wf

        # TODO -> verificar se é de mesmo 
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
                    - classe: classe de pressão (150 ou 600 psi)
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
        self.pp = pp
        self.pn = pn
        
        if a_tubos == "triangular":
            Sm = ls * (Ds - Dotl + (Dotl - de) / p * (p - de))
        else:
            Sm = ls * (Ds - Dotl + (Dotl - de) / pn * (p - de))
        print("Sm", Sm)
        self.Sm = Sm

        Res = de * w / (mi * Sm)
        
        self.Res =Res

        if a_tubos == "triangular":
            angulo_tubos = 30
        elif a_tubos == "quadrado":
            angulo_tubos = 90
        elif a_tubos == "rodado":
            angulo_tubos = 45


        ji = fator_ji(Res, de, angulo_tubos, p)
        self.ji = ji

        h_ideal = ji * cp * w/Sm * ((k/(cp * mi))**(2/3)) 
        self.h_ideal = h_ideal

        #================= Fator de correção para os efeitos da configuração da chicana =====================

        Fc = 1/math.pi * (math.pi + 2 * (Ds - 2 * lc) / Dotl * math.sin( math.acos((Ds - 2 * lc) / Dotl)) - 2 * math.acos((Ds - 2 * lc) / Dotl))    #   Nº tubos seção de escoamento cruzado
        
        jc = Fc + 0.54 * (1 - Fc) ** 0.345
        
        self.Fc = Fc
        self.jc = jc
        #================= Fator de correção para os efeitos dos vazamentos da chicana =====================
        
        delta_sb  = tabela_delta_sb(Ds)  #   Folga diametral casco chicana
        Ssb = Ds * delta_sb / 2 * (math.pi - math.acos(1 - 2 * lc / Ds))    #   Área de seção de vazamento casco chicana 
        delta_tb = 7.938 * 10 ** - 4       #    [m] - Folga diametral tubo chicana- TEMA - Classe R - Verificar valor
        Stb = math.pi * de * delta_tb * Nt * (Fc + 1) / 4   #   Área da seção de vazamento tubo-chicana
        alpha = 0.44 * (1 - Ssb / (Ssb + Stb))
        jl = alpha + (1 - alpha) * math.exp(-2.2 * (Stb + Ssb) / Sm)
        
        self.delta_sb = delta_sb
        self.Ssb = Ssb
        self.delta_tb = delta_tb
        self.Stb =Stb
        self.jl = jl

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

        self.Fbp = Fbp
        self.Sbp = Sbp
        self.Nc = Nc
        self.Nss = Nss
        self.jb = jb

        #================= Fator de correção para o gradiente adverso de temperatura (Jr) =====================
        
        jr_ = 1.51 / (Nc ** 0.18)
        
        if Res > 100:
            jr = 1
        elif Res <= 20:
            jr = jr_
        elif 20<= Res <100:
            jr = jr_ + ((20 - Res) / 80) * (jr_ - 1)
        
        self.jr = jr
        #================= Fator de correção devido ao espaçamento desigual das chicanas na entrada e na saída (Js) =====================
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

        Nb = (L - lsi - lso) / ls + 1
        Nb  = Nb // 1
        self.Nb = Nb

        num = (Nb - 1) + (lsi_ ** (1 - n)) + (lso_ ** (1 - n))
        den = (Nb - 1) + (lsi_) + (lso_)

        js = num / den

        self.d_bocal = d_bocal
        self.li = li
        self.lo = lo
        self.lsi = lsi
        self.lso = lso
        self.lsi_ = lsi_
        self.lso_ = lso_
        self.js = js
        #   Cálculo coeficiente de transmissão de calor para o lado do casco
        hs = h_ideal * jc * jl * jb * jr * js
        
        self.hs = hs
    
    def calculo_temp_parede(self):
        """ ## Descrição:
            Cálcula a temperatura da parede.
            ## Args
                - fluido_frio:bool Se o fluído frio estiver no interior do tubo - True
        """

        if self.fluido_casco == "quente":
            fluido_frio = True
        elif self.fluido_casco == "frio":
            fluido_frio = False

        hs = self.hs
        hio = self.hio
        
        Tc = (self.T1 + self.T2)/2
        tc = (self.t2 + self.t1)/2
        
        print(Tc)
        print(tc)

        if fluido_frio:
            tw = tc + hs/ (hio + hs) * (Tc - tc) 
        else:
            tw = tc + hio/(hio + hs) * (Tc - tc)
        
        self.tw = tw

    def correcao_temp_parede(self):
        """Corrige hs e hio de acordo com temperatura da parede
        """
        
        # TODO -> arrumar para cálculo das propriedades termodinâmicas
        miw = self.propriedades_termodinamicas()
        
        if self.fluido_casco == "quente":
            mi_c = self.mi_q
            mi_t = self.mi_f
            tipo_tubo = self.tipo_f
        elif self.fluido_casco == "frio":
            mi_c = self.mi_f
            mi_t = self.mi_q
            tipo_tubo = self.tipo_q

        phi_t_tubo = (mi_t / miw) ** 0.14
        phi_t_casco= (mi_c / miw) ** 0.14
        
        hs = hs * phi_t_casco

        if tipo_tubo != "water":
            hio = hio * phi_t_tubo

        self.phi_t_tubo = phi_t_tubo
        self.phi_t_casco = phi_t_casco
        self.miw = miw
        self.hio = hio
        self.hs = hs

    def coef_global_limpo(self):
        """ Cálcula o coeficiente global limpo com base nos cefientes de transmissão de calor cálculados  
        """
        hio = self.hio
        hs = self.hs
        Uc = hio * hs / (hio + hs)
        
        self.Uc = Uc
    
    def excesso_area(self):
        """## Descrição:
            Cálcula do fator de inscrustação e excesso da área de troca
        """
        #   Rd calculados deve ser maior que verdadeiro
        self.Rd_verd = self.Rd_f + self.Rd_q
        Rd_verd = self.Rd_verd
        Ud = self.Ud_min
        Uc = self.Uc
        delta_t = self.deltaT
        q = self.q
        A_proj = self.A_proj

        Rd = (Uc - Ud) / (Uc * Ud)
        
        Ud_ = 1 / (1 / Uc + Rd_verd)

        A_nec = q / (Ud_ * delta_t)
        Ea = (A_proj - A_nec)/A_nec * 100

        self.Rd_calc = Rd
        self.A_nec = A_nec
        self.Ea = Ea
        self.Ud = Ud_

    def perda_carga_tubo(self, phi_t = 1):
        """ ## Descrição:
            - Cálculo da perda de carga do lado do tubo.
            ## Args:
                - phi_t: termo (mi/miw) ^ 0.14 para lado do tubo
        """
        Re_t = self.Re_t
        di = self.di
        G_t = self.Gt
        L = self.L
        n = self.n
        v = self.tube_velocity

        if self.fluido_casco == "quente":
            rho = self.rho_f
        elif self.fluido_casco == "frio":
            rho = self.rho_q

        delta_Pr = (4 * n * rho * v ** 2) / 2       #   Perda de carga de retorno 

        f = (1.58 * math.log(Re_t) - 3.28) ** -2    #   Fator de atrito de Fanning

        delta_Pt = (4 * f * G_t ** 2 * L * n) / (di * 2 * rho * phi_t) 

        delta_PT = delta_Pt + delta_Pr

        self.delta_Pr = delta_Pr
        self.delta_Pt = delta_Pt
        self.delta_PT = delta_PT
        

    def perda_carga_casco(self):
        """ ## Descrição:
            - Cálculo da perda de carga do lado do caso.
            ## Args:
                - Fc: Nº tubos seção de escoamento cruzado
                - Nt: Nº de tubos
                - ls: espaçamento das chicanas
                - lsi_: razão entre espaçamento da chicana de entrada e espaçamento das chicanas
                - lso_: razão entre espaçamento da chicana de saída e espaçamento das chicanas
                - a_tubo: arranjo de tubos
            ## Return
                - delta_Ps: perda de carga do lado do casco   
        """
        #  TODO -> correção miw
        Nb = self.Nb
        de = self.de
        Res = self.Res
        Nc = self.Nc
        Stb = self.Stb
        Ssb = self.Ssb
        Sm = self.Sm
        Nss = self.Nss
        Fbp = self.Fbp
        p = self.passo
        pp = self.pp
        lc = self.lc
        Ds = self.Ds
        Fc = self.Fc
        Nt = self.Nt
        ls = self.ls
        lsi_ = self.lsi_
        lso_ = self.lso_
        a_tubo = self.a_tubos



        if self.fluido_casco == "quente":
            mi = self.mi_q
            W = self.wq
            rho = self.rho_q
        elif self.fluido_casco == "frio":
            mi = self.mi_f
            W = self.wf
            rho = self.rho_f


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
        self.Swg= Swg

        

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

        self.delta_Ps = delta_Ps
        self.delta_Pw = delta_Pw
        self.delta_Pe = delta_Pe
        self.delta_Pc = delta_Pc

if __name__ == "__main__":
    str_dados = ""
    with open("public\\json\\comparacoes.json", "r", encoding="utf-8", ) as file:
        str_dados = file.read()

    dados = json.loads(str_dados)["comp_5"]

    a = CascoTubo(**dados["input"])
    
    a.filtro_tubos(dados["n"], dados["Ds"], dados["de_pol"], dados["a_tubos"], dados["passo_pol"])
    a.Nt = 36
    a.area_projeto(dados["L"])
    # a.q = a.q * 1.1
    a.coef_global_min()

    a.diametro_interno_tubo(dados["tube_thickness"])
    a.conveccao_tubo(dados["hot_fluid_tube"])

    # a.caract_chicana(1)

    # a.diametro_casco(dados["shell_thickness"])
    

    




