import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

T1 = Q_(219, ureg.degF)
T2 = Q_(219, ureg.degF)
t1 = Q_(219, ureg.degF)s
T1 = Q_(219, ureg.degF)


print(a.to_base_units())