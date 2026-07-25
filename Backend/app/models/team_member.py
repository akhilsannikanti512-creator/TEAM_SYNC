from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class TeamMember(Base):

    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True, index=True)

    team_id = Column(Integer, ForeignKey("teams.id"))

    student_id = Column(Integer, ForeignKey("students.id"))

    team = relationship(
        "Team",
        back_populates="members"
    )