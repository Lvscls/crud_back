from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: float
    category_id: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None

class Item(ItemBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: str

class Category(CategoryBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True

