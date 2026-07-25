from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentResponse

router = APIRouter()


@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    new_student = Student(
        pin=student.pin,
        name=student.name,
        email=student.email,
        track=student.track,
        skill=student.skill
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student
@router.get("/", response_model=list[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    return students
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        return {"message": "Student not found"}

    return student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        return {"message": "Student not found"}

    student.pin = student_data.pin
    student.name = student_data.name
    student.email = student_data.email
    student.track = student_data.track
    student.skill = student_data.skill

    db.commit()
    db.refresh(student)

    return student
@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        return {"message": "Student not found"}

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}