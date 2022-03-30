"""API version 1."""
from fastapi import APIRouter
from app.api.api_v1.endpoints import products

router = APIRouter()
router.include_router(products.router, prefix='/products', tags=['Products'])
