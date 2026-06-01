from fastapi import FastAPI  # type: ignore[import]
from pydantic import BaseModel  # type: ignore[import]
class Student(BaseModel):
    id: int
    name: str
class updateStudent(BaseModel):
    name: str
app = FastAPI()
students = [
    {"id": 1, "name": "Arun"},
    {"id": 2, "name": "Bharathi"},
    {"id": 3, "name": "Kavin"},
    {"id": 4, "name": "Nisha"},
    {"id": 5, "name": "Priya"}
]
@app.get("/students/{id}")
def idcall(id: int):
    for student in students:
        if student["id"] == id:
            return {"message": student}
    return {"message": "Student not found"}
@app.post("/students")
def create_user(new_user: Student):
    students.append(new_user)
    return {"message": "Student created successfully", "students": students}
@app.put("/students")
def update(id: int, updated_student: updateStudent):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_student.name
            return {"message": "Student updated successfully", "students": students}
    return {"message": "Student not found"}
@app.delete("/students/{id}")
def delete(id: int):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {"message": "Student deleted successfully", "students": students}
    return {"message": "Student not found"}


