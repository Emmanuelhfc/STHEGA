from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

PERCENTAGE_VALIDATOR = [MinValueValidator(Decimal(0.0)), MaxValueValidator(Decimal(1.0))]
CORTE_DEFLETOR = [MinValueValidator(Decimal(0.15)), MaxValueValidator(Decimal(0.4))]

class NamesLayouts(models.TextChoices):
    TRIANGULAR = "triangular"
    ROTATED = "rotated"
    SQUARE = "square"
        

class Layout(models.Model):
    name = models.CharField(max_length=256, choices=NamesLayouts)
    angle = models.FloatField()
    description = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}-{self.angle}"
class TubeDiameter(models.Model):
    diameter_meters = models.FloatField()
    diameter_inch = models.FloatField()

    description = models.CharField(max_length=256,null=True)

    def __str__(self) -> str:
        return f'{self.description}'
class TubeInternDiameter(models.Model):
    intern_diameter_meters = models.FloatField(null=True)
    intern_diameter_inch = models.FloatField(null=True)
    tube_diameter = models.ForeignKey(TubeDiameter, null=True, on_delete=models.CASCADE)
    standard = models.CharField(max_length=100)
    description = models.CharField(max_length=256,null=True)
    tube_thickness_inch = models.FloatField(null=True)

    def __str__(self) -> str:
        return f'{self.tube_diameter}-{self.standard}'

class ConstantsB(models.Model):
    reynolds_min = models.FloatField()
    reynolds_max = models.FloatField()
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    b1 = models.FloatField()
    b2 = models.FloatField()
    b3 = models.FloatField()
    b4 = models.FloatField()

class ConstantsA(models.Model):
    reynolds_min = models.FloatField()
    reynolds_max = models.FloatField()
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    a1 = models.FloatField()
    a2 = models.FloatField()
    a3 = models.FloatField()
    a4 = models.FloatField()

class LiLo(models.Model):
    pressure_class_pascal = models.FloatField()
    pressure_class_psi = models.FloatField()
    li_meters = models.FloatField()
    lo_meters = models.FloatField()
    li_inch = models.FloatField()
    lo_inch = models.FloatField()
    Dc_meters = models.FloatField(null=True)
    Dc_inch = models.FloatField(null=True)

class Pitch(models.Model):
    de = models.ForeignKey(TubeDiameter, on_delete=models.CASCADE)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    pitch_meters = models.FloatField()
    pitch_inch = models.FloatField()
    pp_meters = models.FloatField()
    pp_inch = models.FloatField()
    pn_meters = models.FloatField()
    pn_inch = models.FloatField()
    description = models.CharField(max_length=256,null=True)

    def __str__(self) -> str:
        return f'{self.description}-{self.layout}'
    
class TubeCount(models.Model):
    Ds_meters = models.FloatField()
    Ds_inch = models.FloatField()
    Dotl_meters = models.FloatField()
    Dotl_inch = models.FloatField()
    de = models.ForeignKey(TubeDiameter, on_delete=models.CASCADE)
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    n1 = models.PositiveIntegerField(null=True, blank=True)
    n2 = models.PositiveIntegerField(null=True, blank=True)
    n4 = models.PositiveIntegerField(null=True, blank=True)
    n6 = models.PositiveIntegerField(null=True, blank=True)
    n8 = models.PositiveIntegerField(null=True, blank=True)


class DeltaSB(models.Model):
    Dn_min_meters = models.FloatField(unique=True)
    Dn_max_meters = models.FloatField(unique=True)
    Dn_min_inch = models.FloatField(unique=True)
    Dn_max_inch = models.FloatField(unique=True)
    DeltaSB_meters = models.FloatField()
    DeltaSB_inch = models.FloatField()

class NozzleDiameter(models.Model):
    Dc_min_meters = models.FloatField(unique=True)
    Dc_max_meters = models.FloatField(unique=True)
    Dc_min_inch = models.FloatField(unique=True)
    Dc_max_inch = models.FloatField(unique=True)
    nozzle_diameter_meters = models.FloatField()
    nozzle_diameter_inch = models.FloatField()

class TubeMaterial(models.Model):
    group = models.IntegerField(choices=[(1, "GRUPO 1"), (2, "GRUPO 2")], help_text="De acordo com tabela TEMA - RCB-4.5.2")
    material = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.material}-{self.group}'


class InputsShellAndTube(models.Model):
    class TubePasses(models.IntegerChoices):
        ONE = 1, "Uma Passagem nos tubos"
        TWO = 2, "Duas Passagem nos tubos"
        FOUR = 4, "Quatro Passagem nos tubos"
        SIX = 6, "Seis Passagem nos tubos"
        EIGHT = 8, "Oito Passagem nos tubos"

    def get_ds_inch_choices():
        choices = [(value, value) for value in TubeCount.objects.values_list('Ds_inch', flat=True).distinct()]
        return choices
    
    T1_hot = models.FloatField()
    T2_hot = models.FloatField()

    t1_cold = models.FloatField()
    t2_cold = models.FloatField()

    wq = models.FloatField()
    wf = models.FloatField()
    
    cp_quente = models.FloatField()
    cp_frio = models.FloatField()

    casco_passagens = models.IntegerField()

    rho_q = models.FloatField()
    rho_f = models.FloatField()

    mi_q = models.FloatField()
    mi_f = models.FloatField()

    k_q = models.FloatField()
    k_f = models.FloatField()

    Rd_q = models.FloatField()
    Rd_f = models.FloatField()
    
    tipo_q = models.CharField(max_length=256)
    tipo_f = models.CharField(max_length=256)

    n = models.IntegerField(choices=TubePasses.choices, help_text='Número de passagens nos tubos', null=True)
    di = models.ForeignKey(TubeInternDiameter, null=True, on_delete=models.CASCADE)
    pitch = models.ForeignKey(Pitch, null=True, on_delete=models.CASCADE)

    Ds_inch = models.FloatField(null=True, choices=get_ds_inch_choices)
    
    L = models.FloatField(null=True)

    shell_fluid = models.CharField(choices=[("hot", "hot"), ("cold", "cold")], null=True, max_length=4)

    ls_percent = models.DecimalField(
        max_digits=4, 
        decimal_places=3, 
        validators=PERCENTAGE_VALIDATOR, 
        null=True, 
        help_text="Espaçamento entre defletores em funçao do diametro interno do trocador (Ds) (%)"
    )

    lc_percent = models.DecimalField(
        max_digits=4, 
        decimal_places=3, 
        validators=CORTE_DEFLETOR, 
        null=True, 
        help_text="Corte defeltor em funçao do comprimento do diâmetro  (L) do trocador (%)"
    )


    shell_thickness_meters = models.FloatField(null=True)

    tube_material = models.ForeignKey(TubeMaterial, null=True, on_delete=models.CASCADE)

    pressure_class = models.FloatField(choices=[(150.0, '150 psi'), (600.0, "600 psi")], null=True)

    reference = models.TextField(default="")