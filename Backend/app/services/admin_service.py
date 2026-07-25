from sqlalchemy.orm import Session

from app.models.admin import Admin
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)


class AdminService:

    def __init__(self, db: Session):
        self.db = db

    def create_admin(self, username: str, password: str):

        existing = (
            self.db.query(Admin)
            .filter(Admin.username == username)
            .first()
        )

        if existing:
            return {
                "message": "Admin already exists"
            }

        admin = Admin(
            username=username,
            password=hash_password(password)
        )

        self.db.add(admin)
        self.db.commit()
        self.db.refresh(admin)

        return {
            "message": "Admin Registered Successfully"
        }

    def login(self, username: str, password: str):

        admin = (
            self.db.query(Admin)
            .filter(Admin.username == username)
            .first()
        )

        if admin is None:
            return None

        if not verify_password(password, admin.password):
            return None

        token = create_access_token(
            {"sub": admin.username}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }