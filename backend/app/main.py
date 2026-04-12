from fastapi import FastAPI
from app.routes.category_routes import router as category_router
from app.routes.user_routes import router as user_router
from app.routes.account_routes import router as account_router
from app.routes.transaction_routes import router as transaction_router
from app.routes.reports_routes import router as reports_router

app = FastAPI()
app.include_router(category_router)
app.include_router(user_router)
app.include_router(account_router)
app.include_router(transaction_router)
app.include_router(reports_router)

@app.get("/")
async def root():
    return {"message": "Fintrack API online"}