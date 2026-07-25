import csv
import io

from fastapi import HTTPException

from app.models.student import Student


class CSVService:

    REQUIRED_COLUMNS = ["PIN", "Name", "Email", "Track", "Skill"]

    VALID_TRACKS = [
        "Full Stack",
        "DevOps",
        "Gen AI"
    ]

    VALID_SKILLS = [
        "Good",
        "Average",
        "Beginner"
    ]

    def __init__(self, db):
        self.db = db

    def import_students(self, file_content: bytes):

        try:
            raw_content = file_content.decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(
                status_code=400,
                detail="CSV file must be UTF-8 encoded."
            )

        csv_reader = csv.DictReader(io.StringIO(raw_content))

        if csv_reader.fieldnames is None:
            raise HTTPException(
                status_code=400,
                detail="CSV file is empty or invalid."
            )

        missing_columns = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in csv_reader.fieldnames
        ]

        if missing_columns:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required columns: {', '.join(missing_columns)}"
            )

        imported_count = 0

        for row in csv_reader:

            pin = row["PIN"].strip()

            existing_student = (
                self.db.query(Student)
                .filter(Student.pin == pin)
                .first()
            )

            if existing_student:
                continue

            track = row["Track"].strip()
            skill = row["Skill"].strip()

            if track not in self.VALID_TRACKS:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid Track: {track}"
                )

            if skill not in self.VALID_SKILLS:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid Skill: {skill}"
                )

            student = Student(
                pin=pin,
                name=row["Name"].strip(),
                email=row["Email"].strip(),
                track=track,
                skill=skill
            )

            self.db.add(student)

            imported_count += 1

        self.db.commit()

        return {
            "message": "Students imported successfully",
            "count": imported_count
        }