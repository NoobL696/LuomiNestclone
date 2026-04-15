from sqlalchemy import Column, String, Text, DateTime, Boolean
from app.models import Base
from datetime import datetime


class Plugin(Base):
    __tablename__ = "plugins"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    version = Column(String, nullable=False)
    is_enabled = Column(Boolean, default=True)
    installed_at = Column(DateTime, default=datetime.utcnow)
