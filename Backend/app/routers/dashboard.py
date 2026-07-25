from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.dashboard_service import DashboardService
from app.utils.auth import get_current_admin

router = APIRouter()


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):

    service = DashboardService(db)

    return service.get_dashboard()