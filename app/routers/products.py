from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

router = APIRouter(prefix='/products', tags=['products'])


# new model
class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    rating = Column(Float)
    is_active = Column(Boolean, default=True)


@router.get('/')
async def all_products():
    pass


@router.post('/create')
async def create_product():
    pass


@router.get('/{category_slug}')
async def product_by_category(category_slug: str):
    pass


@router.get('/detail/{product_slug}')
async def product_detail(product_slug: str):
    pass


@router.put('/detail/{product_slug}')
async def update_product(product_slug: str):
    pass


@router.delete('/delete')
async def delete_product(product_id: int):
    pass