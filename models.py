from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", back_populates="items")

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    
    items = relationship("Item", back_populates="category")
