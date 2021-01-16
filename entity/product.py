from dataclasses import dataclass
from unicodedata import numeric

from sqlalchemy import Column, String, Integer, Date, ForeignKey, SmallInteger, Numeric
from sqlalchemy.orm import relationship

from entity.base import Base


@dataclass
class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}
    productCode: str = Column(String(15), primary_key=True)
    productName: str = Column(String(70))
    productLine: str = Column(String(50))
    productScale: str = Column(String(10))
    productVendor: str = Column(String(50))
    productDescription: str = Column(String(50))
    quantityInStock: int = Column(SmallInteger)
    buyPrice: numeric = Column(Numeric(2, 10))
    MSRP: numeric = Column(Numeric(10, 2))
