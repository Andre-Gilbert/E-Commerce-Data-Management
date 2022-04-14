"""Product database model."""
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class Product(Base):
    """Class that represents products."""
    __tablename__ = 'product'

    item_number = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    category_id = Column(Integer, ForeignKey('category._id'), index=True)
    supplier_id = Column(Integer, ForeignKey('supplier._id'), index=True)

    category = relationship('Category', backref='products')
    supplier = relationship('Supplier', backref='products')
