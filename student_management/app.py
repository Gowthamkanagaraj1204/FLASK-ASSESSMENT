from flask import Flask, render_template, abort
app = Flask(__name__)

students = {
    1: {
        "name": "Arun Kumar",
        "age": 20,
        "course": "Python Programming"
    },
    2: {
        "name": "Priya",
        "age": 21,
        "course": "Web Development"
    },
    3: {
        "name": "Karthik",
        "age": 19,
        "course": "Data Science"
    },
    4: {
        "name": "Divya",
        "age": 22,
        "course": "Database Management"
    }
}

@app.route("/")
def home():
    return render_template(
        "home.html",
        students=students
    )

@app.route("/student/<int:student_id>")
def student_details(student_id):
    student = students.get(student_id)

    if student is None:
        abort(404)

    return render_template(
        "student_details.html",
        student=student,
        student_id=student_id
    )

if __name__ == "__main__":
    app.run(debug=True)