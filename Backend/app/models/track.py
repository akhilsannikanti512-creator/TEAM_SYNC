from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True, nullable=False)

    status = Column(String(20), default="Active")