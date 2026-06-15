from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PartEntity(Base):
    __tablename__ = "parts"

    part_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(String, ForeignKey("parts.part_id"), nullable=True)
    quantity = Column(Integer, nullable=False)
    unit_weight = Column(Float, nullable=False)
    material = Column(String, nullable=False)