from rest_framework import serializers
from API.models import Results
from pymoo.core.mixed import MixedVariableGA

class ResultsSerializer(serializers.ModelSerializer):
    L = serializers.SerializerMethodField()
    Ds_inch = serializers.SerializerMethodField()
    de = serializers.SerializerMethodField()
    n = serializers.SerializerMethodField()
    pitch = serializers.SerializerMethodField()

    class Meta:
        model = Results
        fields = (
            "id", "calculation_id", "inputs", "q", "R", "S", "F", "mldt", "deltaT", "Nt", 
            "Dotl", "Ds", "A_proj", "Ud_min", "area_one_tube", "area_tube", "Gt", 
            "Re_t", "Res", "tube_velocity", "hi", "hio", "pp", "pn", "ls", "lc", 
            "Dc", "delta_sb_meters", "d_bocal", "li", "lo", "lsi", "lso", "Sm", 
            "theta_b", "Scd", "delta_tb", "Dctl", "theta_ctl", "Fw", "Ntb", "Stb", 
            "Sbp", "Swg", "Stw", "Sw", "Nc", "Nss", "Ncw", "Nb", "Gc", "Pr_s", "ji", 
            "h_ideal", "Rlm", "Rs", "jl", "Fbp", "jb", "Ntc", "jr", "Fc", "jc", 
            "lsi_s", "lso_s", "js", "hs", "T_c", "tc", "tw", "Uc", "Us", "Rd_calc", 
            "A_nec", "Ea", "delta_Pr", "delta_Ptt", "delta_PT", "fi", "delta_Pbi", 
            "Rcl", "Rcb", "delta_Pc", "Rcs", "delta_Pe", "Ntw", "Dw", "delta_Pwi", 
            "delta_Pw", "delta_Ps", "objective_function_1", "objective_function_2", 
            "error", "constraint_ea_max", "constraint_ea_min", "created_date", "L",
            "Ds_inch", "de", "n", "pitch",
        )

    def get_L(self, instance: Results) -> float:
        return instance.inputs.L
    
    def get_Ds_inch(self, instance: Results) -> float:
        return instance.inputs.Ds_inch

    def get_de(self, instance: Results) -> str:
        return instance.inputs.pitch.de.description
    
    def get_n(self, instance: Results) -> int:
        return instance.inputs.n

    def get_pitch(self, instance: Results) -> int:
        return instance.inputs.pitch.description
    

    
