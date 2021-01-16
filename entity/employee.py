from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from entity.base import Base
from entity.customer import Customer


@dataclass
class Employee(Base):
    __tablename__ = 'employees'
    employeeNumber: int = Column(Integer, primary_key=True)
    lastName: str = Column(String(50))
    firstName: str = Column(String(50))
    extension: str = Column(String(50))
    email: str = Column(String(50))
    officeCode: str = Column(String(10))
    reportsTo: int = Column(Integer)
    customersReportTo: List[Customer] = relationship(
        'Customer', back_populates='salesRepEmployee'
    )
    jobTitle: str = Column(String(50))