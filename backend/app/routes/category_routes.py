from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services.category_service import create_category, get_category_by_id, list_category, update_category, delete_category

router = APIRouter(prefix="/category", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        return create_category(db, category)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{category_id}", response_model=CategoryResponse)
def get_by_id(category_id: int, db: Session = Depends(get_db)):
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="categoria não encontrada")
    return category

@router.get("/", response_model=list[CategoryResponse])
def list_all(user_id: int, db: Session = Depends(get_db)):
    return list_category(db, user_id)

@router.put("/{category_id}", response_model=CategoryResponse)
def update(category_id: int, category_data: CategoryUpdate, db:Session = Depends(get_db)):
    try:
        return update_category(db, category_id, category_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    category = delete_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="categoria não encontrada")
    return {"message": "Categoria deletada"}