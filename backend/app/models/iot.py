from sqlalchemy import Column, String, Integer, DateTime, Boolean
from app.models import Base
from datetime import datetime


class IoTDevice(Base):
    __tablename__ = "iot_devices"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
    room = Column(String, nullable=True)
    state = Column(String, default="off")
    is_online = Column(Boolean, default=False)
