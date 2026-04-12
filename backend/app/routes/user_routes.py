from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user_schema import UserCreate, UserBase, UserResponse, UserUpdate
from app.services.user_service import create_user, update_user, get_user_by_id, list_users, delete_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(user_id:int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return user

@router.get("/", response_model=list[UserResponse])
def list_all(db: Session = Depends(get_db)):
    return list_users(db)

@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    try:
        return update_user(db, user_id, user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return {"message": "Usuario deletado"}