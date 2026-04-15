from sqlalchemy import Column, String, Text, DateTime, Integer
from app.models import Base
from datetime import datetime


class Memory(Base):
    __tablename__ = "memories"

    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    memory_type = Column(String, nullable=False)
    importance = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
