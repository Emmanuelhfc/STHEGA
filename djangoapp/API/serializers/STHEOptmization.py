
from rest_framework import serializers
from django.db import models
from API.serializers.inputs_shell_and_tube import InputsShellAndTube

from pymoo.operators.crossover.binx import BinomialCrossover
from pymoo.operators.crossover.sbx import SBX

class CrossoverRealOption(models.TextChoices):
    binx = "binx", "BinomialCrossover"
    dex = "dex", "Dex"
    erx = "erx", "EdgeRecombinationCrossover"
    erpx = "erpx", "ExponentialCrossover"
    hux = "hux", "HalfUniformCrossover"
    ox = "ox", "OrderCrossover"
    pcx = "pcx", "ParentCentricCrossover"
    spntx = "spntx", "SinglePointCrossover"
    tnptx = "tnptx", "TwoPointCrossover"
    sbx = "sbx", "SimulatedBinaryCrossover"
    ux = "ux", "UniformCrossover"

class CrossoverChoiceOption(models.TextChoices):
    binx = "binx", "BinomialCrossover"
    dex = "dex", "Dex"
    erx = "erx", "EdgeRecombinationCrossover"
    erpx = "erpx", "ExponentialCrossover"
    hux = "hux", "HalfUniformCrossover"
    ox = "ox", "OrderCrossover"
    pcx = "pcx", "ParentCentricCrossover"
    spntx = "spntx", "SinglePointCrossover"
    tnptx = "tnptx", "TwoPointCrossover"
    # sbx = "sbx", "SimulatedBinaryCrossover"
    ux = "ux", "UniformCrossover"





class OptimizationInputsSerializer(serializers.Serializer):
    
    inputs_shell_and_tube = serializers.IntegerField(help_text="ID do modelo InputsShellAndTube")
    crossover_choice_type = serializers.ChoiceField(
        CrossoverChoiceOption.choices, 
        default=CrossoverChoiceOption.ux,
        help_text = "Crossover que será aplicados para tipo Choice"
    )
    crossover_real_type = serializers.ChoiceField(
        CrossoverRealOption.choices, 
        default=CrossoverRealOption.sbx,
        help_text = "Crossover que será aplicados para tipo Real"
    )



