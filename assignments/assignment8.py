from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [
    {"student_id": 1, "name": "John", "age": 18, "grade": "12"},
    {"student_id": 2, "name": "Emily", "age": 17, "grade": "11"},
    {"student_id": 3, "name": "Michael", "age": 16, "grade": "10"},
    {"student_id": 4, "name": "Sophia", "age": 17, "grade": "11"},
    {"student_id": 5, "name": "William", "age": 16, "grade": "10"},
    {"student_id": 6, "name": "Olivia", "age": 18, "grade": "12"},
    {"student_id": 7, "name": "James", "age": 17, "grade": "11"},
    {"student_id": 8, "name": "Emma", "age": 16, "grade": "10"},
    {"student_id": 9, "name": "Alexander", "age": 18, "grade": "12"},
    {"student_id": 10, "name": "Ava", "age": 17, "grade": "11"},
]

# function for update student status
def update_student(student_id: int, student_data: dict):
    for student in students:
        if student['student_id'] == student_id:
            student.update(student_data)
            return {"message": "Student data updated successfully"}
    return {"message": "Student not found"}

#function to add new student in simple way
def post_student(new_student):
    if True:
        new_student_id = int(input("Enter the student ID: "))
        new_student_name = input("Enter the new name: ")
        new_student_age = int(input("Enter the new age: "))
        new_student_grade = input("Enter the new grade: ")
        new_student = {"student_id": new_student_id, "name": new_student_name, "age": new_student_age, "grade": new_student_grade}
        students.append(new_student)
        return {"message": "Student data added successfully"}


# function to delete a student
def delete_student(student_id: int):
    for student in students:
        if student['student_id'] == student_id:
            students.remove(student)
            return {"message": "Student data deleted successfully"}
    return {"message": "Student not found"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Crud Operations"}

@app.get("/students")
def read_students():
    return students

@app.get("/students/{student_id}")
def read_student(student_id: int):
    for student in students:
        if student['student_id'] == student_id:
            return student
    return {"message": "Student not found"}

@app.post("/students/update/{student_id}")
def update_student_route(student_id: int, student_data: dict):
    return update_student(student_id, student_data)

@app.post("/students/addnew")
def add_student(new_student: dict):
    return post_student(new_student)

@app.delete("/students/delete/{student_id}")
def delete_student_route(student_id: int):
    return delete_student(student_id)

def run_scripter():
    return uvicorn.run(app, host="127.0.0.1", port=8000)

run_scripter()