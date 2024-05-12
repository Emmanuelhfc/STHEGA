from sqlalchemy.orm import DeclarativeBase
from dataBase.connection import engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from enum import Enum


Base = declarative_base()

class TubeLayout(Enum):
    TRIANGULAR = 1 # 30
    ROTATED_TRIANGULAR = 2  #60
    SQUARE = 3 # 90
    ROTATED_SQUARE = 4 #45

class AvaliationThermoInputs(Base):
    __tablename__ = "avaliation_thermo_input"
    id: Mapped[int] = mapped_column(primary_key=True)
    name_avaliation: Mapped[str] = mapped_column(String(30))

    T1: Mapped[float] = mapped_column(Float())
    T2: Mapped[float] = mapped_column(Float())
    mi_q: Mapped[float] = mapped_column(Float())
    cp_quente: Mapped[float] = mapped_column(Float())
    Rd_q: Mapped[float] = mapped_column(Float())
    k_q: Mapped[float] = mapped_column(Float())
    rho_q: Mapped[float] = mapped_column(Float())
    w_q: Mapped[float] = mapped_column(Float())
    tipo_q: Mapped[float] = mapped_column(String(30))
    fluid_side: Mapped[float] = mapped_column(String(30))

    thermo_inputs_cold: Mapped[Optional["AvaliationThermoInputsCold"]] = relationship(
        back_populates="thermo_inputs",
        cascade="delete"
    )

    design_inputs: Mapped[Optional["AvaliationDesignInputs"]] = relationship(
        back_populates="thermo_inputs",
        cascade="delete"
    )

    results: Mapped[Optional["AvaliationResults"]] = relationship(
        back_populates="thermo_inputs",
        cascade="delete"
    )

    def __repr__(self) -> str:
        return f"AvaliationthermoInputs(id={self.id!r}, name={self.name_avaliation!r})"

class AvaliationThermoInputsCold(Base):
    __tablename__ = "avaliation_thermo_inputs_cold"
    id: Mapped[int] = mapped_column(primary_key=True)

    t1: Mapped[float] = mapped_column(Float())
    t2: Mapped[float] = mapped_column(Float())
    mi_f: Mapped[float] = mapped_column(Float())
    cp_frio: Mapped[float] = mapped_column(Float())
    Rd_f: Mapped[float] = mapped_column(Float())
    k_f: Mapped[float] = mapped_column(Float())
    rho_f: Mapped[float] = mapped_column(Float())
    w_f: Mapped[float] = mapped_column(Float())
    tipo_f: Mapped[float] = mapped_column(String(30))
    fluid_side: Mapped[float] = mapped_column(String(30))
    
    thermo_inputs: Mapped["AvaliationThermoInputs"] = relationship(
        back_populates="thermo_inputs_cold",
    )
    thermo_inputs_id: Mapped[int] = mapped_column(ForeignKey("avaliation_thermo_input.id"))
 



class AvaliationDesignInputs(Base):
    __tablename__ = "avaliation_design_inputs"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    thermo_inputs_id: Mapped[int] = mapped_column(ForeignKey("avaliation_thermo_input.id"))
    thermo_inputs: Mapped["AvaliationThermoInputs"] = relationship(
        back_populates="design_inputs",
    )
    

class AvaliationResults(Base):
    __tablename__ = "avaliation_results"
    id: Mapped[int] = mapped_column(primary_key=True)

    thermo_inputs_id: Mapped[int] = mapped_column(ForeignKey("avaliation_thermo_input.id"))
    thermo_inputs: Mapped["AvaliationThermoInputs"] = relationship(
        back_populates="results",
    )

    # fullname: Mapped[Optional[str]]

