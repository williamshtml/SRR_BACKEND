from fastapi import FastAPI
# Cambiamos 'transaction_controller' por 'controller'
from app.controller.controller import router as transaction_router

app = FastAPI(title="SRR Backend v2.0")

app.include_router(transaction_router)

@app.get("/")
async def root():
    return {"message": "SRR Backend Online - Ready for Data Ferrying"}