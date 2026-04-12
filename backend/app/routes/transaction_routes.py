from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.transaction_schemas import TransactionCreate, TransactionResponse, TransactionUpdate
from app.services.transaction_service import create_transaction, get_transaction_by_id, list_transaction, update_transaction, delete_transaction

router = APIRouter(prefix="/transactions", tags=["Transacrions"])

@router.post("/", response_model=TransactionResponse)
def create(transaction: TransactionCreate, db: Session = Depends(get_db)):
    try:
        return create_transaction(db, transaction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_by_id(transaction_id: int, db: Session = Depends(get_db)):
    transacion = get_transaction_by_id(db, transaction_id)
    if not transacion:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transacion

@router.get("/", response_model=list[TransactionResponse])
def list_all(user_id: int, db: Session = Depends(get_db)):
    return list_transaction(db, user_id)

@router.put("/{transaction_id}", response_model=TransactionResponse)
def update(transaction_id: int, transaction_data: TransactionUpdate, db: Session = Depends(get_db)):
    transaction = update_transaction(db, transaction_id, transaction_data)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transaction

@router.delete("/{transaction_id}")
def delete(transaction_id: int, db: Session = Depends(get_db)):
    transaction = delete_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return {"message": "Transação deletada"}