from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseNotFound
from frontend.utils import*
import requests
import logging

logger = logging.getLogger('API')
def results(request, pk):

    endpoint_results = api_endpoint(request, reverse('API:results_detail', kwargs={'pk': pk}))
    resp = requests.get(endpoint_results)
    
    if resp.status_code != 200:
        return HttpResponseNotFound('Não encontrou resultados')
    
    result_data = resp.json()

    input_id = resp.json().get('inputs')
    endpoint_inputs = api_endpoint(request, reverse('API:inputs_shell_and_tube_detail', kwargs={'pk': input_id}))
    resp_inp = requests.get(endpoint_inputs)
    if resp_inp.status_code != 200:
        return HttpResponseNotFound('Não encontrou Inputs')
    
    input_data = resp_inp.json()
    

    inputs = item_inputs(input_data)
    balanco_energia = results_balanco_energia(result_data)
    calc_aux = results_calc_auxiliares(result_data)
    results_trans_tubos = results_transcal_tubos(result_data)
    r_perda_carga_tubos = results_perda_carga_tubos(result_data)
    r_trans_cal_casco = results_trans_cal_casco(result_data)
    r_perda_carga_casco = results_perda_carga_casco(result_data)
    other_results = outros_resultados(result_data)


    files = []
    if result_data.get('calculation_id'):
        endpoint_charts = api_endpoint(request, reverse('API:chart_list'))
        resp_charts = requests.get(endpoint_charts, params={'calculation_id': result_data.get('calculation_id')})
        if resp_charts.status_code == 200:
            charts = resp_charts.json()
            if len(charts) > 0:
                files.extend(charts[0]['files'])


    context = {
        "input_casco": inputs['input_casco'],
        "input_tubos": inputs['input_tubos'],
        "other_inputs": inputs['other_inputs'],
        "energy_balance": balanco_energia,
        "aux_calc": calc_aux,
        "trans_cal_tubes": results_trans_tubos,
        "perda_carga_tubos": r_perda_carga_tubos,
        "tans_cal_casco": r_trans_cal_casco,
        "perda_carga_casco": r_perda_carga_casco,
        "other_results": other_results,
        'files': files
    }

    return render(request, 'results.html', context=context)

def outros_resultados(result_data):
    results_ = [
        {
            "var": r"\(U_{c}\)",
            "description": "Coeficiente Global de transferência de calor limpo",
            "value": result_data['Uc'],
            "unity": "W/m^2 K"
        },
        {
            "var": r"\(U_{s}\)",
            "description": "Coeficiente Global de transferência de calor sujo",
            "value": result_data['Us'],
            "unity": "W/m^2 K"
        },
        {
            "var": r"\(A_{nec}\)",
            "description": "Área necessária",
            "value": result_data['A_nec'],
            "unity": "m^2"
        },
        {
            "var": r"\(EA\)",
            "description": "Excesso de área",
            "value": result_data['Ea'],
            "unity": "%"
        },
    ]

    return results_

