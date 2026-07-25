from openpyxl import Workbook
from sqlalchemy.orm import Session

from app.models.team import Team
from app.models.team_member import TeamMember
from app.models.student import Student


class ExcelService:

    def __init__(self, db: Session):
        self.db = db

    def export_teams(self):

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Teams"

        sheet.append([
            "Team Name",
            "Track",
            "PIN",
            "Student Name",
            "Skill"
        ])

        teams = self.db.query(Team).all()

        for team in teams:

            members = (
                self.db.query(TeamMember)
                .filter(TeamMember.team_id == team.id)
                .all()
            )

            for member in members:

                student = (
                    self.db.query(Student)
                    .filter(Student.id == member.student_id)
                    .first()
                )

                if student:

                    sheet.append([
                        team.team_name,
                        team.track,
                        student.pin,
                        student.name,
                        student.skill
                    ])

        filename = "teams.xlsx"

        workbook.save(filename)

        return filename