from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base


class Novel(Base):
    __tablename__ = "novels"

    id = Column(Integer, primary_key=True, index=True)
    universe_id = Column(Integer, ForeignKey("universes.id"))

    title = Column(String(255), nullable=False)
    description = Column(Text)
    genre = Column(String(100))
    status = Column(String(50), default="Planning")

    author = Column(String(255))
    total_chapters = Column(Integer, default=0)