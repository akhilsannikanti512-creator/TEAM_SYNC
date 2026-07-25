from pydantic import BaseModel


class TrackCreate(BaseModel):
    name: str


class TrackResponse(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True