from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)

    universe_id = Column(
        Integer,
        ForeignKey("universes.id"),
        nullable=False
    )

    name = Column(String(255), nullable=False)

    title = Column(String(255))
    role = Column(String(100))

    race = Column(String(100))
    gender = Column(String(50))
    age = Column(Integer)

    personality = Column(Text)
    appearance = Column(Text)
    background = Column(Text)

    power_level = Column(String(100))

    description = Column(Text)