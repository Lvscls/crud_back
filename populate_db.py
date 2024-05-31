from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

def clear_db(db: Session):
    db.query(models.Item).delete()
    db.query(models.Category).delete()
    db.commit()


def populate_db():
    db = SessionLocal()
    
    clear_db(db)
    
    categories = [
        schemas.CategoryCreate(name="Électronique"),
        schemas.CategoryCreate(name="Livres"),
        schemas.CategoryCreate(name="Vêtements")
    ]
    
    for category in categories:
        db_category = models.Category(**category.dict())
        db.add(db_category)
    
    db.commit()

    items = [
        schemas.ItemCreate(title="Smartphone", description="Un smartphone Android", price=299.99, category_id=1),
        schemas.ItemCreate(title="Ordinateur portable", description="Un ordinateur portable puissant", price=999.99, category_id=1),
        schemas.ItemCreate(title="Roman", description="Un roman policier captivant", price=19.99, category_id=2),
        schemas.ItemCreate(title="T-shirt", description="Un T-shirt en coton", price=9.99, category_id=3)
    ]

    for item in items:
        db_item = models.Item(**item.dict())
        db.add(db_item)
    
    db.commit()
    db.close()
