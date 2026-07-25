from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.track import Track
from app.models.team import Team
from app.models.team_member import TeamMember

from app.services.team_generator import TeamGenerator


class TeamService:

    def __init__(self, db: Session):
        self.db = db

    def generate(self):

        generator = TeamGenerator()

        # Delete previous generated teams
        self.db.query(TeamMember).delete()
        self.db.query(Team).delete()
        self.db.commit()

        # Fetch ALL students at once (no per-track looping).
        all_students = self.db.query(Student).all()

        all_teams = {}

        if not all_students:
            return all_teams

        generated_teams = generator.create_balanced_teams(all_students)

        formatted_teams = []

        team_number = 1

        for team in generated_teams:

            db_team = Team(
                team_name=f"Team {team_number}",
                track="Mixed"
            )

            self.db.add(db_team)
            self.db.commit()
            self.db.refresh(db_team)

            formatted_team = []

            for student in team:

                db_member = TeamMember(
                    team_id=db_team.id,
                    student_id=student.id
                )

                self.db.add(db_member)

                formatted_team.append({
                    "id": student.id,
                    "pin": student.pin,
                    "name": student.name,
                    "track": student.track,
                    "skill": student.skill
                })

            self.db.commit()

            formatted_teams.append(formatted_team)

            team_number += 1

        all_teams["Mixed"] = formatted_teams

        return all_teams

    def get_all_teams(self):

        teams = self.db.query(Team).all()

        result = []

        for team in teams:

            members = (
                self.db.query(TeamMember)
                .filter(TeamMember.team_id == team.id)
                .all()
            )

            team_data = {
                "id": team.id,
                "team_name": team.team_name,
                "track": team.track,
                "members": []
            }

            for member in members:

                student = (
                    self.db.query(Student)
                    .filter(Student.id == member.student_id)
                    .first()
                )

                if student:

                    team_data["members"].append({
                        "id": student.id,
                        "pin": student.pin,
                        "name": student.name,
                        "track": student.track,
                        "skill": student.skill
                    })

            result.append(team_data)

        return result

    def get_team_by_id(self, team_id: int):

        team = (
            self.db.query(Team)
            .filter(Team.id == team_id)
            .first()
        )

        if not team:
            return None

        members = (
            self.db.query(TeamMember)
            .filter(TeamMember.team_id == team.id)
            .all()
        )

        result = {
            "id": team.id,
            "team_name": team.team_name,
            "track": team.track,
            "members": []
        }

        for member in members:

            student = (
                self.db.query(Student)
                .filter(Student.id == member.student_id)
                .first()
            )

            if student:

                result["members"].append({
                    "id": student.id,
                    "pin": student.pin,
                    "name": student.name,
                    "track": student.track,
                    "skill": student.skill
                })

        return result

    def delete_all_teams(self):
        """
        Delete all generated teams and their members.
        """

        self.db.query(TeamMember).delete()
        self.db.query(Team).delete()

        self.db.commit()

        return {
            "message": "All generated teams deleted successfully."
        }

    def reset_project(self):
        """
        Delete all students, teams and team members.
        """

        self.db.query(TeamMember).delete()
        self.db.query(Team).delete()
        self.db.query(Student).delete()

        self.db.commit()

        return {
            "message": "Project reset successfully."
        }