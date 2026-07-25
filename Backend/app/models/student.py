from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime

from app.database.database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    pin = Column(String(20), unique=True)

    name = Column(String(100))

    email = Column(String(100), unique=True)

    track = Column(String(30))

    skill = Column(String(20))

    created_at = Column(DateTime, default=datetime.utcnow)