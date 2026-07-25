from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_students: int
    total_tracks: int
    total_teams: int
    total_team_members: int