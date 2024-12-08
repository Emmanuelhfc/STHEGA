
import math
import logging
import json
from API.models import *
from django.db.models import F, Value
from django.db.models.functions import Abs

class TubeCountError(Exception):
    """Exceção personalizada para erros relacionados à contagem de tubos."""
    def __init__(self, message="O número de tubos (Nt) é zero."):
        self.message = message
        super().__init__(self.message)

# TODO -> Rever tipos de arranjos dos tubos por tabelas da norma;
# TODO -> Update - arredondar valores das tabelas
# TODO -> rever se tabelas tem todos tipos de arranjo e se arranjos estão com nomes corretos
# TODO -> consertar tabela delta_sb, pode ter valores de Dn que não se enquadram em nenhuma condição
# TODO -> Ver se é possível aplica order By em alguns filtros

POL2M = 0.0254

logger = logging.getLogger('API')
class CascoTubo:
    def __init__(self, input: InputsShellAndTube, *args, **kwargs, ):

        self.T1 = input.T1_hot
        self.T2 = input.T2_hot 
        self.t1 = input.t1_cold 
        self.t2 = input.t2_cold
        self.wf = input.wf
        self.wq = input.wq
        self.cp_quente = input.cp_quente
        self.cp_frio = input.cp_frio
        self.num_casco = input.casco_passagens
        self.rho_q = input.rho_q
        self.rho_f = input.rho_f
        self.mi_f = input.mi_f
        self.mi_q = input.mi_q
        self.k_q = input.k_q
        self.k_f = input.k_f
        self.tipo_q = input.tipo_q
        self.tipo_f = input.tipo_f
        self.Rd_f = input.Rd_f
        self.Rd_q = input.Rd_q
        self.di:TubeInternDiameter = input.di
        self.de:TubeDiameter = input.di.tube_diameter
        self.pitch:Pitch = input.pitch
        self.layout:Layout = input.pitch.layout
        self.n = input.n
        self.Ds_inch = input.Ds_inch
        self.L = input.L
        self.shell_fluid = input.shell_fluid
        self.ls_percent = input.ls_percent
        self.lc_percent = input.lc_percent
        self.tube_material:TubeMaterial = input.tube_material
        self.shell_thickness_meters = input.shell_thickness_meters
        self.pressure_class = input.pressure_class
        self.perda_carga_admissivel_casco = input.perda_carga_admissivel_casco
        self.perda_carga_admissivel_tubo = input.perda_carga_admissivel_tubo

        self._balaco_de_energia()
        self._diferenca_temp_deltaT()
    
    # def __setattr__(self, __name: str, __value) -> None:
    #     logging.debug(f"  {__name}: {__value}")
    #     super().__setattr__(__name, __value)


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


            # logger.debug(f'({self.T1} - {self.t2})-({self.T2} - {self.t1})')
            # logger.debug(f'ln(({self.T1} - {self.t2})/({self.T2} - {self.t1})')
        
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


    def filtro_tubos(self) -> int:
        tube_count = TubeCount.objects.filter(
            de=self.de,
            pitch=self.pitch,
            layout=self.layout,
            Ds_inch = self.Ds_inch
        ).first()
                                                   
        self.Ds = tube_count.Ds_meters

        match self.n:
            case 1:
                Nt = tube_count.n1
            case 2:
                Nt = tube_count.n2
            case 4:
                Nt = tube_count.n4
            case 6:
                Nt = tube_count.n6
            case 8:
                Nt = tube_count.n8

        self.Nt = Nt

        if self.Nt == 0:
            raise TubeCountError("O número de tubos (Nt) é zero.")
        self.Dotl = tube_count.Dotl_meters
        
        return self.Nt

    def area_projeto(self) -> float:
        """Cálculo da área de projeto

        Args: 
            L (float): comprimento do trocador
        """
        # TODO -> ver se é com de ou d
        # TODO -> Confirmar se não deveria multiplicar pelo número de passes
        Nt = self.Nt
        de = self.de.diameter_meters

        A_proj = Nt * math.pi * de * self.L  
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
    def conveccao_tubo(self):
        """Faz o cálculo da convecção no lado do tubo
        """
        
        # TODO -> Rever cálculo de d (diâmetro interno)
        # TODO -> Temperatura média não pode ser negativa, no caso do fluido quente aqui seria negativo
        # TODO -> verificar corretamente de onde é k_t
                
        n = self.n
        Nt = self.Nt
        L = self.L
        de = self.de.diameter_meters
        di = self.di.intern_diameter_meters
        
        # Fluido quente no lado do tubo
        if self.shell_fluid == "cold":
            w = self.wq
            mi = self.mi_q
            rho = self.rho_q
            tipo_fluido = self.tipo_q
            t2_t = self.T1
            t1_t = self.T2
            cp = self.cp_quente
            k = self.k_q

        else:
            w = self.wf
            mi = self.mi_f
            rho = self.rho_f
            tipo_fluido = self.tipo_f
            t2_t = self.t2
            t1_t = self.t1
            cp = self.cp_frio
            k = self.k_f


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

            Nu = 0.027 * (Re_t)**0.8 * (cp*mi/k)**(1/3) * a
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

        self.area_one_tube = at_
        self.area_tube = at
        self.Gt = Gt
        self.Re_t = Re_t
        self.tube_velocity = v_t
        self.hi = hi
        self.hio = hio

    def _espacamento_defletor(self):

        ls = self.Ds * float(self.ls_percent)

        espacamento_min = 1/5 *self.Ds
        
        if espacamento_min < (2*POL2M):
            espacamento_min = 2*POL2M

        espacamento_max = 74 * (self.de.diameter_inch ** 0.75)

        if self.tube_material.group == 2:
            espacamento_max = espacamento_max * 0.88
        
        espacamento_max = espacamento_max * POL2M

        if ls < espacamento_min:
            ls = espacamento_min

        elif ls > espacamento_max:
            ls = espacamento_max

        self.min_ls = espacamento_max
        self.max_ls = espacamento_min
        return ls

    def _corte_defletor(self):
        return float(self.lc_percent) * self.Ds

    
    def _diametro_externo_casco(self):
        """Determinação do diâmetro externo do casco.

        Args:
            espessura (float): espessura do casco em [m]
        """
        
        Dc = self.Ds + 2 * self.shell_thickness_meters
        return Dc

    

    def _tabela_folga_diametral_casco_defletor(self):
        """ ## Descrição:
                - Filtra delta_sb [m]
            ## Args:
                - Dn: diâmetro nominal do caso
            Return:
                -delta_sb: arbetura diametral casco chicana
        """
        #TODO -> rever tavaela folga diametra

        self.delta_sb = DeltaSB.objects.get(
            Dn_min_meters__lte = self.Ds,
            Dn_max_meters__gt = self.Ds
        )        

        return self.delta_sb.DeltaSB_meters

    def _diametro_bocal(self):
        """ ## Descrição:
            Cálculo o diâmetro do casco e filtra da tabela diâmetro do Bocal
            ## Args:
                - Dc: diâmetro do casco
            ## Return:
                - d_bocal: diâmetro do bocal [m]
                - Dc:   diâmetro do casco    [m]
        """

        self.nozzle_diameter = NozzleDiameter.objects.get(
            Dc_min_meters__lt = self.Ds,
            Dc_max_meters__gte = self.Ds
        )
        
        
        return self.nozzle_diameter.nozzle_diameter_meters
    
    def _li_lo_tabela(self):
        """ ## Descrição:
            Filtra da tabela a li e lo com base no diâmetro do casco e classe de pressão [Pesquisar mais sobre isso]
            ## Args:
                - Ds: diâmetro do casco
                - classe: classe de pressão (150 ou 600 psi)
            ## Return:
                - li: [m]
                - lo: [m]
        """
        
        
        li_lo = LiLo.objects.filter(
            pressure_class_psi= self.pressure_class
        ).annotate(
            abs_difference=Abs(F('Dc_meters') - Value(self.Dc))
        ).order_by('abs_difference').first()

        lo = li_lo.lo_meters
        li = li_lo.li_meters

        return li, lo

    def _espacamento_defletor_entrada(self):
        diam_bocal = self.nozzle_diameter.nozzle_diameter_meters

        lsi = self.ls
        if diam_bocal > self.ls:
            lsi = self.li + diam_bocal

        return lsi

    def _espacamento_defletor_saida(self):

        diam_bocal = self.nozzle_diameter.nozzle_diameter_meters

        lso = self.ls
        if diam_bocal > self.ls:
            lso = self.lo + diam_bocal

        return lso



    def _calculo_area_fluxo_cruzado(self):

        angle = self.layout.angle
        ls = self.ls
        Ds = self.Dotl
        de = self.de.diameter_meters
        Dotl = self.Dotl
        p = self.pitch.pitch_meters
        pn = self.pn

        if angle == 30 or angle == 90:
            Sm = ls * (Ds - Dotl + ((Dotl - de) / p )* (p - de))
        else:
            Sm = ls * (Ds - Dotl + ((Dotl - de) / pn) * (p - de))
        
        return Sm
    
    def _angulo_corte_defletor(self):
        theta_b = 2 * math.acos(1 - 2 * self.lc / self.Ds) 
        return theta_b

    def _calculo_area_vazamento_casco_defletor(self):
        Scd = math.pi * self.Ds * self.delta_sb_meters/2 *(1 - (self.theta_b/(2*math.pi)))
        return Scd

    def _folga_tubo_defletor(self):
        delta_tb = 7.938 * 10 ** - 4       #    [m] - Folga diametral tubo chicana- TEMA - Classe R - Verificar valor
        return delta_tb

    def _calculo_diam_feixe_tubos_centro_tubos(self):
        Dctl = self.Dotl - self.de.diameter_meters
        return Dctl

    def _angulo_interseccao_corte_defletor_com_Dctl(self):
        theta_ctl = 2 * math.acos((self.Ds - 2*self.lc)/self.Dctl)
        return theta_ctl

    def _fracao_tubos_janela_defletor(self):
        Fw = (self.theta_ctl/(2*math.pi)) - (math.sin(self.theta_ctl)/(2*math.pi))
        return Fw


    def _numero_tubos_defletor(self):
        Ntb = (1 - self.Fw) * self.Nt
        return Ntb
    
    def _area_vazamento_tubo_defletor(self):
        de = self.de.diameter_meters
        Stb = (math.pi/4) * ((self.delta_tb + de)**2 - de**2) * self.Ntb
        return Stb
    
    def _area_bypass_tubo_parede_casco(self):
        Sbp = (self.Ds - self.Dotl) * self.ls
        return Sbp

    def _area_total_janela_defletor(self):
        Swg = (self.Ds**2/4)*((self.theta_b/2) - (math.sin(self.theta_b)/2))
        return Swg
    
    def _area_tubos_janela_defletor(self):
        de = self.de.diameter_meters
        Swt = math.pi/4 * (de**2) * self.Fw * self.Nt
        return Swt

    def _area_escoamento_janela_defletor(self):
        Sw = self.Swg - self.Swt
        return Sw

    def _numero_tubos_secao_escoamento_cruzado(self):
        
        Nc = self.Ds/self.pp * (1 - (2 * self.lc / self.Ds))

        if Nc % 1 != 0:
            Nc = Nc//1 + 1

        return Nc

    def _numero_pares_tiras_selantes(self):
        
        Nss = self.Nc / 5
        if Nss % 1 != 0:
            Nss = Nss//1 + 1

        return Nss

    def _numero_efetivo_fileira_tubos_janela_defletor(self):
        Ncw = 0.8 / self.pp * (self.lc - ((self.Ds - self.Dctl)/2))
        if Ncw % 1 != 0:
            Ncw = Ncw//1 + 1

        return Ncw

    def _numero_total_defletores(self):
        Nb = ((self.L - self.lsi - self.lso)/ self.ls) + 1
        if Nb % 1 != 0:
            Nb = Nb//1 + 1
        return Nb

    def calculos_auxiliares(self):
        pn, pp = self.pitch.pn_meters, self.pitch.pp_meters
        self.pp = pp
        self.pn = pn
        self.ls = self._espacamento_defletor()
        self.lc = self._corte_defletor()
        self.Dc = self._diametro_externo_casco()
        self.delta_sb_meters = self._tabela_folga_diametral_casco_defletor()
        self.d_bocal  = self._diametro_bocal()
        self.li, self.lo = self._li_lo_tabela()
        self.lsi = self._espacamento_defletor_entrada()
        self.lso = self._espacamento_defletor_saida()
        self.Sm = self._calculo_area_fluxo_cruzado()
        self.theta_b = self._angulo_corte_defletor()
        self.Scd = self._calculo_area_vazamento_casco_defletor()
        self.delta_tb = self._folga_tubo_defletor()
        self.Dctl = self._calculo_diam_feixe_tubos_centro_tubos()
        self.theta_ctl = self._angulo_interseccao_corte_defletor_com_Dctl()
        self.Fw = self._fracao_tubos_janela_defletor()
        self.Ntb = self._numero_tubos_defletor()
        self.Stb = self._area_vazamento_tubo_defletor()
        self.Sbp = self._area_bypass_tubo_parede_casco()
        self.Swg = self._area_total_janela_defletor()
        self.Swt = self._area_tubos_janela_defletor()
        self.Sw = self._area_escoamento_janela_defletor()
        self.Nc = self._numero_tubos_secao_escoamento_cruzado()
        self.Nss = self._numero_pares_tiras_selantes()
        self.Ncw = self._numero_efetivo_fileira_tubos_janela_defletor()
        self.Nb = self._numero_total_defletores()
        
    def _vazao_massica_unidade_area_casco(self, wc):
        Gc = wc / self.Sm
        return Gc   
        
    def _numero_reynolds_casco(self, mi_c):
        Res = self.de.diameter_meters * self.Gc / mi_c
        return Res
    
    def _numero_prandtl_casco(self, cp_c, mi_c, k_c):
        Pr_s = cp_c * mi_c / k_c
        return Pr_s
    
    def _fator_colburn_casco(self):

        self.constantA = ConstantsA.objects.get(
            layout= self.layout,
            reynolds_max__gte= self.Res,
            reynolds_min__lt= self.Res
        )

        a4 = self.constantA.a4
        a3 = self.constantA.a3
        a2 = self.constantA.a2
        a1 = self.constantA.a1
        
        a = a3 / (1 + 0.14 * self.Res ** a4)


        ji = a1 *((1.33 / (self.pitch.pitch_meters / self.de.diameter_meters)) ** a )* self.Res ** a2

        return ji

    def _trans_cal_ideal_casco(self, cp_c):
        h_ideal = self.ji * cp_c * self.Gc * (self.Pr_s**(-2/3))
        return h_ideal

    def _razao_ambas_areas_vazamento_e_fluxo_cruzado(self):
        Rlm = (self.Scd + self.Stb) / self.Sm
        return Rlm
    
    def _razao_area_vazamento_casco_defletor_e_soma_areas_vazamento(self):
        Rs = self.Scd / (self.Scd + self.Stb)
        return Rs
    
    def _fator_de_correcao_devido_vazamentos(self):
        jl = 0.44 * (1 - self.Rs) + (1 - 0.44 * (1 - self.Rs))*math.exp((-2.2*self.Rlm))
        return jl

    def _fracao_escoamento_cruzado_que_pode_ocorrer_bypass(self):
        Fbp = self.Sbp / self.Sm
        return Fbp

    def _fator_correcao_devido_fluxo_bypass(self):
        if self.Res <= 100:
            C = 1.35
        elif self.Res > 100:
            C = 1.25
        
        a = (2 * self.Nss / self.Nc)**(1/3)

        jb = math.exp(-C * self.Fbp *(1 - a))
        return jb


    def _numero_total_fileiras_tubos_cruzado_pelo_fluxo(self):
        Ntc = (self.Nc + self.Ncw) * (self.Nb + 1)
        return Ntc

    def _fator_correcao_devido_gradiente_adverso_temperatura_escoamento_laminar(self):
        if self.Res > 100:
            jr =1
            return jr

        jr_ = (10 / self.Ntc) ** 0.18
        if self.Res <=20 :
            return jr_

        jr = jr_ + (20 - self.Res)/80 * (jr_ -1)

        return jr

    def _fracao_tubos_na_secao_escoamento_cruzado(self):
        Fc = 1 - 2 * self.Fw
        return Fc

    def _fator_correcao_devido_configuracoes_defletor(self):
        jc = 0.55 + 0.72 * self.Fc
        return jc 

    def _razao_espacamento_defletor_entrada_e_espacamento_normal(self):
        lsi_s = self.lsi / self.ls
        return lsi_s
        
    def _razao_espacamento_defletor_saida_e_espacamento_normal(self):
        lso_s = self.lso / self.ls
        return lso_s

    def _fator_correcao_devido_a_espacamento_desigual(self):
        n = 1/3
        if self.Res > 100:
            n = 0.6
        
        num = self.Nb + self.lsi_s **(1 - n) + self.lso_s ** (1 - n)
        den = self.Nb - 1 + self.lsi_s + self.lso_s

        js = num / den
        return js

    def trans_cal_casco(self):
        if self.shell_fluid == "hot":
            k = self.k_q
            cp = self.cp_quente
            mi = self.mi_q
            w = self.wq
        else:
            k = self.k_f
            cp = self.cp_frio
            mi = self.mi_f
            w = self.wf

        #================= Cálculo trans cal ideal =====================
        self.Gc = self._vazao_massica_unidade_area_casco(w)
        self.Res = self._numero_reynolds_casco(mi)
        self.Pr_s = self._numero_prandtl_casco(cp, mi, k)
        self.ji = self._fator_colburn_casco()
        self.h_ideal = self._trans_cal_ideal_casco(cp)

        #================= Fator de correção para os efeitos dos vazamentos da chicana =====================
        self.Rlm = self._razao_ambas_areas_vazamento_e_fluxo_cruzado()
        self.Rs = self._razao_area_vazamento_casco_defletor_e_soma_areas_vazamento()
        self.jl = self._fator_de_correcao_devido_vazamentos()

        #================= Fator de correção para os efeitos de contorno (“bypass” ) do feixe =====================
        self.Fbp = self._fracao_escoamento_cruzado_que_pode_ocorrer_bypass()
        self.jb = self._fator_correcao_devido_fluxo_bypass()


        #================= Fator de correção para o gradiente adverso de temperatura (Jr) =====================
        self.Ntc = self._numero_total_fileiras_tubos_cruzado_pelo_fluxo()
        self.jr = self._fator_correcao_devido_gradiente_adverso_temperatura_escoamento_laminar()

        #================= Fator de correção para os efeitos da configuração da chicana =====================
        self.Fc = self._fracao_tubos_na_secao_escoamento_cruzado()
        self.jc = self._fator_correcao_devido_configuracoes_defletor()
    
        #================= Fator de correção devido ao espaçamento desigual das chicanas na entrada e na saída (Js) =====================
        
        self.lsi_s = self._razao_espacamento_defletor_entrada_e_espacamento_normal()
        self.lso_s = self._razao_espacamento_defletor_saida_e_espacamento_normal()
        self.js = self._fator_correcao_devido_a_espacamento_desigual()

        #================= coeficiente trans cal lado casco  =====================
        hs = self.h_ideal * self.jc * self.jl * self.jb * self.jr * self.js
        self.hs = hs
    
    def calculo_temp_parede(self):
        """ ## Descrição:
            Cálcula a temperatura da parede.
            ## Args
                - fluido_frio:bool Se o fluído frio estiver no interior do tubo - True
        """

        if self.shell_fluid == "hot":
            fluido_frio = True
        else:
            fluido_frio = False

        hs = self.hs
        hio = self.hio
        
        Tc = (self.T1 + self.T2)/2
        tc = (self.t2 + self.t1)/2
        

        if fluido_frio:
            tw = tc + hs/ (hio + hs) * (Tc - tc) 
        else:
            tw = tc + hio/(hio + hs) * (Tc - tc)
        
        
        self.Tc = Tc
        self.tc = tc

        self.tw = tw

    # def correcao_temp_parede(self):
    #     """Corrige hs e hio de acordo com temperatura da parede
    #     """
        
    #     # TODO -> arrumar para cálculo das propriedades termodinâmicas
    #     miw = self.propriedades_termodinamicas()
        
    #     if self.shell_fluid == "hot":
    #         mi_c = self.mi_q
    #         mi_t = self.mi_f
    #         tipo_tubo = self.tipo_f
    #     elif self.shell_fluid == "cold":
    #         mi_c = self.mi_f
    #         mi_t = self.mi_q
    #         tipo_tubo = self.tipo_q

    #     phi_t_tubo = (mi_t / miw) ** 0.14
    #     phi_t_casco= (mi_c / miw) ** 0.14
        
    #     hs = hs * phi_t_casco

    #     if tipo_tubo != "water":
    #         hio = hio * phi_t_tubo

    #     self.phi_t_tubo = phi_t_tubo
    #     self.phi_t_casco = phi_t_casco
    #     self.miw = miw
    #     self.hio = hio
    #     self.hs = hs

    def coef_global_limpo(self):
        """ Cálcula o coeficiente global limpo com base nos cefientes de transmissão de calor cálculados  
        """
        hio = self.hio
        hs = self.hs
        Uc = hio * hs / (hio + hs)
        
        self.Uc = Uc

    def coef_global_sujo(self):
        Us = self.Uc + self.Rd_f + self.Rd_q
        self.Us = Us
    
    def excesso_area(self):
        Ud = self.Ud_min
        Uc = self.Uc
        delta_t = self.deltaT
        q = self.q
        A_proj = self.A_proj
        Us = self.Us

        Rd = (Uc - Ud) / (Uc * Ud)
        
        A_nec = q / (Us * delta_t)
        Ea = (A_proj - A_nec)/A_nec * 100

        self.Rd_calc = Rd
        self.A_nec = A_nec
        self.Ea = Ea

    def perda_carga_tubo(self, phi_t = 1):
        """ ## Descrição:
            - Cálculo da perda de carga do lado do tubo.
            ## Args:
                - phi_t: termo (mi/miw) ^ 0.14 para lado do tubo
        """
        Re_t = self.Re_t
        di = self.di.intern_diameter_meters
        G_t = self.Gt
        L = self.L
        n = self.n
        v = self.tube_velocity

        if self.shell_fluid == "hot":
            rho = self.rho_f
        else:
            rho = self.rho_q

        delta_Pr = (4 * n * rho * v ** 2) / 2       #   Perda de carga de retorno 

        f = (1.58 * math.log(Re_t) - 3.28) ** -2    #   Fator de atrito de Fanning
        self.f = f

        delta_Pt = (4 * f * G_t ** 2 * L * n) / (di * 2 * rho * phi_t) 
        # delta_Pt = (4 * f  * v ** 2 * L * n) / (di * 2 * phi_t) 

        # logger.debug(f"(4 * {f} * {G_t} ** 2 * {L} * {n}) / ({di} * 2 * {rho} * {phi_t})") 

        delta_PT = delta_Pt + delta_Pr

        self.delta_Pr = delta_Pr
        self.delta_Pt = delta_Pt
        self.delta_PT = delta_PT
    
    def _constantes_b(self) -> list:

        self.constantB = ConstantsB.objects.get(
            layout= self.layout,
            reynolds_max__gte= self.Res,
            reynolds_min__lt= self.Res
        )
        
        b1 = self.constantB.b1
        b2 = self.constantB.b2
        b3 = self.constantB.b3
        b4 = self.constantB.b4

        return [b1, b2, b3, b4]

    def _fator_correcao_perda_carga_devido_correntes_vazamento(self):
        Rcl = math.exp(-1.33 * (1 + self.Rs) * self.Rlm ** self.pitch.pitch_meters)
        return Rcl

    def _fator_correcao_perda_carga_devido_corrente_bypass(self):

        nss_nc = self.Nss / self.Nc

        D = 3.7
        if self.Res <=100:
            D = 4.5

        if nss_nc >= (1/2):
            Rcb = 1
            return Rcb  
        
        a = (2 * self.Nss / self.Nc) ** (1/3)

        Rcb = math.exp(-D * self.Fbp * (1 - a))

        return Rcb
    
    def _fator_atrito_fluido_casco(self):
        b1, b2, b3, b4 = self._constantes_b()

        b = b3 / (1 + 0.14 * self.Res ** b4)
        fi = b1 * (1.33 / (self.pitch.pitch_meters / self.de.diameter_meters)) ** b * (self.Res) ** b2 

        return fi
    
    def _perda_carga_ideal(self, rho_c):
        delta_Pbi = (4 * self.fi * self.Gc**2 * self.Nc / (2 * rho_c) )
        return delta_Pbi

    def _perda_carga_regiao_escoamento_cruzado(self):
        delta_Pc = self.delta_Pbi * (self.Nb -1) * self.Rcl * self.Rcb
        return delta_Pc
    
    def _correcao_perda_carga_para_espacamento_desigual_defletores(self):
        n = 0.2
        if self.Res <= 100:
            n = 1

        Rcs = self.lsi_s ** -(2-n) + self.lso_s ** -(2-n)

        return Rcs
    
    def _perda_carga_regiao_entrada_e_saida(self):
        delta_Pe = 2 * self.delta_Pbi * (1 + self.Ncw/self.Nc) * self.Rcb * self.Rcs
        return delta_Pe
    
    def _numero_tubos_janela_defletor(self):
        Ntw = self.Nt * self.Fw
        return Ntw
    def _diametro_hidraulico_janela_defletor(self):
        de = self.de.diameter_meters
        Dw = 4 * self.Sw / (math.pi * de * self.Ntw + self.theta_b * self.Ds / 2)
        return Dw

    def _perda_carga_ideal_para_janela_defletor(self, w_c, rho_c, mi_c):
        de = self.de.diameter_meters
        if self.Res > 100:
            delta_Pwi = (2 + 0.6 * self.Ncw) * (w_c ** 2 / (self.Sm * self.Sw)) / (2 * rho_c)

        else: 
            a1 = (26 * mi_c * w_c) / (math.sqrt(self.Sm * self.Sw))
            a2 = (self.Ncw / (self.pitch.pitch_meters - de)) + self.ls / (self.Dw ** 2)
            a3 = w_c ** 2 / (self.Sm * self.Sw * rho_c)

            delta_Pwi = a1 * a2 + a3
        
        return delta_Pwi

    def _perda_carga_janela_defletor(self):
        delta_Pw = self.delta_Pwi * self.Nb * self.Rcl
        return delta_Pw


    def perda_carga_casco(self):
        if self.shell_fluid == "hot":
            mi = self.mi_q
            W = self.wq
            rho = self.rho_q
        elif self.shell_fluid == "cold":
            mi = self.mi_f
            W = self.wf
            rho = self.rho_f


        self.fi = self._fator_atrito_fluido_casco()
        self.delta_Pbi = self._perda_carga_ideal(rho)

        #================ Perda de carga na seção de escoamento cruzado ======================
        self.Rcl = self._fator_correcao_perda_carga_devido_correntes_vazamento()
        self.Rcb = self._fator_correcao_perda_carga_devido_corrente_bypass()
        self.delta_Pc = self._perda_carga_regiao_escoamento_cruzado()
        
        #================== Perda de carga nas regiões de entrada e saída do casco delta_Pe ============

        self.Rcs = self._correcao_perda_carga_para_espacamento_desigual_defletores()
        self.delta_Pe = self._perda_carga_regiao_entrada_e_saida()

        #================= Perda de carga nas janelas ==============================================
        self.Ntw = self._numero_tubos_janela_defletor()
        self.Dw = self._diametro_hidraulico_janela_defletor()
        self.delta_Pwi = self._perda_carga_ideal_para_janela_defletor(W, rho, mi)
        self.delta_Pw = self._perda_carga_janela_defletor()
        
        #================ Perda de carga do lado do casco ===============================================
        delta_Ps = self.delta_Pc + self.delta_Pw + self.delta_Pe       #   Perda de carga lado do casco excluindo os bocais

        self.delta_Ps = delta_Ps

    def results(self) -> dict:
        results = {
            'q': self.q,
            'R': self.R,
            'S': self.S,
            'F': self.F,
            'mldt': self.mldt,
            'deltaT': self.deltaT,
            'Nt': self.Nt,
            'Dotl': self.Dotl,
            'Ds': self.Ds,
            'A_proj': self.A_proj,
            'Ud_min': self.Ud_min,
            'area_one_tube': self.area_one_tube,
            'area_tube': self.area_tube,
            'Gt': self.Gt,
            'Re_t': self.Re_t,
            'tube_velocity': self.tube_velocity,
            'hi': self.hi,
            'hio': self.hio,
            'pp': self.pp,
            'pn': self.pn,
            'ls': self.ls,
            'lc': self.lc,
            'Dc': self.Dc,
            'delta_sb_meters': self.delta_sb_meters,
            'd_bocal': self.d_bocal,
            'li': self.li,
            'lo': self.lo,
            'lsi': self.lsi,
            'lso': self.lso,
            'Sm': self.Sm,
            'theta_b': self.theta_b,
            'Scd': self.Scd,
            'delta_tb': self.delta_tb,
            'Dctl': self.Dctl,
            'theta_ctl': self.theta_ctl,
            'Fw': self.Fw,
            'Ntb': self.Ntb,
            'Stb': self.Stb,
            'Sbp': self.Sbp,
            'Swg': self.Swg,
            'Stw': self.Swt,
            'Sw': self.Sw,
            'Nc': self.Nc,
            'Nss': self.Nss,
            'Ncw': self.Ncw,
            'Nb': self.Nb,
            'Gc': self.Gc,
            'Pr_s': self.Pr_s,
            'ji': self.ji,
            'h_ideal': self.h_ideal,
            'Rlm': self.Rlm,
            'Rs': self.Rs,
            'jl': self.jl,
            'Fbp': self.Fbp,
            'jb': self.jb,
            'Ntc': self.Ntc,
            'jr': self.jr,
            'Fc': self.Fc,
            'jc': self.jc,
            'lsi_s': self.lsi_s,
            'lso_s': self.lso_s,
            'js': self.js,
            'hs': self.hs,
            'T_c': self.Tc,
            'tc': self.tc,
            'tw': self.tw,
            'Uc': self.Uc,
            'Us': self.Us,
            'Rd_calc': self.Rd_calc,
            'A_nec': self.A_nec,
            'Ea': self.Ea,
            'delta_Pr': self.delta_Pr,
            'delta_Ptt': self.delta_Pt,
            'delta_PT': self.delta_PT,
            'fi': self.fi,
            'delta_Pbi': self.delta_Pbi,
            'Rcl': self.Rcl,
            'Rcb': self.Rcb,
            'delta_Pc': self.delta_Pc,
            'Rcs': self.Rcs,
            'delta_Pe': self.delta_Pe,
            'Ntw': self.Ntw,
            'Dw': self.Dw,
            'delta_Pwi': self.delta_Pwi,
            'delta_Pw': self.delta_Pw,
            'delta_Ps': self.delta_Ps,
        }

        return results


    def objective_function_GA(self, fator_area_proj=1):
        aval_delta_PT = math.fabs(self.delta_PT - self.perda_carga_admissivel_tubo)
        aval_delta_Ps = math.fabs(self.delta_Ps - self.perda_carga_admissivel_casco)

        F = self.A_proj*fator_area_proj + aval_delta_PT + aval_delta_Ps 
    
        return F
    
    def restricao_EA_min(self):
        return 5 - self.Ea
    
    def restricao_EA_max(self):
        return self.Ea - 25
        
    

if __name__ == "__main__":
   ...




