from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class MemoryEntry(Base):
    __tablename__ = "memory_entries"

    id = Column(Integer, primary_key=True, index=True)

    universe_id = Column(Integer, ForeignKey("universes.id"))

    memory_type = Column(String(50))
    content = Column(Text)