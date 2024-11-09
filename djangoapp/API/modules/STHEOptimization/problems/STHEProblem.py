

from API.modules.CascoTubo import CascoTubo
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Choice, Binary
from API.models import*
from uuid import uuid4

class STHEProblem(ElementwiseProblem):

    def __init__(self, inputs_shell_and_tube_id, **kwargs):
        self.calculation_id = uuid4()
        self.initial_inputs = InputsShellAndTube.objects.get(id=inputs_shell_and_tube_id).__dict__

        tube_material_ids = tuple(TubeMaterial.objects.values_list('id', flat=True))
        ds_inch_options = tuple(TubeCount.objects.values_list('Ds_inch', flat=True).distinct())
        layout_ids = tuple(Layout.objects.values_list('id', flat=True))
        pitch_ids = tuple(Pitch.objects.values_list('id', flat=True))
        di_standard = tuple(TubeInternDiameter.objects.values_list('standard', flat=True).distinct())

        vars = {
            "shell_thickness_meters": Real(bounds=(0, 0.50)),
            "ls_percent": Real(bounds=DISTANCIA_DEFLETOR_VALUES),
            "lc_percent": Real(bounds=CORTE_DEFLETOR_VALUES),
            "L": Real(bounds=(0, 20)),

            "pressure_class": Choice(options=[150.0, 600.0]),
            "tube_material_id": Choice(options=tube_material_ids),
            "shell_fluid": Choice(options=tuple(ShellFluid.values)),
            "Ds_inch": Choice(options=ds_inch_options),
            "n": Choice(options=tuple(TubePasses.values)),
            # "layout_id": Choice(options=layout_ids),
            "pitch_id": Choice(options=pitch_ids),
            "di_standard": Choice(options=di_standard)
        }
        super().__init__(vars=vars, n_obj=1, **kwargs)


    def set_shte_inputs(self, X) -> InputsShellAndTube:
        inputs_sthe = InputsShellAndTube.objects.create(
            T1_hot = self.initial_inputs["T1_hot"],
            T2_hot = self.initial_inputs["T2_hot"],
            t1_cold = self.initial_inputs["t1_cold"],
            t2_cold = self.initial_inputs["t2_cold"],
            wq = self.initial_inputs["wq"],
            wf = self.initial_inputs["wf"],
            cp_quente = self.initial_inputs["cp_quente"],
            cp_frio = self.initial_inputs["cp_frio"],
            casco_passagens = self.initial_inputs["casco_passagens"],
            rho_q = self.initial_inputs["rho_q"],
            rho_f = self.initial_inputs["rho_f"],
            mi_q = self.initial_inputs["mi_q"],
            mi_f = self.initial_inputs["mi_f"],
            k_q = self.initial_inputs["k_q"],
            k_f = self.initial_inputs["k_f"],
            Rd_q = self.initial_inputs["Rd_q"],
            Rd_f = self.initial_inputs["Rd_f"],
            tipo_q = self.initial_inputs["tipo_q"],
            tipo_f = self.initial_inputs["tipo_f"],
            reference = self.initial_inputs["reference"],
            calculation_id = self.calculation_id,
            
            pressure_class = X["pressure_class"],
            shell_thickness_meters = X["shell_thickness_meters"],
            lc_percent = X["lc_percent"],
            ls_percent = X["ls_percent"],
            shell_fluid = X["shell_fluid"],
            L = X["L"],
            Ds_inch = X["Ds_inch"],
            n = X["n"],
            tube_material= TubeMaterial.objects.get(id=X["tube_material_id"]),
            
        )
        pitch = Pitch.objects.get(id= X["pitch_id"])
        de = pitch.de

        di = TubeInternDiameter.objects.filter(
            tube_diameter = de.id,
            standard = X["di_standard"]
        ).first()
        inputs_sthe.di = di
        inputs_sthe.pitch = pitch
        inputs_sthe.save()

        return inputs_sthe
    
    def STHE_calculte(self, input:InputsShellAndTube):

        shell_and_tube = CascoTubo(input)
        shell_and_tube.filtro_tubos()
        shell_and_tube.area_projeto()
        shell_and_tube.coef_global_min()
        shell_and_tube.conveccao_tubo()
        shell_and_tube.espacamento_defletor()
        shell_and_tube.corte_defletor()
        shell_and_tube.diametro_casco()
        shell_and_tube.conveccao_casco()
        shell_and_tube.calculo_temp_parede()
        shell_and_tube.coef_global_limpo()
        shell_and_tube.excesso_area()
        shell_and_tube.perda_carga_tubo()
        shell_and_tube.perda_carga_casco()

        return shell_and_tube