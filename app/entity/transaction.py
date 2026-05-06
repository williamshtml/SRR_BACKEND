from sqlalchemy import Column, String, Numeric, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base # Corregido: apunta a config.database
from datetime import datetime
import uuid

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True)
    organization_id = Column(UUID(as_uuid=True), nullable=False)
    source_id = Column(Integer, nullable=True)
    captured_by = Column(String, nullable=True)
    forwarded_by = Column(String, nullable=True)
    raw_message = Column(String)
    amount = Column(Numeric(10, 2))
    sender_name = Column(String)
    unique_hash = Column(String, unique=True)
    sync_method = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)