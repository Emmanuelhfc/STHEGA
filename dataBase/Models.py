from sqlalchemy.orm import DeclarativeBase
from dataBase.connection import engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

Base = declarative_base()

class AvaliationTermoInputs(Base):
    __tablename__ = "avaliation_termo_inputs"
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

    # back_populate é o campo que linka essa classe para outra
    # cascade  - definido que se um item desse model for deletado os itens linkados do outro modos serão deletados todos
    # "sem orfãos"
    design_inputs: Mapped[Optional["AvaliationDesignInputs"]] = relationship(
        back_populates="avaliation_termo_input",
        cascade="delete"
    )

    results: Mapped[Optional["AvaliationResults"]] = relationship(
        back_populates="avaliation_termo_input",
        cascade="delete"
    )

    def __repr__(self) -> str:
        return f"AvaliationTermoInputs(id={self.id!r}, name={self.name_avaliation!r})"
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

class AvaliationTermoInputsCold(Base):
    __tablename__ = "avaliation_termo_inputs_cold"
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

    seila: Mapped[float] = mapped_column(String(30))
    seila2: Mapped[float] = mapped_column(String(30))





class AvaliationDesignInputs(Base):
    __tablename__ = "avaliation_design_inputs"
    id: Mapped[int] = mapped_column(primary_key=True)
    seila2: Mapped[float] = mapped_column(String(30))
    termo_inputs: Mapped["AvaliationTermoInputs"] = relationship(
        back_populates="avaliation_design_input",
    )
    

class AvaliationResults(Base):
    __tablename__ = "avaliation_results"
    id: Mapped[int] = mapped_column(primary_key=True)

    termo_inputs: Mapped["AvaliationTermoInputs"] = relationship(
        back_populates="avaliation_result",
    )

    # fullname: Mapped[Optional[str]]


if __name__ == '__main__':
    engine_ = engine()
    Base.metadata.create_all(engine_)
    
   

# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

