from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone


CORTE_DEFLETOR_VALUES = (0.15, 0.4)

CORTE_DEFLETOR = [MinValueValidator(Decimal(CORTE_DEFLETOR_VALUES[0])), MaxValueValidator(Decimal(CORTE_DEFLETOR_VALUES[1]))]

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
        return f'[{self.de.description}] [{self.layout.name}] [{self.description}]'
    
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
    

class TubePasses(models.IntegerChoices):
        ONE = 1, "Uma Passagem nos tubos"
        TWO = 2, "Duas Passagens nos tubos"
        FOUR = 4, "Quatro Passagens nos tubos"
        SIX = 6, "Seis Passagens nos tubos"
        EIGHT = 8, "Oito Passagens nos tubos"

class ShellFluid(models.TextChoices):
    hot = ("hot", "hot")
    cold = ("cold", "cold")

class InputsShellAndTube(models.Model):
    def get_ds_inch_choices():
        choices = [(value, value) for value in TubeCount.objects.values_list('Ds_inch', flat=True).distinct()]
        return choices
    
    calculation_id = models.UUIDField(null=True, blank=True)
    T1_hot = models.FloatField()
    T2_hot = models.FloatField()
    t1_cold = models.FloatField()
    t2_cold = models.FloatField()
    wq = models.FloatField()
    wf = models.FloatField()
    cp_quente = models.FloatField()
    cp_frio = models.FloatField()
    casco_passagens = models.IntegerField(default=1)
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

    n = models.IntegerField(choices=TubePasses.choices, help_text='Número de passagens nos tubos', null=True, blank=True)
    di = models.ForeignKey(TubeInternDiameter, null=True, on_delete=models.CASCADE, blank=True)
    pitch = models.ForeignKey(Pitch, null=True, on_delete=models.CASCADE, blank=True)
    Ds_inch = models.FloatField(null=True, choices=get_ds_inch_choices, blank=True)
    L = models.FloatField(null=True, blank=True)
    shell_fluid = models.CharField(choices=ShellFluid.choices, null=True, max_length=4, blank=True)
    ls_percent = models.DecimalField(
        max_digits=4, 
        decimal_places=3,  
        null=True, 
        help_text="Espaçamento entre defletores em funçao do diametro interno do trocador (Ds) (%)",
        blank=True
    )
    lc_percent = models.DecimalField(
        max_digits=4, 
        decimal_places=3, 
        validators=CORTE_DEFLETOR, 
        null=True, 
        help_text="Corte defeltor em funçao do comprimento do diâmetro  (L) do trocador (%)",
        blank=True,
    )
    shell_thickness_meters = models.FloatField(null=True, blank=True)
    tube_material = models.ForeignKey(TubeMaterial, null=True, on_delete=models.CASCADE, blank=True)
    pressure_class = models.FloatField(choices=[(150.0, '150 psi'), (600.0, "600 psi")], null=True, blank=True)

    reference = models.TextField(default="", blank=True)

    perda_carga_admissivel_casco = models.FloatField(default=0, blank=True)
    perda_carga_admissivel_tubo = models.FloatField(default=0, blank=True)

