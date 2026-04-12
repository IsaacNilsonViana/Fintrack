from sqlalchemy.orm import Session
from app.models.user import User
from app.models.transaction import Transaction
from app.schemas.transaction_schemas import TransactionCreate

from app.models.account import Account
from app.models.category import Category

def get_balance_by_account(db: Session, account_id: int, user_id: int):
    
    account = db.query(Account).filter(Account.id == account_id).filter(Account.user_id == user_id).first()

    if not account:
        raise ValueError("Conta não encontrada")
    
    transactions = db.query(Transaction).filter(Transaction.account_id == account_id,Transaction.user_id == user_id).all()

    soma = 0

    if not transactions:
        return soma

    for i in transactions:
        soma += i.amount

    return soma

def get_expenses_by_category(db: Session, user_id: int):

    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()

    result = {}

    for i in transactions:
        category = i.category.name
        if category in result:
            result[category] += i.amount
        
        else:
            result[category] = i.amount

    return result

def get_balance_by_month(db: Session, user_id: int):
    
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()

    result = {}

    for i in transactions:
        month = i.date.strftime("%Y-%m")
        if month in result:
            result[month] += i.amount
        
        else:
            result[month] = i.amount

    return result
    
