from app.database import Base, engine

import app.models.universe
import app.models.character
import app.models.novel
import app.models.chapter
import app.models.memory
import app.models.user

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")