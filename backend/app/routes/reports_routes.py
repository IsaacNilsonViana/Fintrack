from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.reports_service import get_balance_by_account, get_expenses_by_category, get_balance_by_month

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/account/{account_id}")
def by_account(account_id: int, user_id:int, db: Session = Depends(get_db)):
    try:
        return get_balance_by_account(db, account_id, user_id)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail=str(e))
    
@router.get("/category/{user_id}")
def by_category(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_expenses_by_category(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/month/{user_id}")
def by_month(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_balance_by_month(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))