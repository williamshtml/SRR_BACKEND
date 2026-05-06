from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
# Importamos desde tu archivo 'service'
from app.service.service import TransactionService

router = APIRouter(prefix="/api/v1/sync", tags=["Mesh Sync"])

@router.post("/collect")
async def collect_transaction(payload: dict, db: AsyncSession = Depends(get_db)):
    return await TransactionService.process_sync(db, payload)