from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.csv_service import CSVService
from app.utils.auth import get_current_admin

router = APIRouter()


@router.post("/import")
async def import_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):
    service = CSVService(db)

    contents = await file.read()

    return service.import_students(contents)