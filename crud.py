from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

import models, schemas

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
   return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items_by_category(db: Session, category_id: int):
  return db.query(models.Item).filter(models.Item.category_id == category_id).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item_update: schemas.ItemUpdate):
    try:
        
        db_item = db.query(models.Item).filter(models.Item.id == item_id).one()
        
        
        for key, value in item_update.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        
        
        db.commit()
        db.refresh(db_item)
        return db_item

    except NoResultFound:
        
        return None

def delete_item(db: Session, item_id: int):
    try:
        db_item = db.query(models.Item).filter(models.Item.id == item_id).one()
        db.delete(db_item)
        db.commit()
        return db_item
    except NoResultFound:
        return None


def get_categories(db: Session, skip: int = 0, limit: int = 100):
 return db.query(models.Category).offset(skip).limit(limit).all()

def get_category(db: Session, category_id: int):
  return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_category(db: Session, category: schemas.CategoryCreate):
   db_category = models.Category(**category.dict())
   db.add(db_category)
   db.commit()
   db.refresh(db_category)
   return db_category

def delete_category(db: Session, category_id: int):
    try:
        db_category = db.query(models.Category).filter(models.Category.id == category_id).one()
        db.delete(db_category)
        db.commit()
        return db_category
    except NoResultFound:
        return None