def results_perda_carga_casco(result_data):

    results_ = [
        {
            "var": r"\(N_{tw}\)",
            "description": "número de tubos na janela do defletor",
            "value": result_data['Ntw'],
            "unity": ""
        },
        {
            "var": r"\(Re_{s}\)",
            "description": "número de Reynolds no casco",
            "value": result_data['Res'],
            "unity": ""
        },
         {
            "var": r"\(D_w\)",
            "description": "diâmetro hidráulico do janela do defletor",
            "value": result_data['Dw'],
            "unity": "m"
        },
        {
            "var": r"\(f_i\)",
            "description": "Fator de atrito",
            "value": result_data['fi'],
            "unity": ""
        },
        {
            "var": r"\(\Delta P_{bi}\)",
            "description": "Perda de carga ideal para região de escoamento cruzado",
            "value": result_data['delta_Pbi'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(R_{cl}\)",
            "description": "fator de correção devido as correntes de vazamento",
            "value": result_data['Rcl'],
            "unity": ""
        },
        {
            "var": r"\(R_{cb}\)",
            "description": "fator de correção devido as correntes bypass",
            "value": result_data['Rcb'],
            "unity": ""
        },
        {
            "var": r"\(R_{cs}\)",
            "description": "fator de correção devido ao espaçamento desigual dos defletores de entrada e saída",
            "value": result_data['Rcs'],
            "unity": ""
        },
        {
            "var": r"\(\Delta P_{c}\)",
            "description": "perda de carga na região de fluxo cruzado",
            "value": result_data['delta_Pc'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(\Delta P_{e}\)",
            "description": "perda de carga nas regiões de entrada e saída",
            "value": result_data['delta_Pe'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(\Delta P_{wi}\)",
            "description": "perda de carga ideal na janela do defletor",
            "value": result_data['delta_Pwi'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(\Delta P_{w}\)",
            "description": "perda de carga na janela do defletor",
            "value": result_data['delta_Pw'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(\Delta P_{s}\)",
            "description": "perda de carga no casco",
            "value": result_data['delta_Ps'],
            "unity": "Pa/m"
        },
    ]

    return results_



def results_trans_cal_casco(result_data):
    results_ = [
        {
            "var": r"\(G_c\)",
            "description": "Vazão mássica por unidade de área casco",
            "value": result_data['Gc'],
            "unity": "kg/m^2 * s"
        },
        {
            "var": r"\(Pr_s\)",
            "description": "Número de Prandtl",
            "value": result_data['Pr_s'],
            "unity": ""
        },
        {
            "var": r"\(j_i\)",
            "description": "Fator de Colburn",
            "value": result_data['ji'],
            "unity": ""
        },
        {
            "var": r"\(h_{ideal}\)",
            "description": "Coeficiente de transferência de calor ideal para lado do casco",
            "value": result_data['h_ideal'],
            "unity": "W/m^2*k"
        },
        {
            "var": r"\(R_{lm}\)",
            "description": "Razão entre ambas as áreas de vazamento e a área de fluxo cruzado puro",
            "value": result_data['Rlm'],
            "unity": ""
        },
        {
            "var": r"\(R_{s}\)",
            "description": "Razão da área de vazamento casco-defletor e a soma das áreas de vazamento",
            "value": result_data['Rs'],
            "unity": ""
        },
        {
            "var": r"\(F_{bp}\)",
            "description": "Fração escoamento cruzado que pode ocorrer corrente C",
            "value": result_data['Fbp'],
            "unity": ""
        },
        {
            "var": r"\(F_{c}\)",
            "description": "Fração de tubos em uma seção de escoamento cruzado",
            "value": result_data['Fc'],
            "unity": ""
        },
        {
            "var": r"\(N_{tc}\)",
            "description": "Número total de fileiras de tubos cruzados pelo fluxo no trocador",
            "value": result_data['Ntc'],
            "unity": ""
        },
        {
            "var": r"\(j_{l}\)",
            "description": "Fator de correção para os efeitos de vazamento do defletor",
            "value": result_data['jl'],
            "unity": ""
        },
        {
            "var": r"\(j_{b}\)",
            "description": "fator de correção para o efeito bypass no feixe de tubos",
            "value": result_data['jb'],
            "unity": ""
        },
        {
            "var": r"\(j_{r}\)",
            "description": "fator de correção para o gradiente de temperatura em escoamento laminar",
            "value": result_data['jr'],
            "unity": ""
        },
        {
            "var": r"\(j_{c}\)",
            "description": "fator de correção devido a configuração do defletor",
            "value": result_data['jc'],
            "unity": ""
        },
        {
            "var": r"\(j_{s}\)",
            "description": "fator de correção devido ao espaçamento dos defletores na entrada e saída do trocador",
            "value": result_data['js'],
            "unity": ""
        },
        {
            "var": r"\(h_{s}\)",
            "description": "Coeficiente de transferência de calor para lado do casco",
            "value": result_data['hs'],
            "unity": "W/m^2 * K"
        },
    ]

    return results_



def results_perda_carga_tubos(result_data):

    results_perda_carga = [
        {
            "var": r"\(\Delta P_t\)",
            "description": "Perda de carga no feixe de tubos",
            "value": result_data['delta_Ptt'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(\Delta P_r\)",
            "description": "Perda de carga na região de retorno",
            "value": result_data['delta_Pr'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(\Delta P_{tt}\)",
            "description": "Perda de carga total no lado dos tubos",
            "value": result_data['delta_PT'],
            "unity": "Pa/m"
        },
    ]

    return results_perda_carga


def results_transcal_tubos(result_data):

    results_trans = [
        {
            "var": r"\(G_t\)",
            "description": "Vazão mássica por unidade de área (tubos)",
            "value": result_data['Gt'],
            "unity": "kg/s*m^2"
        },
        {
            "var": r"\(Re_t\)",
            "description": "Número de Reynolds para o lado dos tubos",
            "value": result_data['Re_t'],
            "unity": ""
        },
        {
            "var": r"\(V_t\)",
            "description": "Velocidade do fluido nos tubos",
            "value": result_data['tube_velocity'],
            "unity": "m/s"
        },
        {
            "var": r"\(h_i\)",
            "description": "Coeficiente de transferência de calor para o lado dos tubos com base na área interna",
            "value": result_data['hi'],
            "unity": "W/m^2 K"
        },
        {
            "var": r"\(h_{io}\)",
            "description": "Coeficiente de transferência de calor para o lado dos tubos com base na área externa",
            "value": result_data['hio'],
            "unity": "W/m^2 K"
        },
    ]

    return results_trans


def results_calc_auxiliares(result_data) -> dict:
   
    calc_aux = [
        {
            "var": r"\(N_t\)",
            "description": "Número de tubos",
            "value": result_data['Nt'],
            "unity": ""
        },
        {
            "var": r"\(D_{otl}\)",
            "description": "Diâmetro externo do feixe de tubos, medido no limite externo dos tubos",
            "value": result_data['Dotl'],
            "unity": "m"
        },
        {
            "var": r"\(A_{proj}\)",
            "description": "Área de projeto",
            "value": result_data['A_proj'],
            "unity": "m^2"
        },
        {
            "var": r"\(L_{s}\)",
            "description": "Distância entre defletores",
            "value": result_data['ls'],
            "unity": "m"
        },
        {
            "var": r"\(L_{c}\)",
            "description": "Corte do defletor",
            "value": result_data['lc'],
            "unity": "m"
        },
        {
            "var": r"\(P_{p}\)",
            "description": "Passo paralelo do tubo",
            "value": result_data['pp'],
            "unity": "m"
        },
        {
            "var": r"\(P_{n}\)",
            "description": "Passo normal do tubo",
            "value": result_data['pn'],
            "unity": "m"
        },
        {
            "var": r"\(D_{c}\)",
            "description": "Diâmetro externo do Casco",
            "value": result_data['Dc'],
            "unity": "m"
        },
        {
            "var": r"\(\delta_{sb}\)",
            "description": "Folga diametral entre casco e defletor",
            "value": result_data['delta_sb_meters'],
            "unity": "m"
        },
        {
            "var": r"\(D_{bocal}\)",
            "description": "Diâmetro do bocal",
            "value": result_data['d_bocal'],
            "unity": "m"
        },
        {
            "var": r"\(L_{si}\)",
            "description": "Espaçamento Defletor de entrada",
            "value": result_data['lsi'],
            "unity": "m"
        },
        {
            "var": r"\(L_{so}\)",
            "description": "Espaçamento Defletor de saída",
            "value": result_data['lso'],
            "unity": "m"
        },
        {
            "var": r"\(Sm\)",
            "description": "Área de fluxo cruzado",
            "value": result_data['Sm'],
            "unity": "m"
        },
        {
            "var": r"\(\theta_b\)",
            "description": "Ângulo de corte do defletor",
            "value": result_data['theta_b'],
            "unity": "rad"
        },
        {
            "var": r"\(S_{cd}\)",
            "description": "Área de vazamento entre o casco e o defletor",
            "value": result_data['Scd'],
            "unity": "m^2"
        },
        {
            "var": r"\(\delta_{td}\)",
            "description": "Folga entre tubo e defletor",
            "value": result_data['delta_tb'],
            "unity": "m"
        },
        {
            "var": r"\(D_{ctl}\)",
            "description": "Diâmetro do feixe de tubos, medido de centro a centro dos tubos",
            "value": result_data['Dctl'],
            "unity": "m"
        },
        {
            "var": r"\(\theta_{ctl}\)",
            "description": r"Ângulo formado da intersecção do corte do defletor com \(D_{ctl}\)",
            "value": result_data['theta_ctl'],
            "unity": "rad"
        },
        {
            "var": r"\(Fw\)",
            "description": r"Fração do número de tubos na janela do defletor",
            "value": result_data['Fw'],
            "unity": ""
        },
        {
            "var": r"\(N_{tb}\)",
            "description": r"Número de tubos no defletor",
            "value": result_data['Ntb'],
            "unity": ""
        },
        {
            "var": r"\(S_{tb}\)",
            "description": r"Área de vazamento entre o tubo e o defletor",
            "value": result_data['Stb'],
            "unity": "m^2"
        },
        {
            "var": r"\(S_{bp}\)",
            "description": r"Área onde ocorre o bypass",
            "value": result_data['Sbp'],
            "unity": "m^2"
        },
        {
            "var": r"\(S_{wg}\)",
            "description": r"Área total na janela do defletor",
            "value": result_data['Swg'],
            "unity": "m^2"
        },
        {
            "var": r"\(S_{tw}\)",
            "description": r"Área dos tubos na janela do defletor",
            "value": result_data['Stw'],
            "unity": "m^2"
        },
        {
            "var": r"\(S_{w}\)",
            "description": r"Área do escoamento da janela do defletor",
            "value": result_data['Sw'],
            "unity": "m^2"
        },
        {
            "var": r"\(N_{c}\)",
            "description": r"Número de fileira de tubos na seção de escoamento cruzado",
            "value": result_data['Nc'],
            "unity": ""
        },
        {
            "var": r"\(N_{ss}\)",
            "description": r"Número de pares de tiras selantes",
            "value": result_data['Nss'],
            "unity": ""
        },
        {
            "var": r"\(N_{cw}\)",
            "description": r"Número efetivo de fileiras de tubos na janela do defletor",
            "value": result_data['Ncw'],
            "unity": ""
        },
        {
            "var": r"\(N_{b}\)",
            "description": r"Número de defletores",
            "value": result_data['Ncw'],
            "unity": ""
        },
    ]

    return calc_aux

def results_balanco_energia(result_data) -> dict:
    balanco_energia = [
        {
            "var": r"\(q\)",
            "description": "Taxa de transferência de calor",
            "value": result_data['q'],
            "unity": "W"
        },
        {
            "var": r"\(MLDT\)",
            "description": "Diferença média logaritmica de Temperaturas",
            "value": result_data['mldt'],
            "unity": "K"
        },
        {
            "var": r"\(\Delta T\)",
            "description": "Diferença média de Temperatura",
            "value": result_data['deltaT'],
            "unity": "K"
        },
    ]

    return balanco_energia

def item_inputs(input_data) -> dict:
    input_data_table = {
        "input_casco": [],
        "input_tubos": [],
        "other_inputs": [],
    }


    input_q = [
        {
            "var": r"\(T_1\)",
            "description": "Temperatura Entrada (Quente)",
            "value": input_data['T1_hot'],
            "unity": "K"
        },
        {
            "var": r"\(T_2\)",
            "description": "Temperatura Saída (Quente)",
            "value": input_data['T2_hot'],
            "unity": "K"
        },
        {
            "var": r"\(w_q\)",
            "description": "Vazão mássica (Quente)",
            "value": input_data['wq'],
            "unity": "kg/s"
        },
        {
            "var": r"\(C_{p,q}\)",
            "description": "Calor Específico (Quente)",
            "value": input_data['cp_quente'],
            "unity": "J/kg*K"
        },
        {
            "var": r"\(\rho_{q}\)",
            "description": "Densidade (Quente)",
            "value": input_data['rho_q'],
            "unity": "kg/m^3"
        },
        {
            "var": r"\(\mu_{q}\)",
            "description": "Viscosidade dinâmica (Quente)",
            "value": input_data['mi_q'],
            "unity": "Pa*s"
        },
        {
            "var": r"\(k_{q}\)",
            "description": "Condutividade Térmica (Quente)",
            "value": input_data['k_q'],
            "unity": "J/kg*K"
        },
        {
            "var": r"\(R_{d,q}\)",
            "description": "Fator de incrustação (Quente)",
            "value": input_data['Rd_q'],
            "unity": "m^2 K/W"
        }

    ]

    input_f = [
        {
            "var": r"\(t_1\)",
            "description": "Temperatura Entrada (Frio)",
            "value": input_data['t1_cold'],
            "unity": "K"
        },
        {
            "var": r"\(t_2\)",
            "description": "Temperatura Saída (Frio)",
            "value": input_data['t2_cold'],
            "unity": "K"
        },
        {
            "var": r"\(w_f\)",
            "description": "Vazão mássica (Frio)",
            "value": input_data['wf'],
            "unity": "kg/s"
        },
        {
            "var": r"\(C_{p,f}\)",
            "description": "Calor Específico (Frio)",
            "value": input_data['cp_frio'],
            "unity": "J/kg*K"
        },
        {
            "var": r"\(\rho_{f}\)",
            "description": "Densidade (Frio)",
            "value": input_data['rho_f'],
            "unity": "kg/m^3"
        },
        {
            "var": r"\(\mu_{f}\)",
            "description": "Viscosidade dinâmica (Frio)",
            "value": input_data['mi_f'],
            "unity": "Pa*s"
        },
        {
            "var": r"\(k_{f}\)",
            "description": "Condutividade Térmica (Frio)",
            "value": input_data['k_f'],
            "unity": "J/kg*K"
        },
        {
            "var": r"\(R_{d,f}\)",
            "description": "Fator de incrustação (Quente)",
            "value": input_data['Rd_f'],
            "unity": "m^2 K/W"
        }

    ]
    other_inputs = [
        {
            "var": r"n",
            "description": "Número de Passagens nos Tubos",
            "value": input_data['n'],
            "unity": ""
        },
        {
            "var": r"\(P_t\)",
            "description": "Passo dos tubos",
            "value": input_data['pitch']['description'],
            "unity": "Pol"
        },
        {
            "var": r"BWG",
            "description": "Norma BWG para espessura do tubo",
            "value": input_data['di']['description'],
            "unity": ""
        },
        {
            "var": r"\(D_s\)",
            "description": "Diâmetro Interno do Casco",
            "value": input_data['Ds_inch'],
            "unity": "Pol"
        },
        {
            "var": r"L",
            "description": "Comprimento do Casco",
            "value": input_data['L'],
            "unity": "m"
        },
        {
            "var": r"\(e_c\)",
            "description": "Espessura do Casco",
            "value": input_data['shell_thickness_meters'],
            "unity": "m"
        },
        {
            "var": r"Material do Tubo",
            "description": "Material do Tubo",
            "value": input_data['tube_material'],
            "unity": ""
        },
        {
            "var": r"\(\Delta P_{a,c}\)",
            "description": "Perda de Carga Adimissível no Casco",
            "value": input_data['perda_carga_admissivel_casco'],
            "unity": "Pa/m"
        },
        {
            "var": r"\(\Delta P_{a,t}\)",
            "description": "Perda de Carga Adimissível no Tubo",
            "value": input_data['perda_carga_admissivel_tubo'],
            "unity": "Pa/m"
        },

    ]
    input_data_table['other_inputs'] = other_inputs
    if input_data["shell_fluid"] ==  "hot":
        input_data_table["input_casco"] = input_q
        input_data_table["input_tubos"] = input_f
    else:
        input_data_table["input_tubos"] = input_q
        input_data_table["input_casco"] = input_f

    return input_data_table

