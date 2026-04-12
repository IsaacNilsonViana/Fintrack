from sqlalchemy.orm import Session
from app.models.account import Account
from app.models.user import User
from app.schemas.account_schema import AccountCreate, AccountUpdate

def create_Account(db: Session, account: AccountCreate):

    user = db.query(User).filter(
        User.id == account.user_id
    ).first()

    if not user:
        raise ValueError("Usuario não encontrado")

    existing = db.query(Account).filter(
        Account.user_id == account.user_id,
        Account.name == account.name
    ).first()

    if existing:
        raise ValueError("Conta existente")

    db_account = Account(
        user_id=account.user_id,
        name=account.name,
        type=account.type
    )

    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return db_account

def get_Account_by_id(db: Session, Account_id: int):
    
    account = db.query(Account).filter(Account.id == Account_id).first()
    
    if account:
        return account
    else: 
        return None

def list_Account(db: Session, user_id: int):
    return db.query(Account).filter(Account.user_id == user_id).all()

def update_Account(db: Session, Account_id: int, Account_data):
    account = db.query(Account).filter(Account.id == Account_id).first()

    if not account:
        return None
    
    if Account_data.name is not None:
        account.name = Account_data.name

    if Account_data.type is not None:
        account.type = Account_data.type

    db.commit()
    db.refresh(account)
    return account

def delete_Account(db: Session, Account_id: int):
    account = db.query(Account).filter(Account.id == Account_id).first()

    if not account:
        return None
    
    db.delete(account)
    db.commit()
    return True