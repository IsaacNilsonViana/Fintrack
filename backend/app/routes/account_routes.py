from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.account_schema import AccountCreate, AccountResponse, AccountUpdate
from app.services.account_service import create_Account, get_Account_by_id, list_Account, update_Account, delete_Account

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/", response_model=AccountResponse)
def create(account: AccountCreate, db: Session = Depends(get_db)):
    try:
        return create_Account(db, account)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{account_id}", response_model=AccountResponse)
def get_by_id(account_id: int, db: Session = Depends(get_db)):
    account = get_Account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account

@router.get("/", response_model=list[AccountResponse])
def list_all(user_id: int, db: Session = Depends(get_db)):
    return list_Account(db, user_id)

@router.put("/{account_id}", response_model=AccountResponse)
def update(account_id: int, account_data: AccountUpdate, db: Session = Depends(get_db)):
    account = update_Account(db, account_id, account_data)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account

@router.delete("/{account_id}")
def delete(account_id: int, db: Session = Depends(get_db)):
    account = delete_Account(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return {"message": "Conta deletada"}