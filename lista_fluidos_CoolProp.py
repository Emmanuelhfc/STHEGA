import CoolProp.CoolProp as CP

fluids = CP.get_global_param_string('FluidsList')

for x in fluids.split(','):
    print(x)