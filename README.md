First of all we need to import modules like fastapi, uvicorn

Then I will create a decsionary in the dictionary

After that i will create functions to upadte student data, add new student and delete student data

After that i will create APIs to get Data
In firts API i will define root location   # @app.get("/")  output is {"message": "Welcome to the Student Crud Operations"}

In second API i will define route to get all  #  @app.get("/students")

In third API i will define route to get specific students  #  @app.get("/students/{student_id}")

In fourth API i will define route to upadte student data  #  @app.post("/students/update/{student_id}")

In fifth API i will define route to add new students  #  @app.post("/students/addnew")

In sixth API i will define route to delete a student   #  @app.delete("/students/delete/{student_id}")

on the last i will write uvicorn funtion to go live on local server