from sqlalchemy import Column, String, DateTime, Boolean
from app.models import Base
from datetime import datetime


class SocialContact(Base):
    __tablename__ = "social_contacts"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    is_friend = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
