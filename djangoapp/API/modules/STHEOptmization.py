

from API.modules.CascoTubo import CascoTubo
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Choice, Binary
from API.models import*


class STHEProblem(ElementwiseProblem):

    def __init__(self, **kwargs):
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