from sqlalchemy.orm import Session
from app.models.user import User
from app.models.transaction import Transaction
from app.schemas.transaction_schemas import TransactionCreate

def create_transaction(db: Session, transaction: TransactionCreate):

    user = db.query(User).filter(
        User.id == transaction.user_id
    ).first()

    if not user:
        raise ValueError("Usuario não encontrado")
    
    db_transaction = Transaction(
        user_id=transaction.user_id,
        amount=transaction.amount,
        category_id=transaction.category_id,
        account_id=transaction.account_id,
        date=transaction.date,
        description=transaction.description
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction

def get_transaction_by_id(db: Session, transaction_id: int):
    
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    
    if transaction:
        return transaction
    else: 
        return None
    
def list_transaction(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()

def update_transaction(db: Session, transaction_id: int, transaction_data):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return None

    if transaction_data.amount is not None:
        transaction.amount = transaction_data.amount

    if transaction_data.category_id is not None:
        transaction.category_id = transaction_data.category_id

    if transaction_data.account_id is not None:
        transaction.account_id = transaction_data.account_id

    if transaction_data.date is not None:
        transaction.date = transaction_data.date

    if transaction_data.description is not None:
        transaction.description = transaction_data.description

    db.commit()
    db.refresh(transaction)
    return transaction

def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return None
    
    db.delete(transaction)
    db.commit()
    return True