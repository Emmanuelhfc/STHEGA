from django import forms

class STHEForm(forms.Form):
    calculation_id = forms.UUIDField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Calculation ID (opcional)',
            'id': 'calculation_id'
        })
    )
    T1_hot = forms.FloatField(
        required=True,
        label="Temperatura Entrada (Quente)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 150.0",
        })
    )
    T2_hot = forms.FloatField(
        required=True,
        label="Temperatura Saída (Quente)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 120.0",
        })
    )
    t1_cold = forms.FloatField(
        required=True,
        label="Temperatura Entrada (Frio)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 25.0",
        })
    )
    t2_cold = forms.FloatField(
        required=True,
        label="Temperatura Saída (Frio)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 40.0",
        })
    )
    wq = forms.FloatField(
        required=True,
        label="Taxa de Fluxo (Quente)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 0.5",
        })
    )
    wf = forms.FloatField(
        required=True,
        label="Taxa de Fluxo (Frio)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 0.7",
        })
    )
    cp_quente = forms.FloatField(
        required=True,
        label="Calor Específico (Quente)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 4.2",
        })
    )
    cp_frio = forms.FloatField(
        required=True,
        label="Calor Específico (Frio)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Ex: 4.2",
        })
    )
    casco_passagens = forms.IntegerField(
        required=True,
        initial=1,
        label="Número de Passagens no Casco",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    rho_q = forms.FloatField(
        required=True,
        label="Densidade (Quente)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    rho_f = forms.FloatField(
        required=True,
        label="Densidade (Frio)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    # Adicionando outros campos...
    n = forms.ChoiceField(
        choices=[],
        required=False,
        label="Número de Passagens nos Tubos",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    # di = forms.ModelChoiceField(
    #     required=False,
    #     label="Diâmetro Interno do Tubo",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     })
    # )
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
    

