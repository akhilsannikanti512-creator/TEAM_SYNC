from pydantic import BaseModel


class TeamMemberResponse(BaseModel):
    student_id: int

    class Config:
        from_attributes = True


class TeamResponse(BaseModel):
    id: int
    team_name: str
    track: str

    class Config:
        from_attributes = True