class Results(models.Model):
    calculation_id = models.UUIDField(null=True, blank=True)
    inputs = models.ForeignKey(InputsShellAndTube, on_delete=models.CASCADE)
    q = models.FloatField(blank=True, null=True)
    R = models.FloatField(blank=True, null=True)
    S = models.FloatField(blank=True, null=True)
    F = models.FloatField(blank=True, null=True)
    mldt = models.FloatField(blank=True, null=True)
    deltaT = models.FloatField(blank=True, null=True)
    Nt = models.FloatField(blank=True, null=True)
    Dotl = models.FloatField(blank=True, null=True)
    Ds = models.FloatField(blank=True, null=True)
    A_proj = models.FloatField(blank=True, null=True)
    Ud_min = models.FloatField(blank=True, null=True)
    area_one_tube = models.FloatField(blank=True, null=True)
    area_tube = models.FloatField(blank=True, null=True)
    Gt = models.FloatField(blank=True, null=True)
    Re_t = models.FloatField(blank=True, null=True)
    Res = models.FloatField(blank=True, null=True)
    tube_velocity = models.FloatField(blank=True, null=True)
    hi = models.FloatField(blank=True, null=True)
    hio = models.FloatField(blank=True, null=True)
    pp = models.FloatField(blank=True, null=True)
    pn = models.FloatField(blank=True, null=True)
    ls = models.FloatField(blank=True, null=True)
    lc = models.FloatField(blank=True, null=True)
    Dc = models.FloatField(blank=True, null=True)
    delta_sb_meters = models.FloatField(blank=True, null=True)
    d_bocal = models.FloatField(blank=True, null=True)
    li = models.FloatField(blank=True, null=True)
    lo = models.FloatField(blank=True, null=True)
    lsi = models.FloatField(blank=True, null=True)
    lso = models.FloatField(blank=True, null=True)
    Sm = models.FloatField(blank=True, null=True)
    theta_b = models.FloatField(blank=True, null=True)
    Scd = models.FloatField(blank=True, null=True)
    delta_tb = models.FloatField(blank=True, null=True)
    Dctl = models.FloatField(blank=True, null=True)
    theta_ctl = models.FloatField(blank=True, null=True)
    Fw = models.FloatField(blank=True, null=True)
    Ntb = models.FloatField(blank=True, null=True)
    Stb = models.FloatField(blank=True, null=True)
    Sbp = models.FloatField(blank=True, null=True)
    Swg = models.FloatField(blank=True, null=True)
    Stw = models.FloatField(blank=True, null=True)
    Sw = models.FloatField(blank=True, null=True)
    Nc = models.FloatField(blank=True, null=True)
    Nss = models.FloatField(blank=True, null=True)
    Ncw = models.FloatField(blank=True, null=True)
    Nb = models.FloatField(blank=True, null=True)
    Gc = models.FloatField(blank=True, null=True)
    Pr_s = models.FloatField(blank=True, null=True)
    ji = models.FloatField(blank=True, null=True)
    h_ideal = models.FloatField(blank=True, null=True)
    Rlm = models.FloatField(blank=True, null=True)
    Rs = models.FloatField(blank=True, null=True)
    jl = models.FloatField(blank=True, null=True)
    Fbp = models.FloatField(blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    Ntc = models.FloatField(blank=True, null=True)
    jr = models.FloatField(blank=True, null=True)
    Fc = models.FloatField(blank=True, null=True)
    jc = models.FloatField(blank=True, null=True)
    lsi_s = models.FloatField(blank=True, null=True)
    lso_s = models.FloatField(blank=True, null=True)
    js = models.FloatField(blank=True, null=True)
    hs = models.FloatField(blank=True, null=True)
    T_c = models.FloatField(blank=True, null=True)
    tc = models.FloatField(blank=True, null=True)
    tw = models.FloatField(blank=True, null=True)
    Uc = models.FloatField(blank=True, null=True)
    Us = models.FloatField(blank=True, null=True)
    Rd_calc = models.FloatField(blank=True, null=True)
    A_nec = models.FloatField(blank=True, null=True)
    Ea = models.FloatField(blank=True, null=True)
    delta_Pr = models.FloatField(blank=True, null=True)
    delta_Ptt = models.FloatField(blank=True, null=True)
    delta_PT = models.FloatField(blank=True, null=True)
    fi = models.FloatField(blank=True, null=True)
    delta_Pbi = models.FloatField(blank=True, null=True)
    Rcl = models.FloatField(blank=True, null=True)
    Rcb = models.FloatField(blank=True, null=True)
    delta_Pc = models.FloatField(blank=True, null=True)
    Rcs = models.FloatField(blank=True, null=True)
    delta_Pe = models.FloatField(blank=True, null=True)
    Ntw = models.FloatField(blank=True, null=True)
    Dw = models.FloatField(blank=True, null=True)
    delta_Pwi = models.FloatField(blank=True, null=True)
    delta_Pw = models.FloatField(blank=True, null=True)
    delta_Ps = models.FloatField(blank=True, null=True)

    objective_function_1 = models.FloatField(blank=True, null=True)
    objective_function_2 = models.FloatField(blank=True, null=True)
    error = models.BooleanField(default=False)

    constraint_ea_max = models.FloatField(blank=True, null=True)
    constraint_ea_min = models.FloatField(blank=True, null=True)
    
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Results {self.id}"


class File(models.Model):
    file = models.FileField()

class Charts(models.Model):
    calculation_id = models.UUIDField(null=True, blank=True)
    files = models.ManyToManyField(File)
    csv = models.ForeignKey(File, blank=True, null=True, on_delete=models.SET_NULL, related_name='chart_csv')