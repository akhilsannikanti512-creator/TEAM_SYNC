from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.team_service import TeamService
from app.utils.auth import get_current_admin

router = APIRouter()


# Generate Teams (Protected)
@router.post("/generate")
def generate_teams(
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):

    service = TeamService(db)

    return service.generate()


# Delete All Teams (Protected)
@router.delete("/")
def delete_all_teams(
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):

    service = TeamService(db)

    return service.delete_all_teams()


# Reset Project (Protected)
@router.delete("/reset")
def reset_project(
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):

    service = TeamService(db)

    return service.reset_project()


# View All Teams
@router.get("/")
def get_all_teams(
    db: Session = Depends(get_db)
):

    service = TeamService(db)

    return service.get_all_teams()


# View Team By ID
@router.get("/{team_id}")
def get_team_by_id(
    team_id: int,
    db: Session = Depends(get_db)
):

    service = TeamService(db)

    team = service.get_team_by_id(team_id)

    if team is None:

        raise HTTPException(
            status_code=404,
            detail="Team not found"
        )

    return team