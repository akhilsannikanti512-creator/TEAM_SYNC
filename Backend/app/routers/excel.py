from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.excel_service import ExcelService
from app.utils.auth import get_current_admin

router = APIRouter()


@router.get("/export")
def export_excel(
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):

    service = ExcelService(db)

    filename = service.export_teams()

    return FileResponse(
        path=filename,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )