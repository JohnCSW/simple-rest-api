from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .order import Order


@dataclass
class Customer(Base):
    __tablename__ = 'customers'
    customerNumber: int = Column(Integer, primary_key=True)
    customerName: str = Column(String(50))
    contactLastName: str = Column(String(50))
    contactFirstName: str = Column(String(50))
    phone: str = Column(String(50))
    addressLine1: str = Column(String(50))
    addressLine2: str = Column(String(50))
    city: str = Column(String(50))
    state: str = Column(String(50))
    postalCode: str = Column(String(50))
    country: str = Column(String(15))
    salesRepEmployeeNumber: int = Column(Integer, ForeignKey('employees.reportsTo'))
    salesRepEmployee= relationship('Employee')
    creditLimit: float = Column(Float(precision=2))
    orders: List[Order] = relationship(
        'Order', back_populates='customer'
    )
