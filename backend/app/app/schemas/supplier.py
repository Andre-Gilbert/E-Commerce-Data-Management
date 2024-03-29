"""Supplier properties."""
from typing import Optional

from pydantic import BaseModel


# Shared properties
class SupplierBase(BaseModel):
    name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    address_id: Optional[int]


# Properties to receive via API on creation
class SupplierCreate(SupplierBase):
    name: str
    email: str
    address_id: int


# Properties to receive via API on update
class SupplierUpdate(SupplierBase):
    pass


class SupplierInDBBase(SupplierBase):
    id: int
    address_id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Supplier(SupplierInDBBase):
    pass


# Additional properties stored in DB
class SupplierInDB(SupplierInDBBase):
    pass
