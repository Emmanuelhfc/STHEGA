import pint
import json
from dataBase.models import TubeLayout
from dataBase.connection import*
from sqlalchemy.orm import Session
from dataBase.models import li_lo, Pitch
from dataBase.models import*
from sqlalchemy import select

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# layout = TubeLayout.TRIANGULAR
# de_pol = 0.75
# passo_pol = 1
# Ds = 8.071

p = 0.0206248
layout = "TRIANGULAR"
de = 0.015875

stmt = select(Pitch).where(
    Pitch.pitch == p,
    Pitch.layout == layout,
    Pitch.de == de,
)

with Session(engine()) as session:
    print("Pn:-----", session.scalars(stmt).one().pn)
