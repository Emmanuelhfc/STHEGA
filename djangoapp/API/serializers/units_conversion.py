from rest_framework import serializers


units_list_input = [
    'degF', 'degC', 'degK',                # Temperaturas (Fahrenheit, Celsius, Kelvin)
    'Btu/(lb*degF)', 'J/(kg*degK)',        # Capacidade calorífica específica (Btu/lb.F, J/kg.K)
    'cP', 'kg/(m*s)', "lb/(ft*h)",                      # Viscosidade (cP, kg/(m.s))
    'h*ft^2*degF/Btu', 'degK*m^2/W',       # Resistência térmica (h.ft^2.F/Btu, K.m^2/W)
    'Btu/(h*ft*degF)', 'W/degK',           # Condutividade térmica (Btu/(h.ft.F), W/K)
    'lb/ft^3', 'kg/m^3',                   # Densidade (lb/ft^3, kg/m^3)
    'lb/h', 'kg/s',                         # Fluxo de massa (lb/h, kg/s)
    'BTU/h',
    'ft',
    'inch',
    'ft^2',
    'ft/s',
    'BTU/(degF*h*ft^2)',
    'lbf/(inch^2)',
]
units_list_output = [
    'si',
    'degF', 'degC', 'degK',                # Temperaturas (Fahrenheit, Celsius, Kelvin)
    'Btu/(lb*degF)', 'J/(kg*degK)',        # Capacidade calorífica específica (Btu/lb.F, J/kg.K)
    'cP', 'kg/(m*s)', "lb/(ft*h)",                      # Viscosidade (cP, kg/(m.s))
    'h*ft^2*degF/Btu', 'degK*m^2/W',       # Resistência térmica (h.ft^2.F/Btu, K.m^2/W)
    'Btu/(h*ft*degF)', 'W/degK',           # Condutividade térmica (Btu/(h.ft.F), W/K)
    'lb/ft^3', 'kg/m^3',                   # Densidade (lb/ft^3, kg/m^3)
    'lb/h', 'kg/s',                         # Fluxo de massa (lb/h, kg/s)
    'BTU/h',
    'ft',
    'inch',
    'ft^2',
    'ft/s',
    'BTU/(degF*h*ft^2)',
    'lbf/(inch^2)',
]

class UnitConversionSerializer(serializers.Serializer):
    input_value = serializers.FloatField()
    input_unit = serializers.ChoiceField(choices=units_list_input)
    output_value = serializers.FloatField(read_only=True)
    output_unit = serializers.ChoiceField(choices=units_list_output)
    