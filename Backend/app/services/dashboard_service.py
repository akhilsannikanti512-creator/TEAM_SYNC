from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.track import Track
from app.models.team import Team
from app.models.team_member import TeamMember


class DashboardService:

    def __init__(self, db: Session):
        self.db = db

    def get_dashboard(self):

        total_students = self.db.query(Student).count()
        total_tracks = self.db.query(Track).count()
        total_teams = self.db.query(Team).count()
        total_team_members = self.db.query(TeamMember).count()

        # Track Distribution
        full_stack = (
            self.db.query(Student)
            .filter(Student.track == "Full Stack")
            .count()
        )

        devops = (
            self.db.query(Student)
            .filter(Student.track == "DevOps")
            .count()
        )

        gen_ai = (
            self.db.query(Student)
            .filter(Student.track == "Gen AI")
            .count()
        )

        # Skill Distribution
        good = (
            self.db.query(Student)
            .filter(Student.skill == "Good")
            .count()
        )

        average = (
            self.db.query(Student)
            .filter(Student.skill == "Average")
            .count()
        )

        beginner = (
            self.db.query(Student)
            .filter(Student.skill == "Beginner")
            .count()
        )

        return {
            "total_students": total_students,
            "total_tracks": total_tracks,
            "total_teams": total_teams,
            "total_team_members": total_team_members,

            "track_distribution": {
                "Full Stack": full_stack,
                "DevOps": devops,
                "Gen AI": gen_ai
            },

            "skill_distribution": {
                "Good": good,
                "Average": average,
                "Beginner": beginner
            }
        }