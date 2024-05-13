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

print(str([1,123,123]))
