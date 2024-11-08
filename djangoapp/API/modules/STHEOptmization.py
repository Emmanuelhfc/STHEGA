

from API.modules.CascoTubo import CascoTubo
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Choice, Binary
from API.models import*
from uuid import uuid4

class STHEProblem(ElementwiseProblem):

    def __init__(self, inputs_shell_and_tube_id, **kwargs):
        self.calculation_id = uuid4()
        inputs = InputsShellAndTube.objects.get(id=inputs_shell_and_tube_id)

        self.T1_hot = inputs.T1_hot
        self.T2_hot = inputs.T2_hot
        self.t1_cold = inputs.t1_cold
        self.t2_cold = inputs.t2_cold
        self.wq = inputs.wq
        self.wf = inputs.wf
        self.cp_quente = inputs.cp_quente
        self.cp_frio = inputs.cp_frio
        self.casco_passagens = inputs.casco_passagens
        self.rho_q = inputs.rho_q
        self.rho_f = inputs.rho_f
        self.mi_q = inputs.mi_q
        self.mi_f = inputs.mi_f
        self.k_q = inputs.k_q
        self.k_f = inputs.k_f
        self.Rd_q = inputs.Rd_q
        self.Rd_f = inputs.Rd_f
        self.tipo_q = inputs.tipo_q
        self.tipo_f = inputs.tipo_f
        self.reference = inputs.reference

        tube_material_ids = tuple(TubeMaterial.objects.values_list('id', flat=True))
        ds_inch_options = tuple(TubeCount.objects.values_list('Ds_inch', flat=True).distinct())
        layout_ids = tuple(Layout.objects.values_list('id', flat=True))
        pitch_ids = tuple(Pitch.objects.values_list('id', flat=True))
        di_standard = tuple(TubeInternDiameter.objects.values_list('standard', flat=True).distinct())

        vars = {
            "pressure_class": Choice(options=[150.0, 600.0]),
            "shell_thickness_meters": Real(bounds=(0, 0.50)),
            "tube_material_ids": Choice(options=tube_material_ids),
            "lc_percent": Real(bounds=DISTANCIA_DEFLETOR_VALUES),
            "ls_percent": Real(bounds=CORTE_DEFLETOR_VALUES),
            "shell_fluid": Choice(options=tuple(ShellFluid.values)),
            "L": Real(bounds=(0, 20)),
            "Ds_inch": Choice(options=ds_inch_options),
            "n": Choice(options=tuple(TubePasses.values)),
            "layout_ids": Choice(options=layout_ids),
            "pitch_ids": Choice(options=pitch_ids),
            "di_standard": Choice(options=di_standard)
        }
        super().__init__(vars=vars, n_obj=1, **kwargs)

    
    def _evaluate(self, X, out, *args, **kwargs):
        b, x, z, y = X["b"], X["x"], X["z"], X["y"]

        f = z + y
        if b:
            f = 100 * f

        if x == "multiply":
            f = 10 * f

        out["F"] = f