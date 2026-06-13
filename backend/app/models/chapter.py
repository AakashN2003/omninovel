from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)

    novel_id = Column(Integer, ForeignKey("novels.id"))

    chapter_number = Column(Integer)
    title = Column(String(255))
    content = Column(Text)