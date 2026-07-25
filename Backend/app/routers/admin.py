from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.admin import AdminCreate
from app.services.admin_service import AdminService

router = APIRouter()


@router.post("/register")
def register(
    admin: AdminCreate,
    db: Session = Depends(get_db)
):

    service = AdminService(db)

    return service.create_admin(
        admin.username,
        admin.password
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    service = AdminService(db)

    result = service.login(
        form_data.username,
        form_data.password
    )

    if result is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return result