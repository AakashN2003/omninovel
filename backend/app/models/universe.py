from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Universe(Base):
    __tablename__ = "universes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    genre = Column(String(100))
    description = Column(Text)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )