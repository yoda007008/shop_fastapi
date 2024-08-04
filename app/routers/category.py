from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

router = APIRouter(prefix="/category", tags=["category"])

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

@router.get("/all_categories")
async def get_all_categories():
    pass

@router.post("/create")
async def create_category():
    pass

@router.put("/update_category")
async def update_category():
    pass

@router.delete("/delete")
async def delete_category():
    pass