import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.entity.transaction import Transaction
from app.repository.repository import TransactionRepository
from app.util.util import generate_transaction_hash

class TransactionService:
    @staticmethod
    async def process_sync(db: AsyncSession, payload: dict):
        # Generar hash para evitar duplicados
        u_hash = generate_transaction_hash(
            payload.get('amount'), 
            payload.get('sender_name'), 
            payload.get('raw_message')
        )

        # Verificar si ya existe
        existing = await TransactionRepository.get_by_hash(db, u_hash)
        if existing:
            return {"status": "ignored", "message": "Transacción duplicada"}

        # Convertir organization_id a objeto UUID
        org_id_str = payload.get('organization_id')
        try:
            org_uuid = uuid.UUID(org_id_str)
        except (ValueError, TypeError):
            # UUID de respaldo si el del payload falla
            org_uuid = uuid.UUID('0867deaf-f92c-45f0-8fc9-6167d0cb2638')

        # Crear nueva transacción
        new_tx = Transaction(
            id=str(uuid.uuid4()),
            organization_id=org_uuid,
            source_id=payload.get('source_id'),
            captured_by=payload.get('captured_by'),
            forwarded_by=payload.get('forwarded_by'),
            raw_message=payload.get('raw_message'),
            amount=payload.get('amount'),
            sender_name=payload.get('sender_name'),
            unique_hash=u_hash,
            sync_method=payload.get('sync_method', 'DIRECT')
        )

        await TransactionRepository.save(db, new_tx)
        return {"status": "success", "id": new_tx.id}