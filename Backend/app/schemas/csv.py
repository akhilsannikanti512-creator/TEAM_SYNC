from pydantic import BaseModel


class CSVResponse(BaseModel):
    message: str
    imported_students: int