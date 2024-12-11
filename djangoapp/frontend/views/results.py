from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseNotFound
from frontend.utils import*
import requests
import logging

logger = logging.getLogger('API')

def item_inputs(input_data) -> dict:
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
        }

    ]

    # t1_cold = forms.FloatField(
    #     required=True,
    #     label=r"\(t_1\) - Temperatura Entrada (Frio) [K]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "Ex: 25.0",
    #     })
    # )
    # t2_cold = forms.FloatField(
    #     required=True,
    #     label=r"\(t_2\) - Temperatura Saída (Frio) [K]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "Ex: 40.0",
    #     })
    # )
    
    # wf = forms.FloatField(
    #     required=True,
    #     label=r"\(w_f\) - Vazão mássica (Frio) [kg/s]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "Ex: 0.7",
    #     })
    # )
    
    # cp_frio = forms.FloatField(
    #     required=True,
    #     label=r"\(C_{p,f}\) - Calor Específico (Frio) [J/kg*K]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "Ex: 4.2",
    #     })
    # )
   
    # rho_f = forms.FloatField(
    #     required=True,
    #     label=r"\(\rho_{q}\) - Densidade (Frio) [kg/m^3]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    
    # mi_f = forms.FloatField(
    #     required=True,
    #     label=r"\(\mu_{f}\) - Viscosidade dinâmica (Frion) [Pa*s]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    
    # k_f = forms.FloatField(
    #     required=True,
    #     label=r"\(k_{f}\) - Viscosidade dinâmica (Frio) [J/kg*K]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # tipo_q = forms.CharField(
    #     required=True,
    #     label=r"Tipo do Fluido (Quente)",
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # tipo_f = forms.CharField(
    #     required=True,
    #     label=r"Tipo do Fluido (Frio)",
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #     })
    # )


    # n = forms.ChoiceField(
    #     choices=TubePasses.choices,
    #     required=False,
    #     label="Número de Passagens nos Tubos",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )


    # pitch = forms.ModelChoiceField(
    #     queryset=Pitch.objects.all(),
    #     required=False,
    #     label=r"[\(d_{e}\) Diâmetro Externo tubo] [Arranjo] [\(P_{t}\) Passo dos Tubos]",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )

    # bwg = forms.ChoiceField(
    #     choices=[("BWG14", "BWG14"), ("BWG16", "BWG16")],
    #     required=False,
    #     label="BWG",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # Ds_inch = forms.ModelChoiceField(
    #     queryset = TubeCount.objects.values_list('Ds_inch', flat=True).distinct(),
    #     required=False,
    #     label=r"\(D_{s}\) - Diâmetro Interno do Casco (Frio) [Pol]",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # L = forms.FloatField(
    #     required=True,
    #     label=r"L - Comprimento do Casco [m]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # shell_fluid = forms.ChoiceField(
    #     choices=ShellFluid.choices,
    #     required=False,
    #     label="Fluido que passa no Casco",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # ls_percent = forms.FloatField(
    #     required=True,
    #     label=r"\(\frac{l_s}{D_s}\) - Espaçamento entre os defletores em porcentagem  [%]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # lc_percent = forms.FloatField(
    #     required=True,
    #     label=r"\(\frac{l_c}{D_s}\) - Corte do Defletor em porcentagem  [%]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # shell_thickness_meters = forms.FloatField(
    #     required=True,
    #     label=r"Espessura do casco [m]",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # tube_material = forms.ModelChoiceField(
    #     queryset = TubeMaterial.objects.all(),
    #     required=False,
    #     label=r"Material do Tubo",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # tube_material = forms.ChoiceField(
    #     choices=[(150.0, '150 Psi'), (600.0, "600 Psi")], 
    #     required=False,
    #     label=r"Classe de Pressão",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # perda_carga_admissivel_casco = forms.FloatField(
    #     required=True,
    #     label=r"Perda de Carga Adimissível no Casco",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    # perda_carga_admissivel_tubo = forms.FloatField(
    #     required=True,
    #     label=r"Perda de Carga Adimissível no Tubo",
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )

    return input_q

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
    

    input_q = item_inputs(input_data)



    item = {
        "var": "",
        "description": "",
        "value": "",
        "unity": ""
    }


    context = {
        "input_casco": input_q,
        "input_tubos": "",
        "other_inputs": "",
        "energy_balance": "",
        "aux_calc": "",
        "trans_cal_tubes": "",
        "perda_carga_tubos": "",
        "tans_cal_casco": "",
        "perda_carga_casco": "",
    }

    return render(request, 'results.html', context=context)
