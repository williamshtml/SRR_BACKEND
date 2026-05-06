from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.entity.transaction import Transaction

class TransactionRepository:
    @staticmethod
    async def save(db: AsyncSession, transaction: Transaction):
        db.add(transaction)
        await db.commit()
        await db.refresh(transaction)
        return transaction

    @staticmethod
    async def get_by_hash(db: AsyncSession, u_hash: str):
        result = await db.execute(select(Transaction).where(Transaction.unique_hash == u_hash))
        return result.scalars().first()