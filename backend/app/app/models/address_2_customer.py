"""Address 2 customer database model."""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base
from app.database.mixins import AssociationMixin


class Address2Customer(Base, AssociationMixin):
    """Class that represents the assignment of addresses to customers."""
    __tablename__ = 'address_2_customer'

    customer_id = Column(Integer, ForeignKey('customer.id'), primary_key=True, index=True)
    address_id = Column(Integer, ForeignKey('address.id'), primary_key=True, index=True)

    customer = relationship('Customer', backref='address_associations', foreign_keys=[customer_id])
    address = relationship('Address', backref='customer_associations', foreign_keys=[address_id])
