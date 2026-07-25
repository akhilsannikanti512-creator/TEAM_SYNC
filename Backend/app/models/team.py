from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Team(Base):

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)

    team_name = Column(String(100), nullable=False)

    track = Column(String(100), nullable=False)

    members = relationship(
        "TeamMember",
        back_populates="team",
        cascade="all, delete"
    )