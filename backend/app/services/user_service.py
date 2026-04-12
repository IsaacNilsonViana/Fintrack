from sqlalchemy.orm import Session
from hashlib import sha256

from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate

def create_user(db: Session, user_data: UserCreate):

    existing = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing:
        raise ValueError("Email já cadastrado")
    
    db_user = User(
        name = user_data.name,
        email = user_data.email,
        phone = user_data.phone,
        password_hash=sha256(user_data.password.encode()).hexdigest() 
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user
    else:
        return None
    
def list_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None
    
    if user_data.name is not None:
        user.name = user_data.name
    
    if user_data.email is not None:
        user.email = user_data.email

    if user_data.phone is not None:
        user.phone = user_data.phone

    if user_data.password is not None:
        user.password_hash = sha256(user_data.password.encode()).hexdigest() 

    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None
    
    db.delete(user)
    db.commit()
    return True