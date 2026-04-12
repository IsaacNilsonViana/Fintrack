from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category_schema import CategoryCreate

def create_category(db: Session, category: CategoryCreate):

    existing = db.query(Category).filter(
        Category.user_id == category.user_id,
        Category.name == category.name
    ).first()

    if existing:
        raise ValueError("Categoria existente")

    db_category = Category(
        user_id=category.user_id,
        name=category.name,
        type=category.type
    )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category

def get_category_by_id(db: Session, category_id: int):
    
    categoria = db.query(Category).filter(Category.id == category_id).first()
    
    if categoria:
        return categoria
    else: 
        return None

def list_category(db: Session, user_id: int):
    return db.query(Category).filter(Category.user_id == user_id).all()

def update_category(db: Session, category_id: int, category_data):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        return None
    
    if category_data.name is not None:
        category.name = category_data.name

    if category_data.type is not None:
        category.type = category_data.type

    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        return None
    
    db.delete(category)
    db.commit()
    return True