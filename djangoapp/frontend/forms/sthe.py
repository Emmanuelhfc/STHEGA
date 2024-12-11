from django import forms
from API.models import TubePasses, TubeInternDiameter, Pitch, TubeCount, ShellFluid, TubeMaterial


class FilterInputForm(forms.Form):
    id = forms.IntegerField(
        required=True,
        label=r"ID do input do cálculo",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )



class STHEForm(forms.Form):
    T1_hot = forms.FloatField(
        required=True,
        label=r"\(T_1\) - Temperatura Entrada (Quente) [K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 150.0",
        })
    )
    T2_hot = forms.FloatField(
        required=True,
        label=r"\(T_2\) - Temperatura Saída (Quente) [K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 120.0",
        })
    )
    t1_cold = forms.FloatField(
        required=True,
        label=r"\(t_1\) - Temperatura Entrada (Frio) [K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 25.0",
        })
    )
    t2_cold = forms.FloatField(
        required=True,
        label=r"\(t_2\) - Temperatura Saída (Frio) [K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 40.0",
        })
    )
    wq = forms.FloatField(
        required=True,
        label=r"\(w_q\) - Vazão mássica (Quente) [kg/s]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 0.5",
        })
    )
    wf = forms.FloatField(
        required=True,
        label=r"\(w_f\) - Vazão mássica (Frio) [kg/s]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 0.7",
        })
    )
    cp_quente = forms.FloatField(
        required=True,
        label=r"\(C_{p,q}\) - Calor Específico (Quente) [J/kg*K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 4.2",
        })
    )
    cp_frio = forms.FloatField(
        required=True,
        label=r"\(C_{p,f}\) - Calor Específico (Frio) [J/kg*K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 4.2",
        })
    )
    rho_q = forms.FloatField(
        required=True,
        label=r"\(\rho_{q}\) - Densidade (Quente) [kg/m^3]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    rho_f = forms.FloatField(
        required=True,
        label=r"\(\rho_{q}\) - Densidade (Frio) [kg/m^3]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    mi_q = forms.FloatField(
        required=True,
        label=r"\(\mu_{q}\) - Viscosidade dinâmica (Quente) [Pa*s]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    mi_f = forms.FloatField(
        required=True,
        label=r"\(\mu_{f}\) - Viscosidade dinâmica (Frion) [Pa*s]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    k_q = forms.FloatField(
        required=True,
        label=r"\(k_{q}\) - Condutividade Térmica (Quente) [J/kg*K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    k_f = forms.FloatField(
        required=True,
        label=r"\(k_{f}\) - Viscosidade dinâmica (Frio) [J/kg*K]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    tipo_q = forms.CharField(
        required=True,
        label=r"Tipo do Fluido (Quente)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    tipo_f = forms.CharField(
        required=True,
        label=r"Tipo do Fluido (Frio)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )


    n = forms.ChoiceField(
        choices=TubePasses.choices,
        required=False,
        label="Número de Passagens nos Tubos",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )


    pitch = forms.ModelChoiceField(
        queryset=Pitch.objects.all(),
        required=False,
        label=r"[\(d_{e}\) Diâmetro Externo tubo] [Arranjo] [\(P_{t}\) Passo dos Tubos]",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    bwg = forms.ChoiceField(
        choices=[("BWG14", "BWG14"), ("BWG16", "BWG16")],
        required=False,
        label="BWG",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    Ds_inch = forms.ModelChoiceField(
        queryset = TubeCount.objects.values_list('Ds_inch', flat=True).distinct(),
        required=False,
        label=r"\(D_{s}\) - Diâmetro Interno do Casco (Frio) [Pol]",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    L = forms.FloatField(
        required=True,
        label=r"L - Comprimento do Casco [m]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    shell_fluid = forms.ChoiceField(
        choices=ShellFluid.choices,
        required=False,
        label="Fluido que passa no Casco",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    ls_percent = forms.FloatField(
        required=True,
        label=r"\(\frac{l_s}{D_s}\) - Espaçamento entre os defletores em porcentagem  [%]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    lc_percent = forms.FloatField(
        required=True,
        label=r"\(\frac{l_c}{D_s}\) - Corte do Defletor em porcentagem  [%]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    shell_thickness_meters = forms.FloatField(
        required=True,
        label=r"Espessura do casco [m]",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    tube_material = forms.ModelChoiceField(
        queryset = TubeMaterial.objects.all(),
        required=False,
        label=r"Material do Tubo",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    tube_material = forms.ChoiceField(
        choices=[(150.0, '150 Psi'), (600.0, "600 Psi")], 
        required=False,
        label=r"Classe de Pressão",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    perda_carga_admissivel_casco = forms.FloatField(
        required=True,
        label=r"Perda de Carga Adimissível no Casco",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    perda_carga_admissivel_tubo = forms.FloatField(
        required=True,
        label=r"Perda de Carga Adimissível no Tubo",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    
    # pitch = forms.ModelChoiceField(
    #     required=False,
    #     label="Passo (Pitch)",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )
    

    def clean(self):
        cleaned_data = super().clean()
        # Remove campos vazios
        return {key: value for key, value in cleaned_data.items() if value not in [None, '']}
    

