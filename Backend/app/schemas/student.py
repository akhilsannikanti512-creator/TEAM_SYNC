from pydantic import BaseModel

class StudentCreate(BaseModel):
    pin: str
    name: str
    email: str
    track: str
    skill: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True