class ConstantsAB(Base):
    __tablename__ = "constants_for_ab"
    id: Mapped[int] = mapped_column(primary_key=True)
    layout: Mapped[TubeLayout]
    Re_max: Mapped[float] = mapped_column(Float())
    Re_min: Mapped[float] = mapped_column(Float())
    a1: Mapped[float] = mapped_column(Float())
    a2: Mapped[float] = mapped_column(Float())
    a3: Mapped[float] = mapped_column(Float())
    a4: Mapped[float] = mapped_column(Float())

    b1: Mapped[float] = mapped_column(Float())
    b2: Mapped[float] = mapped_column(Float())
    b3: Mapped[float] = mapped_column(Float())
    b4: Mapped[float] = mapped_column(Float())

class NozzleDiameter(Base):
    __tablename__ = "nozzle_diameter"
    id: Mapped[int] = mapped_column(primary_key=True)
    Dc_max: Mapped[float] = mapped_column(Float())
    Dc_max_inch: Mapped[float] = mapped_column(Float())
    Dc_min: Mapped[float] = mapped_column(Float())
    Dc_min_inch: Mapped[float] = mapped_column(Float())
    d_nozzle: Mapped[float] = mapped_column(Float())
    d_nozzle_inch: Mapped[float] = mapped_column(Float())

class DeltaSB(Base):
    __tablename__ = "delta_sb"
    id: Mapped[int] = mapped_column(primary_key=True)
    Dn_max: Mapped[float] = mapped_column(Float())
    Dn_min: Mapped[float] = mapped_column(Float())
    Dn_max_inch: Mapped[float] = mapped_column(Float())
    Dn_min_inch: Mapped[float] = mapped_column(Float())
    Delta_sb: Mapped[float] = mapped_column(Float())
    Delta_sb_inch: Mapped[float] = mapped_column(Float())



class TubeCount(Base):
    __tablename__ = 'tube_count'
    id: Mapped[int] = mapped_column(primary_key=True)
    Ds: Mapped[float] = mapped_column(Float())
    Ds_inch: Mapped[float] = mapped_column(Float())
    Dotl: Mapped[float] = mapped_column(Float())
    Dotl_inch: Mapped[float] = mapped_column(Float())
    de: Mapped[float] = mapped_column(Float())
    de_inch: Mapped[float] = mapped_column(Float())
    pitch: Mapped[float] = mapped_column(Float())
    pitch_inch: Mapped[float] = mapped_column(Float())
    layout: Mapped[TubeLayout]
    n1: Mapped[int] = mapped_column(Integer())
    n2: Mapped[int] = mapped_column(Integer())
    n4: Mapped[int] = mapped_column(Integer())
    n6: Mapped[int] = mapped_column(Integer())
    n8: Mapped[int] = mapped_column(Integer())


class li_lo(Base):
    __tablename__ = 'li_lo'
    id: Mapped[int] = mapped_column(primary_key=True)
    pressure_class: Mapped[float] = mapped_column(Float())
    pressure_class_psi: Mapped[float] = mapped_column(Float())
    Dc: Mapped[float] = mapped_column(Float())
    Dc_inch: Mapped[float] = mapped_column(Float())
    li: Mapped[float] = mapped_column(Float())
    li_inch: Mapped[float] = mapped_column(Float())
    lo:  Mapped[float] = mapped_column(Float())
    lo_inch:  Mapped[float] = mapped_column(Float())

class Pitch(Base):
    __tablename__ = 'pitch'
    id: Mapped[int] = mapped_column(primary_key=True)
    de: Mapped[float] = mapped_column(Float())
    de_inch: Mapped[float] = mapped_column(Float())
    pitch: Mapped[float] = mapped_column(Float())
    pitch_inch: Mapped[float] = mapped_column(Float())
    layout: Mapped[TubeLayout]
    pp: Mapped[float] = mapped_column(Float())
    pp_inch: Mapped[float] = mapped_column(Float())
    pn: Mapped[float] = mapped_column(Float())
    pn_inch: Mapped[float] = mapped_column(Float())
    

# if __name__ == '__main__':
#     engine_ = engine()
#     Base.metadata.create_all(engine_)
    
   

# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

