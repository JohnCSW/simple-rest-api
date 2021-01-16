from dataclasses import dataclass

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from entity.base import Base


@dataclass
class Order(Base):
    __tablename__ = 'orders'
    orderNumber: int = Column(Integer, primary_key=True)
    customerNumber: int = Column(Integer, ForeignKey('customers.customerNumber'))
    customer = relationship('Customer')
    status: str = Column(String(15))
    comments: str = Column(String(50))
    orderDate: Date = Column(Date)
    requiredDate: Date = Column(Date)
    shippedDate: Date = Column(Date)
