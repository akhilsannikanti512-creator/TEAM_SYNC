from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Admin(Base):

    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)

    password = Column(String(100), nullable=False)