import sys
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import crud
import schemas
from models import Base, Item, Category

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope='function')
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_item(db):
    item_data = schemas.ItemCreate(title="Test Item", description="Test Description", price=10.0, category_id=1)
    item = crud.create_item(db=db, item=item_data)
    assert item.title == "Test Item"
    assert item.description == "Test Description"
    assert item.price == 10.0
    assert item.category_id == 1

def test_get_item(db):
    item_data = schemas.ItemCreate(title="Test Item", description="Test Description", price=10.0, category_id=1)
    item = crud.create_item(db=db, item=item_data)
    fetched_item = crud.get_item(db=db, item_id=item.id)
    assert fetched_item.id == item.id

def test_update_item(db):
    item_data = schemas.ItemCreate(title="Test Item", description="Test Description", price=10.0, category_id=1)
    item = crud.create_item(db=db, item=item_data)
    item_update = schemas.ItemUpdate(title="Updated Item")
    updated_item = crud.update_item(db=db, item_id=item.id, item_update=item_update)
    assert updated_item.title == "Updated Item"

def test_delete_item(db):
    item_data = schemas.ItemCreate(title="Test Item", description="Test Description", price=10.0, category_id=1)
    item = crud.create_item(db=db, item=item_data)
    deleted_item = crud.delete_item(db=db, item_id=item.id)
    assert deleted_item.id == item.id
    
    with pytest.raises(NoResultFound):
        db.query(Item).filter(Item.id == item.id).one()

def test_create_category(db):
    category_data = schemas.CategoryCreate(name="Test Category")
    category = crud.create_category(db=db, category=category_data)
    assert category.name == "Test Category"

def test_get_category(db):
    category_data = schemas.CategoryCreate(name="Test Category")
    category = crud.create_category(db=db, category=category_data)
    fetched_category = crud.get_category(db=db, category_id=category.id)
    assert fetched_category.id == category.id

def test_delete_category(db):
    category_data = schemas.CategoryCreate(name="Test Category")
    category = crud.create_category(db=db, category=category_data)
    deleted_category = crud.delete_category(db=db, category_id=category.id)
    assert deleted_category.id == category.id
    
    with pytest.raises(NoResultFound):
        db.query(Category).filter(Category.id == category.id).one()
